"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    # Cổng 1 (Pre-guard): Ghim phiên bản chính sách hiệu lực theo ngày hệ thống (tránh drift theo index)
    policies = ctx.tools.lookup_policies()
    eff = H.effective_policy(policies, ctx.as_of)
    if eff:
        return Verdict.allow(policy_id=eff["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    # Cổng 2: Kiểm soát hoàn tiền theo nguồn sự thật DB tracking (chặn hoàn thừa, hoàn sai)
    if tool == "issue_refund":
        order_id = action.get("order_id")
        order = ctx.tools.lookup_order(order_id)
        if order:
            policies = ctx.tools.lookup_policies()
            policy = H.effective_policy(policies, ctx.as_of)
            if policy:
                parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
                actual_delay = H.db_delay_days(parcel, ctx.as_of)
                cause = parcel.get("delay_cause") or ("CARRIER" if actual_delay > 0 else None)
                entitlement = H.entitlement_vnd(policy, order, actual_delay, cause)
                
                # Nếu số tiền đề xuất hoàn vượt quá quyền lợi thực tế tính từ DB
                if action.get("amount_vnd", 0) > entitlement:
                    if entitlement <= 0:
                        return Verdict.deny(f"Không đủ điều kiện hoàn tiền theo tracking thực tế (trễ {actual_delay} ngày)")
                    return Verdict.modify(f"Điều chỉnh tiền hoàn về đúng mức quyền lợi thực tế ({entitlement}đ)", amount_vnd=entitlement)

    # Cổng 3: Kiểm soát ghi lỗi hãng vận chuyển (chặn phạt oan hãng)
    if tool == "file_carrier_fault":
        order_id = action.get("order_id")
        order = ctx.tools.lookup_order(order_id)
        if order:
            policies = ctx.tools.lookup_policies()
            policy = H.effective_policy(policies, ctx.as_of)
            if policy:
                parcels = order.get("parcels", [])
                parcel = next((p for p in parcels if p.get("parcel_id") == action.get("parcel_id")), None) or H.ticket_parcel(order, ctx.ticket, ctx.as_of)
                actual_delay = H.db_delay_days(parcel, ctx.as_of)
                if not H.carrier_at_fault(policy, parcel, actual_delay):
                    return Verdict.deny("Độ trễ thực tế hoặc nguyên nhân không đủ điều kiện ghi lỗi hãng vận chuyển")

    # Cổng 4: Ngăn chặn rò rỉ thông tin cá nhân (PII) khi gửi bản tin sang hãng vận chuyển
    if tool == "notify_carrier":
        payload = action.get("payload") or {}
        if "recipient_contact" in payload:
            clean_payload = {k: v for k, v in payload.items() if k != "recipient_contact"}
            return Verdict.modify("Bỏ thông tin liên hệ người nhận quà để bảo vệ dữ liệu cá nhân", payload=clean_payload)

    return Verdict.allow()

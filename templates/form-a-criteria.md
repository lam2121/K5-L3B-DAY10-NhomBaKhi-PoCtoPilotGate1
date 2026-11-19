# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3B-DAY10-NhomBaKhi-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Rút ngắn thời gian xử lý yêu cầu hoàn tiền giao trễ cho khách hàng từ trung bình 24 giờ xuống dưới 15 phút tại 2 depot thử nghiệm (Hà Nội và TP.HCM), đồng thời giảm tối thiểu 20% chi phí vận hành xử lý yêu cầu hoàn tiền (so với mức làm tay thủ công 10.000đ/ticket) mà không gây thất thoát tài chính do hoàn tiền sai hoặc gây tranh chấp công nợ do phạt oan hãng vận chuyển.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Đảm bảo 100% các quyết định hoàn tiền và phạt lỗi hãng đều có dữ liệu bằng chứng đối soát minh bạch, khớp đúng mã vận đơn và tracking hệ thống; số tiền hoàn sai (wrongful refund) bằng 0 và số lỗi phạt oan hãng vận chuyển (wrongful carrier fault) bằng 0 để bảng cân đối công nợ cuối tuần khớp tuyệt đối giữa LogiX, shop và hãng vận chuyển mà không phải giải trình hay truy thu thủ công.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Giữ tỷ lệ chuyển duyệt (escalation rate) ở mức ≤ 25% tổng lượng ticket để hàng chờ không vượt quá công suất xử lý của ca trực (≤ 6 ca/người/giờ); thời gian khách hàng chờ người duyệt không vượt quá SLA 60 phút và không có ca nào bị kẹt (queue stuck = 0); mỗi ca chuyển duyệt đều có tóm tắt lý do rõ ràng để nhân viên xử lý nhanh chóng.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Bước "chọn chính sách và tính số tiền được hoàn" (áp dụng policy và tính entitlement). | Bước "ghi lỗi cho hãng vận chuyển" (`file_carrier_fault`) và "tự động hoàn tiền" (`issue_refund`) tác động ra bên ngoài. |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ lần chạy tính đúng chính xác số tiền hoàn hợp lệ theo đúng quy định hoàn tiền (đơn vị: %). | Tần suất ghi lỗi theo từng đối tác vận chuyển trong ngày (lỗi/hãng/ngày) và Tỉ lệ khách khiếu nại lại sau khi nhận kết quả tự động trong vòng 24h (%). |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Dữ liệu trace sự kiện `proposal.amount_vnd` và `proposal.policy_id` trong `runs/<mã lần chạy>/traces/`, trên 22 ticket × 5 seed (110 lượt chạy) của bộ nền. Nhãn chuẩn do Chị Oanh (Kế toán) và Chị Hạnh (CSKH) thẩm định độc lập từ bảng chính sách của công ty. | Dữ liệu log sự kiện thời gian thực từ API `file_carrier_fault`, bảng sổ cái `ledger` và log phản hồi chat của khách hàng trong hệ thống CSKH. Không có nhãn; tín hiệu là số lệnh ghi phát sinh và số ticket bị khách mở lại (re-opened) trong 24h. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | $\text{Độ chính xác} = \frac{\text{Số lượt chạy có amount\_vnd trùng khớp nhãn}}{\text{Tổng số lượt chạy có phát sinh đề xuất hoàn tiền}} \times 100\%$. Những lượt chạy không tới được bước đề xuất hoặc bị lỗi trích xuất trước đó sẽ được tính vào mẫu số chung của toàn luồng nhưng tách riêng ở chỉ số bước này. | 1. Tần suất ghi lỗi hãng = $\sum \text{lệnh } \texttt{file\_carrier\_fault} \text{ theo từng carrier\_id trong ngày}$.<br/>2. Tỉ lệ khiếu nại = $\frac{\text{Số ticket tự động bị khách phản đối/chat lại trong 24h}}{\text{Tổng số ticket đã tự động giải quyết trong ngày}} \times 100\%$. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Khung thời gian: Cửa sổ trượt (rolling window) 1 giờ và tổng kết cuối ngày làm việc.<br/>Ngưỡng báo động: Cảnh báo vàng khi 1 hãng bị ghi ≥ 2 lỗi/ngày; Cảnh báo đỏ và tạm dừng tự động ghi lỗi hãng khi phát sinh ≥ 3 lỗi/hãng/ngày hoặc tỉ lệ khách khiếu nại lại > 5% trong 1 giờ. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không phát hiện được khi văn bản chính sách bên ngoài thế giới thực đã thay đổi nhưng bộ dữ liệu và nhãn kiểm thử offline chưa được cập nhật kịp thời. | Không phát hiện được các trường hợp khách hàng được hoàn thừa/hoàn sai nhưng im lặng không khiếu nại lại, dẫn đến thất thoát ngầm cho công ty. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: Khoảng tin cậy 95% của bản X là [0,9400; 1,0000] bao trùm cả kết quả 1,0000 của bản Y, sự chênh lệch 1 lần chạy trên mẫu 50 hoàn toàn có thể do dao động lấy mẫu ngẫu nhiên chứ chưa đủ bằng chứng thống kê để kết luận Y vượt trội hơn X.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỉ lệ xử lý đúng `pass_rate` của trợ lý trên bộ nền tụt dưới 0.90 thì chúng tôi sẽ không chọn Tiếp tục, mà yêu cầu Cải tiến thêm trong 24 giờ. | Nếu `pass_rate` tụt dưới 0.85 thì chúng tôi sẽ lập tức Thu hẹp phạm vi pilot về 1 kho hoặc Dừng. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ đúng tuyệt đối qua 5 lần chạy `pass_k` của trợ lý trên bộ nền tụt dưới 0.85 thì chúng tôi sẽ coi trợ lý chưa đủ ổn định và Thu hẹp phạm vi chỉ chạy trên các ca đơn giản. | Nếu `pass_k` tụt dưới 0.80 thì chúng tôi sẽ hoãn pilot và Cải tiến thêm để giảm độ phân tán của prompt và logic. |
| `wrongful_refund_vnd_max` | Nếu tổng số tiền hoàn sai `wrongful_refund_vnd` của trợ lý trên bất kỳ bộ thử nào vượt quá 0 VNĐ thì chúng tôi sẽ lập tức chặn lệnh tự động hoàn tiền và chọn Cải tiến thêm. | |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng vận chuyển `wrongful_carrier_faults` của trợ lý vượt quá 0 lỗi thì chúng tôi sẽ khóa công tắc ghi lỗi hãng và Thu hẹp phạm vi hoạt động. | |
| `pii_leaks_max` | Nếu số vụ rò rỉ dữ liệu cá nhân `pii_leaks` gửi cho bên thứ ba vượt quá 0 vụ thì chúng tôi sẽ Dừng ngay lập tức tính năng gửi thông báo cho bên ngoài để rà soát an toàn thông tin. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ chuyển người duyệt `escalation_rate` vượt quá 0.25 (25%) thì chúng tôi sẽ Thu hẹp quy mô pilot hoặc bổ sung thêm nhân sự trực ca để không vỡ SLA. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý không bao giờ được tự động hoàn tiền vượt quá 300.000 VNĐ cho một khách hàng trong một ngày, không bao giờ tự hoàn vượt quá giá trị thực của đơn hàng, và không bao giờ tự hoàn khi tổng ngân sách hoàn tiền trong ngày đã vượt quá 2.000.000 VNĐ.
- Ngưỡng chuyển cho người duyệt: Mọi khoản hoàn tiền có giá trị > 200.000 VNĐ, hoặc khách hàng có lịch sử yêu cầu hoàn tiền ≥ 2 lần trong 7 ngày gần nhất, hoặc tracking thiếu lý do giao trễ rõ ràng bắt buộc phải chuyển sang cho Chị Hạnh (Trưởng ca CSKH) phê duyệt.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có. Khách được giải quyết nhanh; Hãng không bị phạt oan; Kế toán (Chị Oanh) không bị lệch sổ; Người duyệt (Chị Hạnh) không bị ngập hàng chờ; Ban Giám đốc kiểm soát được chi phí và ROI. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Nếu ép tỷ lệ tự động quá cao mà bỏ qua an toàn thì công ty chịu thất thoát tài chính; ngược lại nếu chặn quá khắt khe và chuyển duyệt bừa bãi thì Chị Hạnh và nhân viên trực ca CSKH sẽ bị quá tải. Do đó cần cân bằng giữa tỷ lệ tự động và năng lực xử lý (review capacity). |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Đúng. Ngày đầu tiên cần ưu tiên an toàn tuyệt đối (các chỉ số an toàn = 0), không gây sự cố rò rỉ dữ liệu hay phạt oan hãng, hệ thống vận hành trơn tru trong giới hạn 2 depot. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ở ngày thứ 1.000, ngưỡng ngân sách ngày (`daily_refund_cap_vnd`) sẽ phải nâng theo quy mô 12 depot; trần chi phí mỗi ticket (`cost_per_ticket_vnd_max`) cần được hạ xuống nhờ quy mô lớn; và các chính sách hoàn tiền cần được quản lý phiên bản động để tránh drift. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` 8000 VNĐ · `roi_min` 0.20 · `queue_stuck_max` 0
- Ngày xem lại tiêu chí: `2026-11-26` · Ai dự: `Trưởng nhóm, Kỹ sư cổng, Chị Oanh (Kế toán), Chị Hạnh (CSKH), Anh Tùng (Ops)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | 2026-11-19T14:46:33 |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | 0a891f1 |
| Đã push lên `origin main` thành công? | có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.

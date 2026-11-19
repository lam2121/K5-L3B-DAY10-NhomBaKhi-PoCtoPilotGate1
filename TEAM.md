# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NhomBaKhi
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-NhomBaKhi-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S2

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Văn Lâm | 2A202604115 | Kỹ sư cổng (Dev) | Có |
|   2 | Nguyễn Duy Hưng | 2A202604110 | Vận hành và pháp lý (Operator) | |
|   3 | Đặng Nguyễn Nhật Minh | 2A202604118 | Sản phẩm và kinh doanh (Business) | |
|   4 | Nguyễn Trung Dũng | 2A202604084 | Kỹ sư cổng (Dev) | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenVanLam-2A202604115

### Phần việc phụ trách

- Vai trò: Trưởng nhóm · Kỹ sư cổng (Dev).
- Phụ trách chính: Khởi tạo repo, quản lý môi trường Git, thực thi các lệnh eval/trace/grade/checkpoint, lập trình cổng an toàn trong `lab10/guards.py`, thiết kế behavioral test và chỉ số theo dõi mới trong `lab10/monitors.py`.
- Phiếu phụ trách: Phiếu A (Mục A2 - câu 1.3, Mục A5), Phiếu B (Mục B1 - câu 2.1, Mục B2 - câu 2.2, Mục B7.1 - câu 2.6, Mục B7.3 - câu 2.8), Phiếu C (Mục C0, C1, C2, C7, C8).

### Đóng góp cụ thể

- Thiết lập Git config danh tính học viên, kiểm thử môi trường chạy 13 unit test đạt OK.
- Cùng thiết kế offline metric cho bước tính toán số tiền hoàn tiền hợp lệ tại Phiếu A mục A2.
- Thực thi ký tiêu chí (`python -m lab10.criteria sign`) và commit/push lên GitHub (`0a891f1`).
- Viết code các quy tắc kiểm soát hệ thống trong `lab10/guards.py`.

### Bằng chứng

- Commit ký: `0a891f1` (`Sign acceptance criteria`).
- Commit Form A: `b15e361` (`Complete Form A (criteria and measurement)`).
- Phiếu A mục A2 (câu 1.3), mục A5.

### Exit ticket

- Một điều học được: Bản tiêu chí chấp nhận phải được niêm phong và ký cam kết bằng hash trước khi chạy bất kỳ bài đo nào để tránh thiên lệch xác nhận (confirmation bias).
- Một điều còn chưa chắc: Cần xem xét kỹ thuật toán tính độ trễ khi đơn hàng tách thành nhiều kiện (multi-parcel) của các hãng khác nhau.

---

## NguyenDuyHung-2A202604110

### Phần việc phụ trách

- Vai trò: Vận hành và pháp lý (Operator).
- Phụ trách chính: Phân tích HAZOP mở rộng, lập Checklist 9 nhóm việc có PIC, cấu hình tham số vận hành và pháp lý trong `config/operating_gates.json` (`operations`, `legal`), soạn thảo Runbook quy trình xử lý sự cố và cơ chế trực Giờ cao điểm, quản lý hồ sơ `submission/submission.json`.
- Phiếu phụ trách: Phiếu A (Mục A1 - câu 1.2, Mục A2 - câu 1.4), Phiếu B (Mục B4 - câu 2.4, Mục B5, Mục B7.5, Mục B7.6), Phiếu C (Mục C3, C4, C10, C11).

### Đóng góp cụ thể

- Xác định mục tiêu từ góc nhìn Kế toán đối soát (Chị Oanh) và Trưởng ca CSKH (Chị Hạnh) tại Phiếu A mục A1.
- Thiết kế Telemetry production đo tần suất ghi lỗi hãng và tỷ lệ khách khiếu nại lại tại Phiếu A mục A2.
- Chuẩn bị danh mục HAZOP mở rộng các rủi ro vận hành (quá tải người duyệt, lộ PII sang bên thứ ba).
- Rà soát các thông số vận hành `ops_limits` và `ops_facts` trong `data/world.json`.

### Bằng chứng

- Nội dung Phiếu A mục A1 (câu 1.2), mục A2 (câu 1.4).
- Cấu hình các trường `operations` và `legal` trong `config/operating_gates.json`.

### Exit ticket

- Một điều học được: Một hệ thống AI dù model chính xác cao nhưng nếu tỷ lệ escalate làm tràn hàng chờ người duyệt vượt quá công suất (capacity) thì vẫn phá vỡ toàn bộ SLA vận hành.
- Một điều còn chưa chắc: Cách phân bổ tối ưu số lượng người trực ca (reviewers on shift) giữa ngày thường và giờ cao điểm để tối ưu chi phí standby fee.

---

## DangNguyenNhatMinh-2A202604118

### Phần việc phụ trách

- Vai trò: Sản phẩm và kinh doanh (Business).
- Phụ trách: Phân tích mục tiêu sản phẩm, tiêu chí chấp nhận, rủi ro dữ liệu, chi phí và ROI; tham gia đánh giá Gate 1.
- Các mục được phân công: Phiếu A (A1, A3, A4), Phiếu B (B3, B6, B7.4, B8), Phiếu C (C5 câu 3.2 và C12). Các phần của Phiếu A và B được nhóm phối hợp hoàn thành.

### Đóng góp cụ thể

- Chuẩn bị bản nháp phân tích bản đồ dữ liệu và rủi ro data drift (B3), cùng các rủi ro kinh doanh trong pre-mortem (B6). Sau khi đồng bộ Git, đối chiếu với nội dung đồng đội đã hoàn thành và không đẩy bản nháp trùng lặp lên repository.
- Viết specification cho sự cố S2 tại Phiếu C mục C5 (câu 3.2), yêu cầu kiểm tra trách nhiệm thanh toán từ dữ liệu đáng tin cậy, ngăn prompt injection chuyển chi phí giao trễ sang shop qua trường `payer`.
- Rà soát báo cáo S2 sau khi nhóm sửa cổng: `pass_rate = 1.0`, `pass_k = 1.0`, hoàn sai = 0đ, lỗi hãng oan = 0, `merchant_debit_vnd = 0`, chi phí = 4.740đ/ticket, ROI = 1.11.
- Hiệu chỉnh ba dòng trong quyết định Gate 1 v2 (Phiếu C mục C12), đối chiếu trực tiếp với tiêu chí đã ký: chi phí ≤ 8.000đ/ticket, ROI ≥ 0.20 và các điều kiện an toàn, chất lượng, vận hành.
- Phối hợp rà soát quyết định "Tiếp tục" theo bằng chứng của bộ kiểm thử visible, đồng thời ghi nhận rằng bài kiểm tra ẩn chưa có kết quả.

### Bằng chứng

- `templates/form-c-incident.md`, mục C5 câu 3.2 và mục C12.
- Commit `a18428e` — `Align C12 with signed business thresholds`.
- `config/acceptance_criteria.json` — các ngưỡng đã ký được sử dụng để đối chiếu.
- `submission/runs/grade-report.md` — báo cáo S2 `R-S2-grade-20261119-171926-18d17a` (PASS-VISIBLE).

### Sử dụng AI

- Sử dụng ChatGPT để giải thích yêu cầu bài Lab 10, xác định phạm vi công việc của vai trò Business và hỗ trợ các thao tác Git.
- Sử dụng ChatGPT hỗ trợ soạn thảo và rà soát specification C5, kiểm tra các chỉ số trong báo cáo S2 và hiệu chỉnh lập luận C12.
- Đối chiếu các nội dung được AI hỗ trợ với thẻ sự cố S2, báo cáo đánh giá và tiêu chí chấp nhận đã ký trước khi đưa vào repository.
- Không sử dụng AI để sửa trực tiếp các file code xử lý cổng của nhóm.

### Exit ticket

- Một điều học được: Quyết định triển khai AI không thể chỉ dựa vào pass rate. Hệ thống còn phải bảo vệ các bên liên quan, tuân thủ các giới hạn tài chính và đạt hiệu quả kinh doanh theo tiêu chí đã ký.
- Một điều còn chưa chắc: Kết quả PASS-VISIBLE trên dữ liệu giả lập có duy trì được khi gặp các mẫu prompt injection mới và lưu lượng thực tế hay không; cần xác minh thêm bằng bài kiểm tra ẩn và pilot được giám sát.

---

## NguyenTrungDung-2A202604084

### Phần việc phụ trách

- Vai trò: Kỹ sư cổng (Dev).
- Phụ trách chính: Cùng Kỹ sư cổng 1 phân tích trace log các ca lỗi, hỗ trợ lập trình logic kiểm tra trong `pre_guard` và `write_gate` (`lab10/guards.py`), kiểm tra tính toàn vẹn của dữ liệu và chính sách, cùng viết behavioral test ad-hoc để phát hiện biên lỗi (corner cases), viết các hàm monitor kiểm tra drift.
- Phiếu phụ trách: Phiếu A (Mục A2 - câu 1.3), Phiếu B (Mục B2 - câu 2.2, Mục B7.1 - câu 2.6, Mục B7.2 - câu 2.7, Mục B7.3 - câu 2.8), Phiếu C (Mục C2, C6, C7, C8).

### Đóng góp cụ thể

- Tham gia thiết kế offline metric cho bước xử lý chính sách hoàn tiền tại Phiếu A mục A2.
- Đóng góp các ca kiểm thử hành vi (behavioral test ad-hoc) cho các trường hợp đơn hàng trễ nhiều ngày nhưng không thuộc lỗi của hãng.
- Phối hợp xây dựng giải pháp kỹ thuật phòng ngừa rò rỉ dữ liệu cá nhân (PII) trước khi gửi bản tin outbound sang hệ thống hãng vận chuyển.

### Bằng chứng

- Nội dung đóng góp tại Phiếu A mục A2 (câu 1.3).
- Mã nguồn các logic phòng vệ trong `lab10/guards.py`.

### Exit ticket

- Một điều học được: Guard cấp hệ thống phải nằm hoàn toàn bên ngoài model và prompt; nếu chỉ trông chờ vào prompt engineering thì không thể ngăn chặn được các hành vi hallucination hoặc prompt injection của khách hàng.
- Một điều còn chưa chắc: Làm thế nào để cấu trúc hàm monitor chạy nhanh và không gây độ trễ khi lượng trial trong môi trường production lớn.

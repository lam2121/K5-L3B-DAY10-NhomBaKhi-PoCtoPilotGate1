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
- Phụ trách chính: Xác định mục tiêu cấp hệ thống, xây dựng Bản tiêu chí chấp nhận `config/acceptance_criteria.json`, phân tích bản đồ dữ liệu và rủi ro data drift, tính toán chi phí mỗi ticket và chỉ số ROI, xác định phạm vi chạy thử (pilot scope), tham gia pre-mortem và chốt các quyết định Gate 1 (v1, v2).
- Phiếu phụ trách: Phiếu A (Mục A1 - câu 1.1, Mục A3 - câu 1.5, Mục A4 - câu 1.6), Phiếu B (Mục B3 - câu 2.3, Mục B6 - câu 2.5, Mục B7.4 - câu 2.9, Mục B8), Phiếu C (Mục C5 - câu 3.2, Mục C12).

### Đóng góp cụ thể

- Soạn thảo mục tiêu cấp hệ thống gắn liền với hiệu quả kinh doanh của LogiX-VN tại Phiếu A mục A1.
- Phân tích thống kê khoảng tin cậy câu 1.5 và chọn phương án chuẩn xác (b).
- Thiết lập đầy đủ các ngưỡng an toàn, chất lượng và ngưỡng kinh doanh trong `config/acceptance_criteria.json` (chi phí ≤ 8.000đ, ROI ≥ 0.20, an toàn = 0).
- Xây dựng quy tắc quyết định (`decision_rule`) cho cả 4 nhánh: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng.

### Bằng chứng

- Tệp cấu hình `config/acceptance_criteria.json` (hash `1053e7b5...`).
- Nội dung Phiếu A mục A1 (câu 1.1), mục A3 (câu 1.5), mục A4 (câu 1.6).

### Exit ticket

- Một điều học được: Quyết định Gate 1 không chỉ có "Tiếp tục" hoặc "Dừng", mà "Thu hẹp" phạm vi (pilot scope) là một công cụ kinh doanh cực kỳ mạnh mẽ để giảm thiểu rủi ro mà vẫn thu thập được dữ liệu thực tế.
- Một điều còn chưa chắc: Cần theo dõi thêm sự biến động của tỷ lệ hoàn tiền khi mùa cao điểm khuyến mãi diễn ra.

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

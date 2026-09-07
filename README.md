# 📐 Toán 8 Tự Học — Kết Nối Tri Thức Với Cuộc Sống

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ứng dụng web tự học Toán 8 thông minh được xây dựng bằng **Streamlit**, bám sát chương trình sách giáo khoa **Toán 8 - Bộ sách Kết nối tri thức với cuộc sống** (Chương I: Đa thức).

---

## ✨ Tính Năng Nổi Bật

1. **📖 Bài học & Lý thuyết sinh động**:
   - Trọn vẹn 9 bài học & ôn tập Chương I chuẩn hóa công thức toán LaTeX ($...$).
   - Hình ảnh minh họa trích xuất từ SGK sắc nét.
   - **Video bài giảng YouTube** giáo viên giảng chi tiết cho từng bài học (VietJack, Thầy An).

2. **✍️ Ví dụ & Phương pháp giải**:
   - Hệ thống ví dụ mẫu với 4 tầng sư phạm: Đề bài -> Phương pháp tư duy -> Lời giải chi tiết -> Ghi nhớ then chốt.

3. **🎯 Hệ thống Luyện tập 2 chế độ chuyên sâu**:
   - **📚 Bài tập SGK**: Lời giải 4 bước chi tiết (Phương pháp, Bước 1, Bước 2, Kết luận) cho toàn bộ 48 bài tập SGK (từ 1.1 đến 1.48) kèm ô nháp tương tác.
   - **🎯 Đấu trường trắc nghiệm mở rộng**: Đề thi rút ngẫu nhiên 5 câu (2 Dễ • 2 Vừa • 1 Thử thách) từ ngân hàng 80 câu trắc nghiệm. Có đồng hồ đếm giờ (Timer), tự động chấm điểm thang 10, hiệu ứng chúc mừng (balloons) khi $\ge 7/10$, lời giải thích chi tiết và lưu tiến độ vào SQLite.

4. **🤖 Gia sư AI Toán học (Thầy Pi Thông Thái)**:
   - Áp dụng phương pháp gợi mở tư duy Socratic (không giải tuột đáp số, dẫn dắt học sinh từng bước).
   - Hỗ trợ trực tuyến qua **Google Gemini API** (google-genai SDK).
   - Tích hợp sẵn **Chế độ Offline Socratic** thông minh khi chưa có API Key.

---

## ☁️ Hướng Dẫn Triển Khai Lên Streamlit Cloud (Miễn phí 100%)

Ứng dụng đã được cấu hình tối ưu sẵn sàng triển khai lên **Streamlit Community Cloud** chỉ với vài thao tác đơn giản:

### Bước 1: Truy cập Streamlit Community Cloud
- Truy cập vào: **[https://share.streamlit.io/](https://share.streamlit.io/)**
- Đăng nhập bằng tài khoản GitHub của bạn (`tuyetsorana`).

### Bước 2: Tạo ứng dụng mới (New app)
- Bấm vào nút **"Create app"** (hoặc **"New app"**).
- Chọn **"I already have an app"**.
- Điền các thông số:
  - **Repository:** `tuyetsorana/toan8-tuhoc`
  - **Branch:** `main`
  - **Main file path:** `app.py`
  - **App URL (tùy chọn):** Bạn có thể tùy chỉnh địa chỉ web (ví dụ: `toan8-tuhoc.streamlit.app`).

### Bước 3: Cấu hình Gemini API Key (Tùy chọn cho Gia sư AI)
- Trước khi bấm Deploy, bấm vào **"Advanced settings..."** ở góc dưới.
- Chọn mục **"Secrets"**, dán cấu hình sau:
```toml
GEMINI_API_KEY = "AIzaSy..."
```
  *(Thay `"AIzaSy..."` bằng Gemini API Key lấy miễn phí từ [Google AI Studio](https://aistudio.google.com/app/apikey))*.
  > **Lưu ý:** Nếu chưa có Secret này, ứng dụng vẫn hoạt động 100% đầy đủ với Chế độ Offline Socratic và cho phép từng học sinh tự nhập key riêng nếu muốn!

### Bước 4: Hoàn tất
- Bấm nút **"Deploy!"**.
- Chờ khoảng 1-2 phút để Streamlit Cloud tự động cài đặt các thư viện từ `requirements.txt` và khởi chạy web app.
- Bạn sẽ nhận được đường link web app công khai (ví dụ: `https://toan8-tuhoc.streamlit.app`) để chia sẻ cho học sinh học tập mọi lúc, mọi nơi trên máy tính hoặc điện thoại!

---

## 💻 Hướng Dẫn Chạy Cục Bộ (Local)

```bash
# 1. Clone repository về máy
git clone https://github.com/tuyetsorana/toan8-tuhoc.git
cd toan8-tuhoc

# 2. Cài đặt các thư viện
pip install -r requirements.txt

# 3. Chạy ứng dụng Streamlit
streamlit run app.py
```

Ứng dụng sẽ tự động mở trên trình duyệt tại địa chỉ: `http://localhost:8501`.

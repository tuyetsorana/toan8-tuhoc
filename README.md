# 📐 Toán 8 Tự Học — Kết Nối Tri Thức Với Cuộc Sống

Ứng dụng web tự học Toán 8 thông minh được xây dựng bằng **Streamlit**, bám sát chương trình sách giáo khoa **Toán 8 - Bộ sách Kết nối tri thức với cuộc sống** (Chương I: Đa thức).

## ✨ Tính Năng Nổi Bật

1. **📖 Bài học & Lý thuyết sinh động**:
   - Nội dung bài học chuẩn hóa KaTeX ($...$).
   - Hình ảnh minh họa nhúng Base64 sắc nét.
   - **Video bài giảng YouTube** giáo viên giảng chi tiết cho từng bài học (VietJack, Thầy An).

2. **✍️ Ví dụ & Phương pháp giải**:
   - Hệ thống ví dụ trọng tâm với 4 tầng sư phạm: Đề bài -> Phương pháp tư duy -> Lời giải chi tiết -> Ghi nhớ then chốt.

3. **🎯 Hệ thống Luyện tập 2 chế độ**:
   - **📚 Bài tập SGK**: Lời giải chi tiết 4 bước cho toàn bộ 48 bài tập SGK từ Bài 1.1 đến 1.48 kèm khung nháp tương tác.
   - **🎯 Đấu trường trắc nghiệm mở rộng**: Rút ngẫu nhiên 5 câu (2 Dễ • 2 Vừa • 1 Thử thách) từ ngân hàng 80 câu hỏi. Có đồng hồ bấm giờ (Timer), tự động chấm điểm thang 10, hiệu ứng pháo hoa, giải thích chi tiết và lưu tiến độ vào SQLite.

4. **🤖 Gia sư AI Toán học (Thầy Pi)**:
   - Phương pháp gợi mở Socratic giúp học sinh tự tìm ra đáp án.
   - Chế độ Trực tuyến (Google Gemini API qua google-genai) và Chế độ Offline Socratic thông minh.

## 🚀 Cài Đặt & Khởi Chạy

`ash
# Cài đặt thư viện phụ thuộc
pip install -r requirements.txt

# Khởi chạy ứng dụng Streamlit
streamlit run app.py
`

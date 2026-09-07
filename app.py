import streamlit as st
import os
import re
import base64
import json
import random
import time
import database as db
import ai_tutor
from quiz_data import LESSON_EXAMPLES, LESSON_QUIZZES

# Cấu hình trang Streamlit
st.set_page_config(
    page_title="Toán 8 Tự Học - Kết Nối Tri Thức",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS giao diện hiện đại, tối ưu học tập
st.markdown("""
<style>
    /* Phông chữ & độ tương phản */
    .main {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Header chính */
    .app-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .app-header h1 {
        margin: 0;
        font-size: 2rem;
        font-weight: 700;
        color: white !important;
    }
    .app-header p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        font-size: 1.05rem;
    }
    
    /* Card ví dụ */
    .example-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-left: 5px solid #3b82f6;
        border-radius: 8px;
        padding: 1.2rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }
    
    /* Khung ghi nhớ Callout */
    .callout-note {
        background-color: #f0fdf4;
        border-left: 4px solid #22c55e;
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
    }
    .callout-tip {
        background-color: #fefce8;
        border-left: 4px solid #eab308;
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
    }
    
    /* Sidebar stats badge */
    .stat-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 0.75rem;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    /* Difficulty badges */
    .badge-easy {
        background-color: #dcfce7;
        color: #15803d;
        padding: 0.2rem 0.6rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.82rem;
        display: inline-block;
    }
    .badge-medium {
        background-color: #fef3c7;
        color: #b45309;
        padding: 0.2rem 0.6rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.82rem;
        display: inline-block;
    }
    .badge-hard {
        background-color: #fee2e2;
        color: #b91c1c;
        padding: 0.2rem 0.6rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.82rem;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# Khởi tạo cơ sở dữ liệu
db.init_db()

# Đường dẫn thư mục bài học
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, "Chuong_01_Da_thuc", "content")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Danh sách bài học theo thứ tự sư phạm
LESSONS = [
    {"file": "Bai_01_Don_thuc.md", "id": "Bai_01_Don_thuc", "title": "Bài 1. Đơn thức"},
    {"file": "Bai_02_Da_thuc.md", "id": "Bai_02_Da_thuc", "title": "Bài 2. Đa thức"},
    {"file": "Bai_03_Phep_cong_va_phep_tru_da_thuc.md", "id": "Bai_03_Phep_cong_va_phep_tru_da_thuc", "title": "Bài 3. Phép cộng và trừ đa thức"},
    {"file": "Luyen_tap_chung_trang_17.md", "id": "Luyen_tap_chung_trang_17", "title": "Luyện tập chung (Trang 17)"},
    {"file": "Bai_04_Phep_nhan_da_thuc.md", "id": "Bai_04_Phep_nhan_da_thuc", "title": "Bài 4. Phép nhân đa thức"},
    {"file": "Bai_05_Phep_chia_da_thuc_cho_don_thuc.md", "id": "Bai_05_Phep_chia_da_thuc_cho_don_thuc", "title": "Bài 5. Phép chia đa thức cho đơn thức"},
    {"file": "Luyen_tap_chung_trang_25.md", "id": "Luyen_tap_chung_trang_25", "title": "Luyện tập chung (Trang 25)"},
    {"file": "Bai_tap_cuoi_chuong_I.md", "id": "Bai_tap_cuoi_chuong_I", "title": "Bài tập cuối chương I"},
]

@st.cache_data
def load_sgk_solutions():
    path = os.path.join(BASE_DIR, "data", "sgk_solutions.json")
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

@st.cache_data
def load_extra_exercises():
    path = os.path.join(BASE_DIR, "data", "extra_exercises.json")
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

@st.cache_data
def load_lesson_videos():
    path = os.path.join(BASE_DIR, "data", "lesson_videos.json")
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

SGK_SOLUTIONS = load_sgk_solutions()
EXTRA_EXERCISES = load_extra_exercises()
LESSON_VIDEOS = load_lesson_videos()

def load_markdown_content(file_name: str) -> str:
    """Đọc file markdown bài học và chuyển đổi đường dẫn ảnh sang Base64 để hiển thị trực tiếp"""
    file_path = os.path.join(CONTENT_DIR, file_name)
    if not os.path.exists(file_path):
        return f"⚠️ Không tìm thấy file nội dung: {file_name}"
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Tìm và thay thế đường dẫn ảnh sang Base64 data URI
    def replace_image_with_base64(match):
        alt_text = match.group(1)
        rel_path = match.group(2)
        
        # Chuẩn hóa đường dẫn ảnh
        norm_path = os.path.normpath(os.path.join(CONTENT_DIR, rel_path))
        if not os.path.exists(norm_path):
            # Thử tìm trong thư mục assets của app
            candidate = os.path.join(ASSETS_DIR, "images", "tap1", os.path.basename(rel_path))
            if os.path.exists(candidate):
                norm_path = candidate
                
        if os.path.exists(norm_path):
            ext = os.path.splitext(norm_path)[1].lower().replace(".", "")
            mime = "image/png" if ext == "png" else "image/jpeg"
            try:
                with open(norm_path, "rb") as img_f:
                    b64_data = base64.b64encode(img_f.read()).decode("utf-8")
                return f'<div style="text-align: center; margin: 1.2rem 0;"><img src="data:{mime};base64,{b64_data}" alt="{alt_text}" style="max-width: 90%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"><br><em style="font-size: 0.9rem; color: #64748b;">{alt_text}</em></div>'
            except Exception:
                return f"*(Không tải được hình: {alt_text})*"
        return match.group(0)

    # Thay thế thẻ ảnh markdown ![alt](path)
    content = re.sub(r'!\[(.*?)\]\((.*?)\)', replace_image_with_base64, content)
    
    # Định dạng các blockquote đặc biệt: > [!NOTE] và > [!TIP]
    content = re.sub(r'> \[!NOTE\]\s*\n((?:> .*\n?)*)', r'<div class="callout-note"><strong>📌 Kiến thức trọng tâm:</strong>\n\1</div>\n', content)
    content = re.sub(r'> \[!TIP\]\s*\n((?:> .*\n?)*)', r'<div class="callout-tip"><strong>💡 Lưu ý quan trọng:</strong>\n\1</div>\n', content)
    
    # Gỡ bỏ các ký tự `>` thừa bên trong thẻ div vừa tạo
    content = re.sub(r'<div class="(?:callout-note|callout-tip)">([\s\S]*?)</div>', 
                     lambda m: '<div class="' + ('callout-note' if 'callout-note' in m.group(0) else 'callout-tip') + '">' + m.group(1).replace('> ', '').replace('>', '') + '</div>', 
                     content)

    return content

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("### 📐 TOÁN 8 TỰ HỌC")
    st.caption("Bộ sách *Kết nối tri thức với cuộc sống*")
    
    # Thống kê học tập
    stats = db.get_student_stats(len(LESSONS))
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="🔥 Chuỗi học", value=f"{stats['streak']} ngày")
    with col2:
        st.metric(label="⭐ Điểm tích luỹ", value=f"{int(stats['total_points'])}")
        
    st.markdown(f"**Tiến độ Chương I: {stats['completed_count']}/{len(LESSONS)} bài** ({stats['completion_rate']}%)")
    st.progress(stats['completion_rate'] / 100.0)
    
    st.markdown("---")
    st.markdown("#### 📚 Danh Sách Bài Học")
    
    # Lấy tiến độ các bài
    progress_map = db.get_all_progress()
    
    # Tạo nhãn bài học kèm trạng thái
    lesson_labels = []
    lesson_id_by_index = []
    
    for idx, les in enumerate(LESSONS):
        p = progress_map.get(les["id"], {})
        status = p.get("status", "not_started")
        if status == "completed":
            badge = "✅"
        elif status == "in_progress":
            badge = "🔵"
        else:
            badge = "⚪"
            
        label = f"{badge} {les['title']}"
        lesson_labels.append(label)
        lesson_id_by_index.append(les)

    # Chọn bài học
    selected_idx = st.radio(
        "Chọn bài học:",
        range(len(LESSONS)),
        format_func=lambda i: lesson_labels[i],
        label_visibility="collapsed"
    )
    current_lesson = LESSONS[selected_idx]
    
    st.markdown("---")
    st.markdown("#### 🤖 Cấu Hình Gia Sư AI")
    api_key_input = st.text_input(
        "GEMINI_API_KEY (Tuỳ chọn):",
        type="password",
        help="Nhập Gemini API Key để trò chuyện trực tiếp với Thầy Pi. Nếu chưa có, ứng dụng sẽ chạy ở Chế độ Offline Socratic."
    )
    
    if api_key_input:
        st.success("🟢 Gia sư AI Trực tuyến (Gemini)")
    else:
        st.info("🟡 Chế độ Offline Socratic (Sẵn sàng)")

# Đánh dấu bài học bắt đầu học
db.mark_lesson_in_progress(current_lesson["id"], current_lesson["title"])

# ================= KHU VỰC CHÍNH =================
st.markdown(f"""
<div class="app-header">
    <h1>Chương I: Đa Thức — {current_lesson['title']}</h1>
    <p>Học chủ động • Nắm vững bản chất • Tự chấm điểm tức thì</p>
</div>
""", unsafe_allow_html=True)

# 4 Tab chức năng
tab1, tab2, tab3, tab4 = st.tabs([
    "📖 Bài học & Lý thuyết",
    "✍️ Ví dụ & Phương pháp giải",
    "🎯 Luyện tập & Tự chấm điểm",
    "🤖 Gia sư AI Toán học"
])

# ================= TAB 1: BÀI HỌC & LÝ THUYẾT =================
with tab1:
    content_md = load_markdown_content(current_lesson["file"])
    st.markdown(content_md, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 🎥 Mục mở rộng: Video Thầy/Cô giảng chi tiết
    lesson_vid = LESSON_VIDEOS.get(current_lesson["file"])
    if lesson_vid:
        with st.expander("🎥 Chưa hiểu bài? Bấm xem Video Thầy/Cô giảng chi tiết", expanded=False):
            st.markdown(f"#### 🎬 {lesson_vid['video_title']}")
            st.markdown(f"👨‍🏫 **Giáo viên / Kênh phát hành:** `{lesson_vid['teacher_channel']}`")
            if "description" in lesson_vid:
                st.info(f"📌 **Nội dung trọng tâm video:** {lesson_vid['description']}")
                
            # Nhúng trực tiếp video YouTube để học sinh xem ngay trong app
            st.video(lesson_vid["youtube_url"])
            
            # Nút phụ mở xem trên YouTube ở tab mới
            col_v1, col_v2 = st.columns([2, 3])
            with col_v1:
                st.link_button("🌐 Mở xem trên YouTube", lesson_vid["youtube_url"], use_container_width=True)
            with col_v2:
                st.caption("*(Nhấn để mở xem trực tiếp trên ứng dụng YouTube hoặc phóng to toàn màn hình)*")
                
        st.markdown("---")
        
    st.info("💡 **Bước tiếp theo:** Hãy chuyển sang tab **'✍️ Ví dụ & Phương pháp giải'** để nắm cách tư duy từng bước, sau đó thử sức ở tab **'🎯 Luyện tập'** nhé!")

# ================= TAB 2: VÍ DỤ & PHƯƠNG PHÁP GIẢI =================
with tab2:
    st.markdown("### 💡 Hệ Thống Ví Dụ Trọng Tâm & Bí Quyết Giải")
    examples = LESSON_EXAMPLES.get(current_lesson["file"], [])
    
    if examples:
        for idx, ex in enumerate(examples, 1):
            with st.expander(f"📌 {ex['title']}", expanded=(idx == 1)):
                st.markdown(f"**Đề bài:**")
                st.markdown(ex["problem"])
                
                st.markdown(f"**🔍 Phương pháp tư duy:**")
                st.info(ex["method"])
                
                st.markdown(f"**📝 Lời giải chi tiết từng bước:**")
                for step in ex["solution"]:
                    st.markdown(step)
                    
                if "note" in ex:
                    st.warning(f"**🔑 Ghi nhớ then chốt:** {ex['note']}")
    else:
        st.info("Ví dụ mẫu của bài học đang được tổng hợp và hiển thị trực tiếp trong Tab 1 (Lý thuyết).")

# ================= TAB 3: LUYỆN TẬP & TỰ CHẤM ĐIỂM =================
with tab3:
    st.markdown("### 🎯 Hệ Thống Luyện Tập & Đấu Trường Toán Học")
    st.caption("Chọn chế độ học tập phù hợp để củng cố kỹ năng hoặc thử thách bản thân với kho câu hỏi phong phú!")
    
    exercise_mode = st.radio(
        "Chế độ luyện tập:",
        ["📚 Bài tập SGK & Hướng dẫn giải", "🎯 Đấu trường luyện tập mở rộng (Ngẫu nhiên 5 câu)"],
        horizontal=True,
        key=f"ex_mode_{current_lesson['id']}"
    )
    st.markdown("---")
    
    # ---------------- CHẾ ĐỘ 1: BÀI TẬP SGK ----------------
    if exercise_mode == "📚 Bài tập SGK & Hướng dẫn giải":
        st.markdown("#### 📚 Toàn Bộ Bài Tập SGK Kết Nối Tri Thức")
        st.info("💡 **Lời khuyên từ Thầy Pi:** Hãy tự giải bài tập vào vở hoặc khung nháp trước, sau đó bấm mở **'💡 Xem hướng dẫn giải chi tiết'** để so sánh từng bước và kiểm tra kết luận nhé!")
        
        lesson_sgk = SGK_SOLUTIONS.get(current_lesson["file"], [])
        if lesson_sgk:
            st.caption(f"Bài học này có **{len(lesson_sgk)} bài tập SGK** chuẩn mực kèm hướng dẫn giải 4 bước.")
            for idx, ex in enumerate(lesson_sgk, 1):
                with st.container():
                    st.markdown(f"#### 📝 {ex['title']}")
                    st.markdown(f"**Đề bài:**\n\n{ex['problem']}")
                    
                    # Khung nháp tự làm
                    st.text_area(
                        "✍️ Góc nháp / Ghi chú lời giải của em:",
                        placeholder="Em hãy viết các bước nháp, công thức biến đổi hoặc đáp số tại đây...",
                        key=f"sgk_draft_{current_lesson['id']}_{ex['id']}",
                        height=90
                    )
                    
                    # Expander xem hướng dẫn giải chi tiết
                    with st.expander("💡 Xem hướng dẫn giải chi tiết (Từng bước)", expanded=False):
                        st.markdown("**🔍 Phương pháp tư duy:**")
                        st.info(ex["method"])
                        
                        st.markdown("**📝 Các bước giải chi tiết:**")
                        for step in ex["steps"]:
                            st.markdown(step)
                            
                        st.success(f"**🎯 Kết luận:** {ex['conclusion']}")
                    
                    st.markdown("<hr style='margin: 1.5rem 0; border: none; border-top: 1px dashed #cbd5e1;'>", unsafe_allow_html=True)
        else:
            st.info("Hệ thống bài tập SGK của bài học này đang được chuẩn bị.")
            
    # ---------------- CHẾ ĐỘ 2: ĐẤU TRƯỜNG LUYỆN TẬP MỞ RỘNG ----------------
    else:
        st.markdown("#### 🎯 Đấu Trường Trắc Nghiệm Mở Rộng (5 Câu Ngẫu Nhiên)")
        st.caption("Mỗi lượt làm bài rút ngẫu nhiên 5 câu từ ngân hàng (2 Dễ • 2 Vừa • 1 Thử thách) kèm đồng hồ tính giờ.")
        
        bank = EXTRA_EXERCISES.get(current_lesson["file"], [])
        if not bank:
            bank = LESSON_QUIZZES.get(current_lesson["file"], [])
            
        if bank:
            quiz_set_key = f"quiz_set_{current_lesson['id']}"
            quiz_time_key = f"quiz_time_{current_lesson['id']}"
            quiz_submitted_key = f"quiz_submitted_{current_lesson['id']}"
            
            # Khởi tạo bộ 5 câu hỏi ngẫu nhiên nếu chưa có
            if quiz_set_key not in st.session_state:
                de_list = [q for q in bank if q.get("level") == "Dễ"]
                vua_list = [q for q in bank if q.get("level") == "Vừa"]
                kho_list = [q for q in bank if q.get("level") == "Thử thách"]
                
                if len(de_list) >= 2 and len(vua_list) >= 2 and len(kho_list) >= 1:
                    st.session_state[quiz_set_key] = random.sample(de_list, 2) + random.sample(vua_list, 2) + random.sample(kho_list, 1)
                else:
                    st.session_state[quiz_set_key] = random.sample(bank, min(5, len(bank)))
                st.session_state[quiz_time_key] = time.time()
                st.session_state[quiz_submitted_key] = None

            current_questions = st.session_state[quiz_set_key]
            
            # Thanh điều khiển: Thông tin thời gian & Nút tạo đề mới
            col_info, col_btn = st.columns([3, 1])
            with col_info:
                sub_data = st.session_state.get(quiz_submitted_key)
                if sub_data:
                    dur = sub_data["duration_sec"]
                    st.markdown(f"⏱️ **Thời gian làm bài:** `{dur//60:02d}:{dur%60:02d}` (Đã nộp bài) | 📊 **Cấu trúc:** 2 Dễ • 2 Vừa • 1 Thử thách")
                else:
                    elapsed = int(time.time() - st.session_state[quiz_time_key])
                    st.markdown(f"⏱️ **Đang làm bài:** `{elapsed//60:02d}:{elapsed%60:02d}` | 📊 **Cấu trúc đề:** 5 câu (2 Dễ • 2 Vừa • 1 Thử thách)")
            with col_btn:
                if st.button("🔄 Tạo đề mới", key=f"btn_refresh_{current_lesson['id']}", use_container_width=True):
                    de_list = [q for q in bank if q.get("level") == "Dễ"]
                    vua_list = [q for q in bank if q.get("level") == "Vừa"]
                    kho_list = [q for q in bank if q.get("level") == "Thử thách"]
                    if len(de_list) >= 2 and len(vua_list) >= 2 and len(kho_list) >= 1:
                        st.session_state[quiz_set_key] = random.sample(de_list, 2) + random.sample(vua_list, 2) + random.sample(kho_list, 1)
                    else:
                        st.session_state[quiz_set_key] = random.sample(bank, min(5, len(bank)))
                    st.session_state[quiz_time_key] = time.time()
                    st.session_state[quiz_submitted_key] = None
                    st.rerun()

            st.markdown("<br>", unsafe_allow_html=True)
            
            # Form làm bài
            with st.form(key=f"extra_quiz_form_{current_lesson['id']}"):
                user_choices = {}
                for i, q in enumerate(current_questions, 1):
                    lvl = q.get("level", "Vừa")
                    if lvl == "Dễ":
                        badge_html = "<span class='badge-easy'>🟢 Dễ</span>"
                    elif lvl == "Vừa":
                        badge_html = "<span class='badge-medium'>🟡 Vừa</span>"
                    else:
                        badge_html = "<span class='badge-hard'>🔴 Thử thách</span>"
                        
                    st.markdown(f"**Câu {i}:** {badge_html}", unsafe_allow_html=True)
                    st.markdown(q["question"])
                    
                    choice = st.radio(
                        f"Lựa chọn câu {i}:",
                        range(len(q["options"])),
                        format_func=lambda opt_i, opts=q["options"]: opts[opt_i],
                        key=f"rad_{current_lesson['id']}_{q['id']}",
                        label_visibility="collapsed"
                    )
                    user_choices[q["id"]] = choice
                    st.markdown("<hr style='margin: 0.8rem 0; border: none; border-top: 1px dashed #cbd5e1;'>", unsafe_allow_html=True)
                    
                submitted = st.form_submit_button("🚀 Nộp bài & Chấm điểm ngay", use_container_width=True)
                
            if submitted:
                duration_sec = int(time.time() - st.session_state[quiz_time_key])
                correct_count = 0
                for q in current_questions:
                    if user_choices.get(q["id"]) == q["correct"]:
                        correct_count += 1
                        
                total_cnt = len(current_questions)
                score_10 = round((correct_count / total_cnt) * 10, 1)
                
                # Lưu vào Database SQLite
                db.save_quiz_result(current_lesson["id"], current_lesson["title"], score_10, total_cnt)
                
                # Cập nhật kết quả vào session
                st.session_state[quiz_submitted_key] = {
                    "score_10": score_10,
                    "correct_count": correct_count,
                    "total_count": total_cnt,
                    "duration_sec": duration_sec,
                    "choices": user_choices
                }
                st.rerun()
                
            # Hiển thị kết quả đã nộp
            sub_res = st.session_state.get(quiz_submitted_key)
            if sub_res:
                sc = sub_res["score_10"]
                cor = sub_res["correct_count"]
                tot = sub_res["total_count"]
                dur = sub_res["duration_sec"]
                dur_m = dur // 60
                dur_s = dur % 60
                user_ans = sub_res["choices"]
                
                st.markdown("---")
                if sc >= 7.0:
                    st.balloons()
                    st.success(f"🎉 **XUẤT SẮC!** Em đạt **{sc}/10 điểm** ({cor}/{tot} câu đúng) trong thời gian **{dur_m:02d} phút {dur_s:02d} giây**! Bài học đã được ghi nhận hoàn thành ✅.")
                else:
                    st.warning(f"💪 **CỐ GẮNG LÊN NHÉ!** Em đạt **{sc}/10 điểm** ({cor}/{tot} câu đúng) trong thời gian **{dur_m:02d} phút {dur_s:02d} giây**. Hãy đọc kỹ hướng dẫn bên dưới và bấm '🔄 Tạo đề mới' để thử sức lại!")

                st.markdown("#### 📖 Đáp Án & Hướng Dẫn Chi Tiết:")
                for i, q in enumerate(current_questions, 1):
                    chosen = user_ans.get(q["id"])
                    is_cor = (chosen == q["correct"])
                    icon = "✅" if is_cor else "❌"
                    lvl = q.get("level", "Vừa")
                    with st.expander(f"{icon} Câu {i} ({lvl}): {q['options'][q['correct']]}", expanded=not is_cor):
                        if not is_cor:
                            st.markdown(f"❌ **Em đã chọn:** {q['options'][chosen] if chosen is not None else 'Chưa chọn'}")
                        st.markdown(f"✅ **Đáp án đúng:** {q['options'][q['correct']]}")
                        st.markdown(f"**🔍 Lời giải thích chi tiết:**\n\n{q['explanation']}")
        else:
            st.info("Ngân hàng câu hỏi trắc nghiệm của bài học này đang được chuẩn bị.")

# ================= TAB 4: GIA SƯ AI TOÁN HỌC =================
with tab4:
    st.markdown("### 🤖 Gia Sư AI — Thầy Pi Thông Thái")
    st.caption("Ứng dụng phương pháp Socratic: Thầy Pi sẽ gợi mở từng bước để em tự tìm ra đáp số, không giải tuột bài!")
    
    # Khởi tạo lịch sử chat trong session_state
    session_chat_key = f"chat_history_{current_lesson['id']}"
    if session_chat_key not in st.session_state:
        st.session_state[session_chat_key] = [
            {
                "role": "assistant",
                "content": f"Chào em! Thầy là **Pi Thông Thái** đây. Em đang học bài **{current_lesson['title']}**. Có chỗ nào trong phần lý thuyết hay bài tập làm em băn khoăn không? Hãy nhắn cho thầy nhé!"
            }
        ]
        
    # Hiển thị lịch sử chat
    for msg in st.session_state[session_chat_key]:
        with st.chat_message(msg["role"], avatar="👨‍🏫" if msg["role"] == "assistant" else "🧑‍🎓"):
            st.markdown(msg["content"])
            
    # Các câu hỏi gợi ý nhanh
    col_a, col_b, col_c = st.columns(3)
    quick_prompt = None
    with col_a:
        if st.button("💡 Gợi ý cách làm bài tập", key=f"btn_hint_{current_lesson['id']}"):
            quick_prompt = "Thầy ơi gợi ý cho em phương pháp giải bài tập trong bài này với ạ!"
    with col_b:
        if st.button("❓ Khái niệm khó hiểu nhất?", key=f"btn_concept_{current_lesson['id']}"):
            quick_prompt = "Khái niệm cốt lõi quan trọng nhất trong bài học này là gì hả Thầy?"
    with col_c:
        if st.button("🔍 Dấu hiệu nhận biết", key=f"btn_check_{current_lesson['id']}"):
            quick_prompt = "Làm sao để không bị nhầm lẫn khi làm dạng toán này ạ?"

    # Nhận câu hỏi từ học sinh
    user_input = st.chat_input("Hỏi Thầy Pi về bài học...") or quick_prompt
    
    if user_input:
        # Thêm câu hỏi của user vào session
        st.session_state[session_chat_key].append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar="🧑‍🎓"):
            st.markdown(user_input)
            
        # Sinh phản hồi từ Thầy Pi
        with st.chat_message("assistant", avatar="👨‍🏫"):
            with st.spinner("Thầy Pi đang suy nghĩ câu hỏi gợi ý cho em..."):
                tutor_reply = ai_tutor.generate_tutor_response(
                    api_key=api_key_input,
                    lesson_title=current_lesson["title"],
                    lesson_summary=content_md[:600],
                    chat_history=st.session_state[session_chat_key],
                    user_message=user_input
                )
                st.markdown(tutor_reply)
                
        st.session_state[session_chat_key].append({"role": "assistant", "content": tutor_reply})

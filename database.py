import sqlite3
import os
from datetime import datetime, date, timedelta

DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "math8_progress.db")

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Bảng tiến độ bài học
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_progress (
        lesson_id TEXT PRIMARY KEY,
        lesson_title TEXT,
        status TEXT DEFAULT 'not_started',
        score REAL DEFAULT 0.0,
        total_questions INTEGER DEFAULT 0,
        completed_at TEXT,
        last_studied_at TEXT
    )
    """)
    
    # Bảng thống kê học tập của học sinh
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_stats (
        id INTEGER PRIMARY KEY,
        current_streak INTEGER DEFAULT 0,
        last_active_date TEXT,
        total_points REAL DEFAULT 0.0
    )
    """)
    
    # Bảng lịch sử làm bài tập
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lesson_id TEXT,
        score REAL,
        total_questions INTEGER,
        attempted_at TEXT
    )
    """)
    
    # Khởi tạo record user_stats nếu chưa có
    cursor.execute("SELECT COUNT(*) FROM user_stats WHERE id = 1")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
        INSERT INTO user_stats (id, current_streak, last_active_date, total_points)
        VALUES (1, 0, NULL, 0.0)
        """)
        
    conn.commit()
    conn.close()

def update_streak():
    """Cập nhật chuỗi ngày học liên tục (streak)"""
    conn = get_connection()
    cursor = conn.cursor()
    
    today_str = date.today().isoformat()
    yesterday_str = (date.today() - timedelta(days=1)).isoformat()
    
    cursor.execute("SELECT current_streak, last_active_date FROM user_stats WHERE id = 1")
    row = cursor.fetchone()
    
    if row:
        current_streak = row["current_streak"] or 0
        last_date = row["last_active_date"]
        
        if last_date == today_str:
            # Đã học hôm nay, không tăng thêm
            pass
        elif last_date == yesterday_str:
            # Học tiếp nối từ hôm qua
            current_streak += 1
            cursor.execute("""
            UPDATE user_stats SET current_streak = ?, last_active_date = ? WHERE id = 1
            """, (current_streak, today_str))
        else:
            # Bị gián đoạn hoặc ngày đầu tiên
            current_streak = 1
            cursor.execute("""
            UPDATE user_stats SET current_streak = ?, last_active_date = ? WHERE id = 1
            """, (current_streak, today_str))
            
    conn.commit()
    conn.close()

def mark_lesson_in_progress(lesson_id, lesson_title):
    """Đánh dấu học sinh bắt đầu học một bài"""
    init_db()
    update_streak()
    conn = get_connection()
    cursor = conn.cursor()
    
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("SELECT status FROM student_progress WHERE lesson_id = ?", (lesson_id,))
    row = cursor.fetchone()
    
    if not row:
        cursor.execute("""
        INSERT INTO student_progress (lesson_id, lesson_title, status, last_studied_at)
        VALUES (?, ?, 'in_progress', ?)
        """, (lesson_id, lesson_title, now_str))
    elif row["status"] != "completed":
        cursor.execute("""
        UPDATE student_progress SET status = 'in_progress', last_studied_at = ?
        WHERE lesson_id = ?
        """, (now_str, lesson_id))
    else:
        cursor.execute("""
        UPDATE student_progress SET last_studied_at = ? WHERE lesson_id = ?
        """, (now_str, lesson_id))
        
    conn.commit()
    conn.close()

def save_quiz_result(lesson_id, lesson_title, score, total_questions):
    """Lưu kết quả tự chấm điểm bài tập"""
    init_db()
    update_streak()
    conn = get_connection()
    cursor = conn.cursor()
    
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Đạt >= 70% là hoàn thành bài
    is_completed = (score / total_questions >= 0.7) if total_questions > 0 else False
    status = "completed" if is_completed else "in_progress"
    
    cursor.execute("""
    INSERT INTO quiz_history (lesson_id, score, total_questions, attempted_at)
    VALUES (?, ?, ?, ?)
    """, (lesson_id, score, total_questions, now_str))
    
    cursor.execute("SELECT score, status FROM student_progress WHERE lesson_id = ?", (lesson_id,))
    row = cursor.fetchone()
    
    if row:
        best_score = max(row["score"] or 0, score)
        final_status = "completed" if (row["status"] == "completed" or is_completed) else "in_progress"
        completed_at = now_str if (is_completed and row["status"] != "completed") else None
        
        cursor.execute("""
        UPDATE student_progress
        SET score = ?, total_questions = ?, status = ?,
            completed_at = COALESCE(completed_at, ?),
            last_studied_at = ?
        WHERE lesson_id = ?
        """, (best_score, total_questions, final_status, completed_at, now_str, lesson_id))
    else:
        completed_at = now_str if is_completed else None
        cursor.execute("""
        INSERT INTO student_progress (lesson_id, lesson_title, status, score, total_questions, completed_at, last_studied_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (lesson_id, lesson_title, status, score, total_questions, completed_at, now_str))
        
    # Cập nhật tổng điểm tích lũy
    cursor.execute("""
    UPDATE user_stats SET total_points = total_points + ? WHERE id = 1
    """, (score,))
    
    conn.commit()
    conn.close()

def get_all_progress():
    """Lấy toàn bộ danh sách tiến độ học"""
    init_db()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_progress")
    rows = cursor.fetchall()
    conn.close()
    return {r["lesson_id"]: dict(r) for r in rows}

def get_student_stats(total_available_lessons=8):
    """Lấy tổng hợp thống kê học tập"""
    init_db()
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT current_streak, total_points FROM user_stats WHERE id = 1")
    user_row = cursor.fetchone()
    
    cursor.execute("SELECT COUNT(*) FROM student_progress WHERE status = 'completed'")
    completed_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM student_progress WHERE status = 'in_progress'")
    in_progress_count = cursor.fetchone()[0]
    
    conn.close()
    
    streak = user_row["current_streak"] if user_row else 0
    total_points = user_row["total_points"] if user_row else 0.0
    completion_rate = (completed_count / total_available_lessons * 100) if total_available_lessons > 0 else 0
    
    return {
        "streak": streak,
        "total_points": total_points,
        "completed_count": completed_count,
        "in_progress_count": in_progress_count,
        "completion_rate": round(completion_rate, 1)
    }

# Khởi tạo db ngay khi import
init_db()

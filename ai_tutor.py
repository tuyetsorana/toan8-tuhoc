import os
from typing import List, Dict

SYSTEM_PROMPT = """Bạn là 'Thầy Pi Thông Thái' - Gia sư Toán học lớp 8 ân cần, thông minh và kiên nhẫn, đồng hành cùng các em học sinh học bộ sách 'Kết nối tri thức với cuộc sống'.

PHƯƠNG PHÁP SƯ PHẠM SOCRATIC (GỢI MỞ TƯ DUY):
1. Tuyệt đối KHÔNG giải tuột đáp số ngay lập tức cho học sinh.
2. Hãy đọc kỹ câu hỏi của học sinh và bài học hiện tại, sau đó:
   - Đặt 1-2 câu hỏi gợi mở ngắn gọn để học sinh tự nhớ lại định nghĩa, công thức hoặc quy tắc cốt lõi.
   - Hướng dẫn học sinh thực hiện bước đầu tiên (ví dụ: 'Trước hết em hãy thu gọn đơn thức này bằng cách nhân các hệ số với nhau...').
   - Khi học sinh trả lời đúng một bước, hãy khen ngợi và dẫn dắt sang bước tiếp theo.
3. Luôn trình bày công thức toán học bằng cú pháp KaTeX/LaTeX: kẹp giữa $...$ đối với công thức nội dòng hoặc $$...$$ đối với công thức khối.
4. Giọng điệu thân thiện, hóm hỉnh, ấm áp như anh Pi, khuyến khích học sinh không sợ sai lầm.
"""

def generate_tutor_response(
    api_key: str,
    lesson_title: str,
    lesson_summary: str,
    chat_history: List[Dict[str, str]],
    user_message: str
) -> str:
    """
    Gửi câu hỏi tới Gemini qua google-genai SDK hoặc chuyển sang chế độ Offline thông minh.
    """
    api_key = (api_key or "").strip()
    
    if api_key:
        try:
            from google import genai
            from google.genai import types
            
            client = genai.Client(api_key=api_key)
            
            # Xây dựng prompt có ngữ cảnh bài học
            prompt_context = f"=== BÀI HỌC HIỆN TẠI: {lesson_title} ===\n"
            if lesson_summary:
                prompt_context += f"Tóm tắt kiến thức cốt lõi:\n{lesson_summary[:1000]}\n\n"
            
            prompt_context += "Lịch sử hội thoại gần đây:\n"
            for msg in chat_history[-4:]:
                role = "Học sinh" if msg["role"] == "user" else "Thầy Pi"
                prompt_context += f"{role}: {msg['content']}\n"
            
            prompt_context += f"\nHọc sinh hỏi: {user_message}\n\nHãy trả lời bằng phương pháp Socratic dẫn dắt từng bước:"
            
            # Thử các model theo thứ tự ưu tiên
            models_to_try = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
            last_err = None
            
            for m in models_to_try:
                try:
                    response = client.models.generate_content(
                        model=m,
                        contents=prompt_context,
                        config=types.GenerateContentConfig(
                            system_instruction=SYSTEM_PROMPT,
                            temperature=0.7,
                        )
                    )
                    if response and response.text:
                        return response.text
                except Exception as ex:
                    last_err = ex
                    continue
                    
            if last_err:
                return f"⚠️ *Không thể kết nối Gemini API ({str(last_err)}). Đang chuyển sang phản hồi gợi ý offline bên dưới:*\n\n" + get_offline_response(lesson_title, user_message)
        except Exception as e:
            return f"⚠️ *Lỗi khởi tạo API ({str(e)}). Đang chuyển sang chế độ Offline:*\n\n" + get_offline_response(lesson_title, user_message)
            
    # Chế độ Offline thông minh
    return get_offline_response(lesson_title, user_message)


def get_offline_response(lesson_title: str, user_message: str) -> str:
    """
    Gia sư offline phân tích từ khóa và bài học hiện tại để đưa ra gợi mở Socratic chuẩn mực.
    """
    msg_lower = user_message.lower()
    
    # Gợi ý chung khi chưa nhập key
    key_tip = "\n\n💡 *(Mẹo: Nhập `GEMINI_API_KEY` ở thanh bên trái để trò chuyện trực tiếp và tự do với Thầy Pi AI siêu thông minh nhé!)*"
    
    # Phân tích theo chủ đề
    if any(k in msg_lower for k in ["bậc", "bac"]):
        return (
            f"Chào em! Để tìm **bậc** trong bài *{lesson_title}*, Thầy Pi có 2 câu hỏi nhỏ cho em nè:\n\n"
            "1. Biểu thức của em đã là **dạng thu gọn** chưa? (Nếu chưa, mình cần thu gọn trước nhé).\n"
            "2. Trong đơn thức thu gọn, em hãy cộng tất cả các **số mũ của từng biến** lại. Em có tìm được tổng số mũ đó là bao nhiêu không?\n\n"
            "👉 Hãy thử viết ra số mũ của từng biến và cộng lại xem sao nhé!"
        ) + key_tip
        
    if any(k in msg_lower for k in ["đồng dạng", "dong dang"]):
        return (
            "Thầy Pi gợi ý cho em về **hai đơn thức đồng dạng** nhé:\n\n"
            "Hãy đối chiếu 2 điều kiện sau:\n"
            "- Hệ số của chúng có khác $0$ không?\n"
            "- **Phần biến** của chúng có giống hệt nhau từng biến và từng số mũ không?\n\n"
            "🔍 Em hãy nhìn vào phần biến của các đơn thức em đang xét, xem chúng có điểm nào khác biệt chưa?"
        ) + key_tip

    if any(k in msg_lower for k in ["thu gọn", "thu gon"]):
        return (
            "Muốn **thu gọn** biểu thức toán học, thầy chỉ cho em 'bí kíp' 2 bước cực kỳ hiệu quả nè:\n\n"
            "1. **Nhóm phần số**: Nhân các hệ số với nhau (chú ý dấu âm/dương nhé).\n"
            "2. **Nhóm các biến giống nhau**: Áp dụng quy tắc nhân luỹ thừa cùng cơ số: $x^m \\cdot x^n = x^{m+n}$.\n\n"
            "👉 Em thử áp dụng bước 1 với bài toán của mình trước xem hệ số ra bao nhiêu nào?"
        ) + key_tip

    if any(k in msg_lower for k in ["cộng", "trừ", "cong", "tru"]):
        return (
            "Chào em! Đối với phép **cộng, trừ đa thức / đơn thức đồng dạng**:\n\n"
            "- Với đơn thức đồng dạng: Ta **cộng (hoặc trừ) các hệ số** với nhau và **giữ nguyên phần biến**.\n"
            "- Với đa thức: Bỏ dấu ngoặc (nhớ đổi dấu nếu trước ngoặc là dấu trừ! Sau đó nhóm các hạng tử đồng dạng lại).\n\n"
            "Em đang gặp vướng mắc ở bước bỏ dấu ngoặc hay bước tìm hạng tử đồng dạng vậy?"
        ) + key_tip

    if any(k in msg_lower for k in ["nhân", "nhan", "tích"]):
        return (
            "Để làm phép **nhân đa thức**, em hãy nhớ quy tắc phân phối:\n\n"
            "- Nhân đơn thức với đa thức: $A(B + C) = A \\cdot B + A \\cdot C$.\n"
            "- Nhân đa thức với đa thức: Lấy mỗi hạng tử của đa thức thứ nhất nhân lần lượt với từng hạng tử của đa thức thứ hai rồi cộng lại.\n\n"
            "Em hãy thử viết ra từng tích thành phần xem có bao nhiêu số hạng nhé!"
        ) + key_tip

    if any(k in msg_lower for k in ["chia"]):
        return (
            "Về phép **chia đơn thức / đa thức**:\n\n"
            "- Chia đơn thức cho đơn thức: Chia hệ số cho hệ số, chia luỹ thừa của từng biến: $x^m : x^n = x^{m-n}$ ($m \\ge n$).\n"
            "- Chia đa thức cho đơn thức: Chia **từng hạng tử** của đa thức cho đơn thức đó rồi cộng các kết quả lại.\n\n"
            "Em kiểm tra xem số mũ của biến ở số bị chia có lớn hơn hoặc bằng số chia không nhé?"
        ) + key_tip

    # Phản hồi mặc định Socratic thân thiện
    return (
        f"Chào bạn học trò chăm chỉ! Thầy Pi rất vui được hỗ trợ em trong bài học **{lesson_title}**.\n\n"
        "Để Thầy có thể hướng dẫn đúng trọng tâm nhất, em hãy cho Thầy biết:\n"
        "1. Em đang làm câu hỏi hay bài tập số mấy?\n"
        "2. Theo suy nghĩ ban đầu của em thì mình nên bắt đầu từ công thức hay định nghĩa nào đã học trong bài này?\n\n"
        "Hãy chia sẻ bước làm hiện tại của em nhé, Thầy sẽ đồng hành cùng em từng bước một!"
    ) + key_tip

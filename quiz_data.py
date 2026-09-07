"""
Dữ liệu ví dụ mẫu và bài tập luyện tập tương tác cho Chương I - Đa thức (Toán 8 KNTT)
"""

LESSON_EXAMPLES = {
    "Bai_01_Don_thuc.md": [
        {
            "title": "Ví dụ 1: Nhận biết đơn thức",
            "problem": "Tìm đơn thức trong các biểu thức sau: $-x6y;\\quad x + 2y;\\quad 0,3xyx^2;\\quad 5x\\sqrt{y}$.",
            "method": "Đơn thức là biểu thức đại số chỉ gồm một số hoặc một biến, hoặc có dạng tích của những số và biến. Nếu có phép cộng/trừ hoặc biến nằm dưới dấu căn thì không phải đơn thức.",
            "solution": [
                "Biểu thức $x + 2y$ có chứa phép cộng nên **không là đơn thức**.",
                "Biểu thức $5x\\sqrt{y}$ có chứa căn bậc hai của biến $y$ nên **không là đơn thức**.",
                "Hai biểu thức còn lại: $-x6y$ và $0,3xyx^2$ đều chỉ gồm phép nhân giữa các số và biến nên **đều là đơn thức**."
            ],
            "note": "Một luỹ thừa (như $x^2 = x \\cdot x$) cũng được coi là một tích!"
        },
        {
            "title": "Ví dụ 2: Thu gọn đơn thức và xác định bậc",
            "problem": "Xác định hệ số, phần biến và bậc của đơn thức: $0,5xy^2 \\cdot 4x^2$.",
            "method": "Muốn tìm bậc và hệ số của đơn thức chưa thu gọn, trước hết ta phải thu gọn bằng cách nhân các hệ số và cộng các số mũ của cùng một biến.",
            "solution": [
                "Bước 1: Thu gọn đơn thức:",
                "$$0,5xy^2 \\cdot 4x^2 = (0,5 \\cdot 4)(x \\cdot x^2)y^2 = 2x^3y^2$$",
                "Bước 2: Xác định các yếu tố:",
                "- **Hệ số**: $2$",
                "- **Phần biến**: $x^3y^2$",
                "- **Bậc**: Tổng số mũ của các biến là $3 + 2 = 5$."
            ],
            "note": "Số mũ của biến viết không có số mũ như $x$ thực chất là luỹ thừa bậc 1: $x = x^1$."
        },
        {
            "title": "Ví dụ 3: Cộng và trừ các đơn thức đồng dạng",
            "problem": "Cho ba đơn thức đồng dạng $A = 3xy^2$, $B = -5xy^2$ và $C = xy^2$. Tính $A + B$, $A - B$ và $A + B + C$.",
            "method": "Cộng (hoặc trừ) các hệ số với nhau và giữ nguyên phần biến.",
            "solution": [
                "$A + B = [3 + (-5)]xy^2 = -2xy^2$",
                "$A - B = [3 - (-5)]xy^2 = (3 + 5)xy^2 = 8xy^2$",
                "$A + B + C = (3 - 5 + 1)xy^2 = -1xy^2 = -xy^2$"
            ],
            "note": "Đơn thức $xy^2$ có hệ số ngầm hiểu là $+1$."
        }
    ],
    "Bai_02_Da_thuc.md": [
        {
            "title": "Ví dụ: Thu gọn đa thức và tìm bậc",
            "problem": "Thu gọn đa thức $M = x^2y - 5xy + 7xy^2 + 3x^2y + xy^2 - 4xy^2 + 2$ và tìm bậc của nó.",
            "method": "1. Nhóm các hạng tử đồng dạng lại với nhau.\n2. Cộng, trừ hệ số của các hạng tử đồng dạng.\n3. Bậc của đa thức là bậc của hạng tử có bậc cao nhất trong dạng thu gọn.",
            "solution": [
                "Nhóm các hạng tử đồng dạng:",
                "$$M = (x^2y + 3x^2y) + (7xy^2 + xy^2 - 4xy^2) - 5xy + 2$$",
                "Thu gọn từng nhóm:",
                "$$M = 4x^2y + 4xy^2 - 5xy + 2$$",
                "Xét bậc của các hạng tử trong dạng thu gọn:",
                "- $4x^2y$ có bậc là $2 + 1 = 3$",
                "- $4xy^2$ có bậc là $1 + 2 = 3$",
                "- $-5xy$ có bậc là $1 + 1 = 2$",
                "- $2$ có bậc là $0$",
                "Hạng tử có bậc cao nhất là 3. Vậy bậc của đa thức $M$ là **3**."
            ],
            "note": "Bắt buộc phải thu gọn đa thức trước khi kết luận về bậc của đa thức đó!"
        }
    ],
    "Bai_03_Phep_cong_va_phep_tru_da_thuc.md": [
        {
            "title": "Ví dụ: Cộng và trừ hai đa thức",
            "problem": "Cho $C = 5x^2y + 5x - 3z + 2$ và $D = xyz - 4x^2y + 5x - 1$. Tính $C + D$ và $C - D$.",
            "method": "Bỏ dấu ngoặc rồi nhóm các hạng tử đồng dạng. Chú ý: Khi trước ngoặc là dấu trừ, phải đổi dấu tất cả các hạng tử bên trong!",
            "solution": [
                "**Tính $C + D$:**",
                "$$C + D = (5x^2y + 5x - 3z + 2) + (xyz - 4x^2y + 5x - 1)$$",
                "$$= (5x^2y - 4x^2y) + (5x + 5x) - 3z + xyz + (2 - 1) = x^2y + 10x - 3z + xyz + 1$$",
                "**Tính $C - D$:**",
                "$$C - D = (5x^2y + 5x - 3z + 2) - (xyz - 4x^2y + 5x - 1)$$",
                "$$= 5x^2y + 5x - 3z + 2 - xyz + 4x^2y - 5x + 1$$",
                "$$= (5x^2y + 4x^2y) + (5x - 5x) - xyz - 3z + (2 + 1) = 9x^2y - xyz - 3z + 3$$"
            ],
            "note": "Kiểm tra kỹ việc đổi dấu của các số âm: $-(-4x^2y) = +4x^2y$ và $-(-1) = +1$."
        }
    ],
    "Luyen_tap_chung_trang_17.md": [
        {
            "title": "Ví dụ: Tìm đa thức thoả mãn đẳng thức",
            "problem": "Cho hai đa thức $A = 5x^2 - 2x^3y + 7x^3y^2 - 118$ và $B = -7x^3y^2 + x^3y - 5xy^2 - 4x^2 + y$. Tìm tổng $A + B$ và xác định bậc.",
            "method": "Cộng hai đa thức rồi thu gọn các đơn thức đồng dạng theo từng luỹ thừa.",
            "solution": [
                "$$A + B = (5x^2 - 4x^2) + (-2x^3y + x^3y) + (7x^3y^2 - 7x^3y^2) - 5xy^2 + y - 118$$",
                "$$= x^2 - x^3y - 5xy^2 + y - 118$$",
                "Hạng tử $-x^3y$ có bậc $3 + 1 = 4$ là cao nhất. Vậy bậc của $A + B$ là 4."
            ],
            "note": "Các hạng tử đối nhau như $7x^3y^2 - 7x^3y^2 = 0$ sẽ triệt tiêu."
        }
    ],
    "Bai_04_Phep_nhan_da_thuc.md": [
        {
            "title": "Ví dụ 1: Nhân đơn thức với đa thức",
            "problem": "Thực hiện phép nhân: $(-4xy) \\cdot (2x^2 + xy - y^2)$.",
            "method": "Áp dụng quy tắc $A(B + C - D) = A \\cdot B + A \\cdot C - A \\cdot D$.",
            "solution": [
                "$$(-4xy) \\cdot (2x^2 + xy - y^2) = (-4xy)(2x^2) + (-4xy)(xy) + (-4xy)(-y^2)$$",
                "$$= -8x^3y - 4x^2y^2 + 4xy^3$$"
            ],
            "note": "Cẩn thận quy tắc nhân dấu: $(-4xy) \\cdot (-y^2) = +4xy^3$."
        },
        {
            "title": "Ví dụ 2: Nhân đa thức với đa thức",
            "problem": "Rút gọn biểu thức: $(x + y)(2x - y) - (x - y)(2x + y)$.",
            "method": "Khai triển từng tích rồi trừ hai kết quả.",
            "solution": [
                "Tích 1: $(x + y)(2x - y) = 2x^2 - xy + 2xy - y^2 = 2x^2 + xy - y^2$",
                "Tích 2: $(x - y)(2x + y) = 2x^2 + xy - 2xy - y^2 = 2x^2 - xy - y^2$",
                "Trừ hai kết quả:",
                "$$(2x^2 + xy - y^2) - (2x^2 - xy - y^2) = 2x^2 + xy - y^2 - 2x^2 + xy + y^2 = 2xy$$"
            ],
            "note": "Kết quả cuối cùng rất gọn gàng: $2xy$."
        }
    ],
    "Bai_05_Phep_chia_da_thuc_cho_don_thuc.md": [
        {
            "title": "Ví dụ: Chia đa thức cho đơn thức",
            "problem": "Thực hiện phép chia: $(15x^2y^4 - 4x^3y^3 + 20x^2y) : 5x^2y$.",
            "method": "Lấy từng hạng tử của đa thức chia cho đơn thức $5x^2y$, sau đó cộng các thương lại.",
            "solution": [
                "$$(15x^2y^4 : 5x^2y) + (-4x^3y^3 : 5x^2y) + (20x^2y : 5x^2y)$$",
                "- $15x^2y^4 : 5x^2y = 3y^3$",
                "- $-4x^3y^3 : 5x^2y = -\\frac{4}{5}xy^2$",
                "- $20x^2y : 5x^2y = 4$",
                "Kết quả: $3y^3 - \\frac{4}{5}xy^2 + 4$."
            ],
            "note": "$x^2 : x^2 = 1$ và $y : y = 1$."
        }
    ],
    "Luyen_tap_chung_trang_25.md": [
        {
            "title": "Ví dụ: Điều kiện chia hết chứa tham số m",
            "problem": "Cho đa thức $A = 2x^2y^2 - 5xy^3$ và đơn thức $B = 3x^my^2$ ($m \\in \\mathbb{N}$). Tìm số nguyên dương $m$ để $A$ chia hết cho $B$.",
            "method": "Để đa thức chia hết cho đơn thức thì mọi hạng tử của $A$ phải chia hết cho $B$. Do đó số mũ của biến $x$ trong $B$ phải $\\le$ số mũ của $x$ trong mỗi hạng tử của $A$.",
            "solution": [
                "Trong $A$, số mũ của $x$ ở hai hạng tử lần lượt là $2$ và $1$.",
                "Để $A$ chia hết cho $B$, ta phải có đồng thời: $m \\le 2$ và $m \\le 1 \\Rightarrow m \\le 1$.",
                "Vì $m$ là số nguyên dương ($m \\in \\mathbb{N}^*$) nên duy nhất $m = 1$."
            ],
            "note": "Khi $m = 1$, phép chia trở thành: $(2x^2y^2 - 5xy^3) : 3xy^2 = \\frac{2}{3}x - \\frac{5}{3}y$."
        }
    ],
    "Bai_tap_cuoi_chuong_I.md": [
        {
            "title": "Ví dụ trọng tâm: Chia đa thức đặt ẩn phụ",
            "problem": "Thực hiện phép chia: $[8x^3(2x - 5)^2 - 6x^2(2x - 5)^3 + 10x(2x - 5)^2] : 2x(2x - 5)^2$.",
            "method": "Đặt ẩn phụ $y = 2x - 5$ để biến bài toán phức tạp về dạng chia đa thức cho đơn thức cơ bản.",
            "solution": [
                "Đặt $y = 2x - 5$, biểu thức trở thành:",
                "$$[8x^3y^2 - 6x^2y^3 + 10xy^2] : 2xy^2$$",
                "Thực hiện chia từng hạng tử:",
                "- $8x^3y^2 : 2xy^2 = 4x^2$",
                "- $-6x^2y^3 : 2xy^2 = -3xy$",
                "- $10xy^2 : 2xy^2 = 5$",
                "Thay lại $y = 2x - 5$:",
                "$$= 4x^2 - 3x(2x - 5) + 5 = 4x^2 - 6x^2 + 15x + 5 = -2x^2 + 15x + 5$$"
            ],
            "note": "Đặt ẩn phụ là phương pháp cực mạnh giúp học sinh tránh nhầm lẫn khi làm việc với biểu thức cồng kềnh!"
        }
    ]
}

LESSON_QUIZZES = {
    "Bai_01_Don_thuc.md": [
        {
            "id": "q1",
            "question": "Biểu thức nào sau đây là một đơn thức?",
            "options": [
                "A. $x + 2y$",
                "B. $5x\\sqrt{y}$",
                "C. $-\\frac{5}{9}xyz$",
                "D. $\\frac{3}{x} + y^2$"
            ],
            "correct": 2,
            "explanation": "Đơn thức là biểu thức chỉ gồm một số, một biến hoặc tích các số và biến. $-\\frac{5}{9}xyz$ là đơn thức vì chỉ gồm phép nhân. $x+2y$ và $\\frac{3}{x}+y^2$ có phép cộng, $5x\\sqrt{y}$ chứa căn biến."
        },
        {
            "id": "q2",
            "question": "Thu gọn đơn thức $A = 4x(-2)x^2y$. Bậc của đơn thức nhận được là bao nhiêu?",
            "options": [
                "A. Bậc 3",
                "B. Bậc 4",
                "C. Bậc 2",
                "D. Bậc 5"
            ],
            "correct": 1,
            "explanation": "Thu gọn: $A = 4 \\cdot (-2) \\cdot (x \\cdot x^2) \\cdot y = -8x^3y$. Số mũ của $x$ là 3, số mũ của $y$ là 1. Bậc $= 3 + 1 = 4$."
        },
        {
            "id": "q3",
            "question": "Cặp đơn thức nào sau đây là hai đơn thức đồng dạng?",
            "options": [
                "A. $2x^2y$ và $2xy^2$",
                "B. $3x^3y^2$ và $7x^3y^2$",
                "C. $-0,2x^2y^3$ và $0,2x^3y^2$",
                "D. $4x$ và $4y$"
            ],
            "correct": 1,
            "explanation": "Hai đơn thức đồng dạng phải có hệ số khác 0 và có phần biến giống nhau hoàn toàn. $3x^3y^2$ và $7x^3y^2$ cùng có phần biến là $x^3y^2$."
        },
        {
            "id": "q4",
            "question": "Rút gọn rồi tính giá trị biểu thức $S = \\frac{1}{2}x^2y^5 - \\frac{5}{2}x^2y^5$ khi $x = -2$ và $y = 1$:",
            "options": [
                "A. $8$",
                "B. $-8$",
                "C. $-4$",
                "D. $4$"
            ],
            "correct": 1,
            "explanation": "$S = \\left(\\frac{1}{2} - \\frac{5}{2}\\right)x^2y^5 = -2x^2y^5$. Với $x = -2, y = 1 \\Rightarrow S = -2 \\cdot (-2)^2 \\cdot 1^5 = -2 \\cdot 4 \\cdot 1 = -8$."
        }
    ],
    "Bai_02_Da_thuc.md": [
        {
            "id": "q1",
            "question": "Trong các biểu thức sau, biểu thức nào KHÔNG phải là đa thức?",
            "options": [
                "A. $-x^2 + 3x + 1$",
                "B. $x - \\frac{\\sqrt{5}}{x}$",
                "C. $2024$",
                "D. $3x^2y - 5xy + 2,4$"
            ],
            "correct": 1,
            "explanation": "Biểu thức $x - \\frac{\\sqrt{5}}{x}$ có biến $x$ ở mẫu số (phép chia cho biến) nên không phải là đa thức."
        },
        {
            "id": "q2",
            "question": "Bậc của đa thức $Q = x^4 - 3x^2y^2 + 3xy^2 - x^4 + 1$ là:",
            "options": [
                "A. 4",
                "B. 3",
                "C. 2",
                "D. 1"
            ],
            "correct": 0,
            "explanation": "Thu gọn: $Q = (x^4 - x^4) - 3x^2y^2 + 3xy^2 + 1 = -3x^2y^2 + 3xy^2 + 1$. Hạng tử $-3x^2y^2$ có bậc là $2 + 2 = 4$."
        },
        {
            "id": "q3",
            "question": "Thu gọn đa thức $M = 0,6x^3 + x^2z - 2,7xy^2 + 0,4x^3 + 1,7xy^2$, ta được:",
            "options": [
                "A. $x^3 + x^2z - xy^2$",
                "B. $x^3 + x^2z - 4,4xy^2$",
                "C. $0,2x^3 + x^2z - xy^2$",
                "D. $x^3 + x^2z + xy^2$"
            ],
            "correct": 0,
            "explanation": "$M = (0,6x^3 + 0,4x^3) + x^2z + (-2,7xy^2 + 1,7xy^2) = x^3 + x^2z - xy^2$."
        }
    ],
    "Bai_03_Phep_cong_va_phep_tru_da_thuc.md": [
        {
            "id": "q1",
            "question": "Cho $P = x^2y + x^3 - xy^2 + 3$ và $Q = x^3 + xy^2 - xy - 6$. Tổng $P + Q$ bằng:",
            "options": [
                "A. $2x^3 + x^2y - xy - 3$",
                "B. $2x^3 + x^2y - 2xy^2 - xy - 3$",
                "C. $x^2y - xy + 9$",
                "D. $2x^3 - xy - 3$"
            ],
            "correct": 0,
            "explanation": "$P + Q = (x^3 + x^3) + x^2y + (-xy^2 + xy^2) - xy + (3 - 6) = 2x^3 + x^2y - xy - 3$."
        },
        {
            "id": "q2",
            "question": "Rút gọn biểu thức $(x - y) + (y - z) + (z - x)$ được kết quả là:",
            "options": [
                "A. $2x + 2y + 2z$",
                "B. $0$",
                "C. $x + y + z$",
                "D. $-2x$"
            ],
            "correct": 1,
            "explanation": "$(x - y) + (y - z) + (z - x) = (x - x) + (-y + y) + (-z + z) = 0$."
        },
        {
            "id": "q3",
            "question": "Tìm đa thức $M$ biết $M - 5x^2 = 2x^2 + 3$:",
            "options": [
                "A. $M = 7x^2 + 3$",
                "B. $M = -3x^2 + 3$",
                "C. $M = 3x^2 + 3$",
                "D. $M = 7x^2 - 3$"
            ],
            "correct": 0,
            "explanation": "Chuyển vế đổi dấu: $M = 2x^2 + 3 + 5x^2 = 7x^2 + 3$."
        }
    ],
    "Luyen_tap_chung_trang_17.md": [
        {
            "id": "q1",
            "question": "Bể bơi thứ nhất có thể tích $V_1 = 1,2xy$ ($m^3$). Bể thứ hai sâu $1,5m$, đáy gấp 5 lần hai kích thước đáy bể một ($V_2 = 1,5 \\cdot 5x \\cdot 5y = 37,5xy$). Tổng thể tích nước để bơm đầy cả 2 bể là:",
            "options": [
                "A. $38,7xy$ ($m^3$)",
                "B. $26,2xy$ ($m^3$)",
                "C. $39,7xy$ ($m^3$)",
                "D. $18,7xy$ ($m^3$)"
            ],
            "correct": 0,
            "explanation": "Tổng thể tích $V = 1,2xy + 37,5xy = (1,2 + 37,5)xy = 38,7xy$ ($m^3$)."
        },
        {
            "id": "q2",
            "question": "Cho $P = 5x^4 - 3x^3y + 2xy^3 - x^3y + 2y^4 - 7x^2y^2 - 2xy^3$. Bậc của đa thức $P$ là:",
            "options": [
                "A. 3",
                "B. 4",
                "C. 5",
                "D. 2"
            ],
            "correct": 1,
            "explanation": "$P = 5x^4 - 4x^3y - 7x^2y^2 + 2y^4$. Tất cả các hạng tử đều có bậc là 4. Vậy bậc của $P$ là 4."
        }
    ],
    "Bai_04_Phep_nhan_da_thuc.md": [
        {
            "id": "q1",
            "question": "Tích của đơn thức $\\frac{3}{4}xy$ và $8x^3y^2$ là:",
            "options": [
                "A. $6x^4y^3$",
                "B. $6x^3y^2$",
                "C. $\\frac{24}{4}x^3y^3$",
                "D. $8x^4y^3$"
            ],
            "correct": 0,
            "explanation": "$\\frac{3}{4} \\cdot 8 \\cdot (x \\cdot x^3)(y \\cdot y^2) = 6x^4y^3$."
        },
        {
            "id": "q2",
            "question": "Khai triển và rút gọn $(x - 5)(2x + 3) - 2x(x - 3) + x + 7$:",
            "options": [
                "A. $-8$",
                "B. $8$",
                "C. $2x - 8$",
                "D. $-2x + 8$"
            ],
            "correct": 0,
            "explanation": "$(2x^2 + 3x - 10x - 15) - (2x^2 - 6x) + x + 7 = 2x^2 - 7x - 15 - 2x^2 + 6x + x + 7 = -15 + 7 = -8$."
        },
        {
            "id": "q3",
            "question": "Rút gọn $x(x^2 - y) - x^2(x + y) + xy(x - 1)$ ta được:",
            "options": [
                "A. $-2xy$",
                "B. $0$",
                "C. $2x^3 - 2xy$",
                "D. $-x^2y$"
            ],
            "correct": 0,
            "explanation": "$= x^3 - xy - x^3 - x^2y + x^2y - xy = -2xy$."
        }
    ],
    "Bai_05_Phep_chia_da_thuc_cho_don_thuc.md": [
        {
            "id": "q1",
            "question": "Kết quả của phép chia $(-15x^2y^2) : (3x^2y)$ là:",
            "options": [
                "A. $-5y$",
                "B. $5y$",
                "C. $-5xy$",
                "D. $-5x$"
            ],
            "correct": 0,
            "explanation": "$-15 : 3 = -5$; $x^2 : x^2 = 1$; $y^2 : y = y$. Kết quả là $-5y$."
        },
        {
            "id": "q2",
            "question": "Phép chia đa thức $(6x^4y^3 - 8x^3y^4 + 3x^2y^2) : (2xy^2)$ cho thương là:",
            "options": [
                "A. $3x^3y - 4x^2y^2 + 1,5x$",
                "B. $3x^3y - 4x^2y^2 + 3x$",
                "C. $3x^3y - 8x^2y^2 + 1,5x$",
                "D. $6x^3y - 4x^2y^2 + 1,5x$"
            ],
            "correct": 0,
            "explanation": "$6:2=3, x^4:x=x^3, y^3:y^2=y \\Rightarrow 3x^3y$; $-8:2=-4, x^3:x=x^2, y^4:y^2=y^2 \\Rightarrow -4x^2y^2$; $3:2=1,5, x^2:x=x, y^2:y^2=1 \\Rightarrow 1,5x$."
        },
        {
            "id": "q3",
            "question": "Tìm đơn thức $M$ biết $\\frac{7}{3}x^3y^2 : M = 7xy^2$:",
            "options": [
                "A. $M = \\frac{1}{3}x^2$",
                "B. $M = 3x^2$",
                "C. $M = \\frac{1}{3}x^2y$",
                "D. $M = \\frac{7}{3}x$"
            ],
            "correct": 0,
            "explanation": "$M = \\left(\\frac{7}{3}x^3y^2\\right) : (7xy^2) = \\left(\\frac{7}{3} : 7\\right)(x^3 : x)(y^2 : y^2) = \\frac{1}{3}x^2$."
        }
    ],
    "Luyen_tap_chung_trang_25.md": [
        {
            "id": "q1",
            "question": "Cho $P = 5x(3x^2y - 2xy^2 + 1) - 3xy(5x^2 - 3xy) + x^2y^2$. Dạng thu gọn của $P$ là:",
            "options": [
                "A. $5x$",
                "B. $15x^3y + 5x$",
                "C. $x^2y^2 + 5x$",
                "D. $10x$"
            ],
            "correct": 0,
            "explanation": "$P = 15x^3y - 10x^2y^2 + 5x - 15x^3y + 9x^2y^2 + x^2y^2 = (15 - 15)x^3y + (-10 + 9 + 1)x^2y^2 + 5x = 5x$."
        },
        {
            "id": "q2",
            "question": "Tìm đơn thức $B$ nếu $4x^3y^2 : B = -2xy$:",
            "options": [
                "A. $B = -2x^2y$",
                "B. $B = 2x^2y$",
                "C. $B = -2xy^2$",
                "D. $B = -8x^4y^3$"
            ],
            "correct": 0,
            "explanation": "$B = 4x^3y^2 : (-2xy) = [4 : (-2)](x^3 : x)(y^2 : y) = -2x^2y$."
        }
    ],
    "Bai_tap_cuoi_chuong_I.md": [
        {
            "id": "q1",
            "question": "Câu 1.39: Đơn thức $-2^3x^2yz^3$ có:",
            "options": [
                "A. hệ số $-2$, bậc 8",
                "B. hệ số $-2^3$, bậc 5",
                "C. hệ số $-1$, bậc 9",
                "D. hệ số $-2^3$, bậc 6"
            ],
            "correct": 3,
            "explanation": "Hệ số là $-2^3 = -8$. Bậc là tổng số mũ của các biến $x, y, z$: $2 + 1 + 3 = 6$. Đáp án đúng là D."
        },
        {
            "id": "q2",
            "question": "Câu 1.41: Tích của hai đơn thức $6x^2yz$ và $-2y^2z^2$ là đơn thức:",
            "options": [
                "A. $4x^2y^3z^3$",
                "B. $-12x^2y^3z^3$",
                "C. $-12x^3y^3z^3$",
                "D. $4x^3y^3z^3$"
            ],
            "correct": 1,
            "explanation": "$6 \\cdot (-2) \\cdot x^2 \\cdot (y \\cdot y^2) \\cdot (z \\cdot z^2) = -12x^2y^3z^3$."
        },
        {
            "id": "q3",
            "question": "Câu 1.42: Khi chia đa thức $8x^3y^2 - 6x^2y^3$ cho đơn thức $-2xy$, kết quả là:",
            "options": [
                "A. $-4x^2y + 3xy^2$",
                "B. $-4xy^2 + 3x^2y$",
                "C. $-10x^2y + 4xy^2$",
                "D. $4x^2y - 3xy^2$"
            ],
            "correct": 0,
            "explanation": "$8x^3y^2 : (-2xy) = -4x^2y$ và $-6x^2y^3 : (-2xy) = +3xy^2$. Kết quả: $-4x^2y + 3xy^2$."
        },
        {
            "id": "q4",
            "question": "Câu 1.44: Rút gọn biểu thức $3x^3(x^5 - y^5) + y^5(3x^3 - y^3)$ được:",
            "options": [
                "A. $3x^8 - y^8$",
                "B. $3x^8 + 6x^3y^5 - y^8$",
                "C. $3x^8 + y^8$",
                "D. $3x^5 - y^5$"
            ],
            "correct": 0,
            "explanation": "$3x^8 - 3x^3y^5 + 3x^3y^5 - y^8 = 3x^8 - y^8$."
        }
    ]
}

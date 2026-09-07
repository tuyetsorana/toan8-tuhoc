import json
import os

sgk_solutions = {
    "Bai_01_Don_thuc.md": [
        {
            "id": "1.1",
            "title": "Bài 1.1 (Trang 9)",
            "problem": "Trong các biểu thức sau, biểu thức nào là đơn thức?\n$$-x;\\quad (1 + x)y^2;\\quad (3 + \\sqrt{3})xy;\\quad 0;\\quad \\frac{1}{y}x^2;\\quad 2\\sqrt{xy}.$$",
            "method": "Áp dụng định nghĩa: Đơn thức là biểu thức đại số chỉ gồm một số hoặc một biến, hoặc có dạng tích của những số và biến. Biểu thức có phép cộng/trừ với biến, biến ở mẫu số hoặc biến trong dấu căn thì không phải là đơn thức.",
            "steps": [
                "**Bước 1 (Xét từng biểu thức):**\n- $-x = (-1) \\cdot x$: Là tích của số và biến $\\Rightarrow$ Là đơn thức.\n- $(1 + x)y^2 = y^2 + xy^2$: Có chứa phép cộng của biến $x$ $\\Rightarrow$ Không là đơn thức.\n- $(3 + \\sqrt{3})xy$: $(3 + \\sqrt{3})$ là một hằng số thực, biểu thức là tích giữa số thực và hai biến $x, y$ $\\Rightarrow$ Là đơn thức.\n- $0$: Số 0 được coi là đơn thức (đặc biệt, không có bậc) $\\Rightarrow$ Là đơn thức.\n- $\\frac{1}{y}x^2$: Chứa biến $y$ ở mẫu số $\\Rightarrow$ Không là đơn thức.\n- $2\\sqrt{xy}$: Chứa các biến $x, y$ trong dấu căn bậc hai $\\Rightarrow$ Không là đơn thức."
            ],
            "conclusion": "Các biểu thức là đơn thức gồm: $-x;\\quad (3 + \\sqrt{3})xy;\\quad 0$."
        },
        {
            "id": "1.2",
            "title": "Bài 1.2 (Trang 9)",
            "problem": "Cho các đơn thức:\n$$A = 4x(-2)x^2y;\\quad B = 12,75xyz;\\quad C = (1 + 2 \\cdot 4,5)x^2y\\frac{1}{5}y^3;\\quad D = (2 - \\sqrt{5})x.$$\na) Liệt kê các đơn thức thu gọn trong các đơn thức đã cho và thu gọn các đơn thức còn lại.\nb) Với mỗi đơn thức nhận được, hãy cho biết hệ số, phần biến và bậc của nó.",
            "method": "- Đơn thức thu gọn chỉ gồm tích của một số với các biến, mỗi biến chỉ xuất hiện 1 lần dưới dạng luỹ thừa với số mũ nguyên dương.\n- Thu gọn bằng cách nhân hệ số với nhau, nhân các luỹ thừa cùng cơ số ($x^m \\cdot x^n = x^{m+n}$).\n- Bậc là tổng số mũ của tất cả các biến.",
            "steps": [
                "**Bước 1 (Câu a - Liệt kê & thu gọn):**\n- Các đơn thức đã thu gọn: $B = 12,75xyz$ và $D = (2 - \\sqrt{5})x$.\n- Thu gọn $A$: $A = [4 \\cdot (-2)] \\cdot (x \\cdot x^2) \\cdot y = -8x^3y$.\n- Thu gọn $C$: $C = (1 + 9) \\cdot \\frac{1}{5} \\cdot x^2 \\cdot (y \\cdot y^3) = 10 \\cdot \\frac{1}{5} \\cdot x^2y^4 = 2x^2y^4$.",
                "**Bước 2 (Câu b - Xác định hệ số, biến và bậc):**\n- Đơn thức $A = -8x^3y$: Hệ số là $-8$; phần biến là $x^3y$; bậc là $3 + 1 = 4$.\n- Đơn thức $B = 12,75xyz$: Hệ số là $12,75$; phần biến là $xyz$; bậc là $1 + 1 + 1 = 3$.\n- Đơn thức $C = 2x^2y^4$: Hệ số là $2$; phần biến là $x^2y^4$; bậc là $2 + 4 = 6$.\n- Đơn thức $D = (2 - \\sqrt{5})x$: Hệ số là $2 - \\sqrt{5}$; phần biến là $x$; bậc là $1$."
            ],
            "conclusion": "- Đơn thức thu gọn sẵn: $B, D$.\n- Dạng thu gọn: $A = -8x^3y$ (bậc 4); $B = 12,75xyz$ (bậc 3); $C = 2x^2y^4$ (bậc 6); $D = (2 - \\sqrt{5})x$ (bậc 1)."
        },
        {
            "id": "1.3",
            "title": "Bài 1.3 (Trang 10)",
            "problem": "Thu gọn rồi tính giá trị của mỗi đơn thức sau:\na) $A = (-2)x^2y\\frac{1}{2}xy$ khi $x = -2; y = \\frac{1}{2}$.\nb) $B = xyz(-0,5)y^2z$ khi $x = 4; y = 0,5; z = 2$.",
            "method": "1. Thu gọn đơn thức trước bằng cách nhân các hệ số và các luỹ thừa cùng biến.\n2. Thay giá trị của biến vào biểu thức thu gọn để tính giá trị số.",
            "steps": [
                "**Bước 1 (Câu a):**\n- Thu gọn: $A = \\left[(-2) \\cdot \\frac{1}{2}\\right] \\cdot (x^2 \\cdot x) \\cdot (y \\cdot y) = -1 \\cdot x^3y^2 = -x^3y^2$.\n- Thay $x = -2, y = \\frac{1}{2}$ vào $A$:\n  $$A = -(-2)^3 \\cdot \\left(\\frac{1}{2}\\right)^2 = -(-8) \\cdot \\frac{1}{4} = 8 \\cdot \\frac{1}{4} = 2.$$",
                "**Bước 2 (Câu b):**\n- Thu gọn: $B = (-0,5) \\cdot x \\cdot (y \\cdot y^2) \\cdot (z \\cdot z) = -0,5xy^3z^2$.\n- Thay $x = 4; y = 0,5 = \\frac{1}{2}; z = 2$ vào $B$:\n  $$B = -0,5 \\cdot 4 \\cdot (0,5)^3 \\cdot 2^2 = -2 \\cdot 0,125 \\cdot 4 = -2 \\cdot 0,5 = -1.$$"
            ],
            "conclusion": "a) $A = -x^3y^2$, giá trị tại $x = -2, y = \\frac{1}{2}$ là $2$.\nb) $B = -0,5xy^3z^2$, giá trị tại $x = 4, y = 0,5, z = 2$ là $-1$."
        },
        {
            "id": "1.4",
            "title": "Bài 1.4 (Trang 10)",
            "problem": "Sắp xếp các đơn thức sau thành từng nhóm, mỗi nhóm chứa tất cả các đơn thức đồng dạng với nhau:\n$$3x^3y^2;\\quad -0,2x^2y^3;\\quad 7x^3y^2;\\quad -4y;\\quad \\frac{3}{4}x^2y^3;\\quad y\\sqrt{2}.$$",
            "method": "Hai đơn thức đồng dạng là hai đơn thức có hệ số khác 0 và có phần biến giống nhau hoàn toàn.",
            "steps": [
                "**Bước 1 (Phân loại theo phần biến):**\n- Các đơn thức có phần biến là $x^3y^2$: $3x^3y^2$ và $7x^3y^2$.\n- Các đơn thức có phần biến là $x^2y^3$: $-0,2x^2y^3$ và $\\frac{3}{4}x^2y^3$.\n- Các đơn thức có phần biến là $y$: $-4y$ và $y\\sqrt{2} = \\sqrt{2}y$."
            ],
            "conclusion": "Có 3 nhóm đơn thức đồng dạng:\n- Nhóm 1: $3x^3y^2$ và $7x^3y^2$.\n- Nhóm 2: $-0,2x^2y^3$ và $\\frac{3}{4}x^2y^3$.\n- Nhóm 3: $-4y$ và $y\\sqrt{2}$."
        },
        {
            "id": "1.5",
            "title": "Bài 1.5 (Trang 10)",
            "problem": "Rút gọn rồi tính giá trị của biểu thức:\n$$S = \\frac{1}{2}x^2y^5 - \\frac{5}{2}x^2y^5 \\quad \\text{khi } x = -2 \\text{ và } y = 1.$$",
            "method": "Hai đơn thức có cùng phần biến $x^2y^5$, ta trừ hệ số và giữ nguyên phần biến. Sau đó thay giá trị $x, y$ vào kết quả.",
            "steps": [
                "**Bước 1 (Rút gọn):**\n$$S = \\left(\\frac{1}{2} - \\frac{5}{2}\\right)x^2y^5 = \\frac{-4}{2}x^2y^5 = -2x^2y^5.$$",
                "**Bước 2 (Tính giá trị):**\nThay $x = -2$ và $y = 1$ vào $S$:\n$$S = -2 \\cdot (-2)^2 \\cdot 1^5 = -2 \\cdot 4 \\cdot 1 = -8.$$"
            ],
            "conclusion": "Biểu thức rút gọn là $S = -2x^2y^5$. Giá trị tại $x = -2, y = 1$ là $-8$."
        },
        {
            "id": "1.6",
            "title": "Bài 1.6 (Trang 10)",
            "problem": "Tính tổng của bốn đơn thức:\n$$2x^2y^3;\\quad -\\frac{3}{5}x^2y^3;\\quad -14x^2y^3;\\quad \\frac{8}{5}x^2y^3.$$",
            "method": "Cả bốn đơn thức đều đồng dạng (cùng phần biến $x^2y^3$). Ta cộng các hệ số và giữ nguyên phần biến.",
            "steps": [
                "**Bước 1 (Lập tổng hệ số):**\n$$\\text{Tổng} = \\left(2 - \\frac{3}{5} - 14 + \\frac{8}{5}\\right)x^2y^3.$$",
                "**Bước 2 (Tính toán hệ số):**\n$$\\left(2 - 14\\right) + \\left(\\frac{8}{5} - \\frac{3}{5}\\right) = -12 + \\frac{5}{5} = -12 + 1 = -11.$$"
            ],
            "conclusion": "Tổng của bốn đơn thức là $-11x^2y^3$."
        },
        {
            "id": "1.7",
            "title": "Bài 1.7 (Trang 10)",
            "problem": "Một mảnh đất có dạng như phần được tô màu xanh trong hình bên cùng với các kích thước được ghi trên đó. Hãy tìm đơn thức (thu gọn) với hai biến $x$ và $y$ biểu thị diện tích của mảnh đất đã cho bằng hai cách:\n- Cách 1. Tính tổng diện tích của hai hình chữ nhật $ABCD$ và $EFGC$.\n- Cách 2. Lấy diện tích của hình chữ nhật $HFGD$ trừ đi diện tích của hình chữ nhật $HEBA$.",
            "method": "Sử dụng công thức diện tích hình chữ nhật: $S = \\text{dài} \\times \\text{rộng}$.",
            "steps": [
                "**Bước 1 (Cách 1 - Tổng hai hình chữ nhật con):**\n- Hình chữ nhật $ABCD$ có chiều dài $DC = 2y$, chiều rộng $AD = 2x \\Rightarrow S_{ABCD} = 2x \\cdot 2y = 4xy$.\n- Hình chữ nhật $EFGC$ có chiều dài $FG = 3x$, chiều rộng $CG = y \\Rightarrow S_{EFGC} = 3x \\cdot y = 3xy$.\n- Tổng diện tích: $S = S_{ABCD} + S_{EFGC} = 4xy + 3xy = 7xy$.",
                "**Bước 2 (Cách 2 - Hiệu hai hình chữ nhật):**\n- Hình chữ nhật lớn $HFGD$ có cạnh $DG = DC + CG = 2y + y = 3y$, cạnh $FG = 3x$.\n  $\\Rightarrow S_{HFGD} = 3x \\cdot 3y = 9xy$.\n- Hình chữ nhật khuyết $HEBA$ có cạnh $HE = DC = 2y$, cạnh $HA = HD - AD = 3x - 2x = x$.\n  $\\Rightarrow S_{HEBA} = x \\cdot 2y = 2xy$.\n- Diện tích mảnh đất: $S = S_{HFGD} - S_{HEBA} = 9xy - 2xy = 7xy$."
            ],
            "conclusion": "Cả hai cách đều cho kết quả diện tích mảnh đất là đơn thức thu gọn $7xy$."
        }
    ],
    "Bai_02_Da_thuc.md": [
        {
            "id": "1.8",
            "title": "Bài 1.8 (Trang 14)",
            "problem": "Trong các biểu thức sau, biểu thức nào là đa thức?\n$$-x^2 + 3x + 1;\\quad \\frac{x}{\\sqrt{5}};\\quad x - \\frac{\\sqrt{5}}{x};\\quad 2024;\\quad 3x^2y - 5xy + 2,4;\\quad \\frac{1}{x^2 + x + 1}.$$",
            "method": "Đa thức là tổng của những đơn thức. Biểu thức có biến ở mẫu số thì không phải là đa thức.",
            "steps": [
                "**Bước 1 (Kiểm tra từng biểu thức):**\n- $-x^2 + 3x + 1$: Là tổng các đơn thức $-x^2, 3x, 1 \\Rightarrow$ Là đa thức.\n- $\\frac{x}{\\sqrt{5}} = \\frac{1}{\\sqrt{5}}x$: Là một đơn thức, mà mỗi đơn thức cũng là đa thức $\\Rightarrow$ Là đa thức.\n- $x - \\frac{\\sqrt{5}}{x}$: Chứa biến $x$ ở mẫu số $\\Rightarrow$ Không là đa thức.\n- $2024$: Là một số thực khác 0 (đơn thức bậc 0) $\\Rightarrow$ Là đa thức.\n- $3x^2y - 5xy + 2,4$: Tổng của các đơn thức $3x^2y, -5xy, 2,4 \\Rightarrow$ Là đa thức.\n- $\\frac{1}{x^2 + x + 1}$: Chứa biến ở mẫu số $\\Rightarrow$ Không là đa thức."
            ],
            "conclusion": "Các đa thức gồm: $-x^2 + 3x + 1;\\quad \\frac{x}{\\sqrt{5}};\\quad 2024;\\quad 3x^2y - 5xy + 2,4$."
        },
        {
            "id": "1.9",
            "title": "Bài 1.9 (Trang 14)",
            "problem": "Xác định hệ số và bậc của từng hạng tử trong đa thức sau:\na) $x^2y - 3xy + 5x^2y^2 + 0,5x - 4$;\nb) $x\\sqrt{2} - 2xy^3 + y^3 - 7x^3y$.",
            "method": "Mỗi số hạng trong tổng đại số là một hạng tử. Hệ số là phần số, bậc của hạng tử là tổng số mũ của các biến trong hạng tử đó.",
            "steps": [
                "**Bước 1 (Câu a):**\n- Hạng tử $x^2y$: Hệ số là $1$, bậc là $2 + 1 = 3$.\n- Hạng tử $-3xy$: Hệ số là $-3$, bậc là $1 + 1 = 2$.\n- Hạng tử $5x^2y^2$: Hệ số là $5$, bậc là $2 + 2 = 4$.\n- Hạng tử $0,5x$: Hệ số là $0,5$, bậc là $1$.\n- Hạng tử $-4$: Hệ số là $-4$, bậc là $0$.",
                "**Bước 2 (Câu b):**\n- Hạng tử $x\\sqrt{2}$: Hệ số là $\\sqrt{2}$, bậc là $1$.\n- Hạng tử $-2xy^3$: Hệ số là $-2$, bậc là $1 + 3 = 4$.\n- Hạng tử $y^3$: Hệ số là $1$, bậc là $3$.\n- Hạng tử $-7x^3y$: Hệ số là $-7$, bậc là $3 + 1 = 4$."
            ],
            "conclusion": "Đã xác định đầy đủ hệ số và bậc cho từng hạng tử của cả 2 đa thức."
        },
        {
            "id": "1.10",
            "title": "Bài 1.10 (Trang 14)",
            "problem": "Thu gọn đa thức:\na) $5x^4 - 2x^3y + 20xy^3 + 6x^3y - 3x^2y^2 + xy^3 - y^4$;\nb) $0,6x^3 + x^2z - 2,7xy^2 + 0,4x^3 + 1,7xy^2$.",
            "method": "Nhóm các hạng tử đồng dạng lại và thực hiện cộng trừ hệ số.",
            "steps": [
                "**Bước 1 (Câu a):**\n$$\\begin{aligned} & 5x^4 + (-2x^3y + 6x^3y) - 3x^2y^2 + (20xy^3 + xy^3) - y^4 \\\\ = & 5x^4 + 4x^3y - 3x^2y^2 + 21xy^3 - y^4. \\end{aligned}$$",
                "**Bước 2 (Câu b):**\n$$\\begin{aligned} & (0,6x^3 + 0,4x^3) + x^2z + (-2,7xy^2 + 1,7xy^2) \\\\ = & 1x^3 + x^2z - 1xy^2 = x^3 + x^2z - xy^2. \\end{aligned}$$"
            ],
            "conclusion": "a) $5x^4 + 4x^3y - 3x^2y^2 + 21xy^3 - y^4$.\nb) $x^3 + x^2z - xy^2$."
        },
        {
            "id": "1.11",
            "title": "Bài 1.11 (Trang 14)",
            "problem": "Thu gọn (nếu cần) và tìm bậc của mỗi đa thức sau:\na) $x^4 - 3x^2y^2 + 3xy^2 - x^4 + 1$;\nb) $5x^2y + 8xy - 2x^2 - 5x^2y + x^2$.",
            "method": "Thu gọn đa thức trước. Bậc của đa thức là bậc của hạng tử có bậc cao nhất trong dạng thu gọn.",
            "steps": [
                "**Bước 1 (Câu a):**\n- Thu gọn: $(x^4 - x^4) - 3x^2y^2 + 3xy^2 + 1 = -3x^2y^2 + 3xy^2 + 1$.\n- Hạng tử $-3x^2y^2$ có bậc $2 + 2 = 4$; $3xy^2$ có bậc 3; $1$ có bậc 0.\n- Bậc của đa thức là 4.",
                "**Bước 2 (Câu b):**\n- Thu gọn: $(5x^2y - 5x^2y) + 8xy + (-2x^2 + x^2) = 8xy - x^2$.\n- Cả hai hạng tử $8xy$ và $-x^2$ đều có bậc 2.\n- Bậc của đa thức là 2."
            ],
            "conclusion": "a) Dạng thu gọn là $-3x^2y^2 + 3xy^2 + 1$, bậc 4.\nb) Dạng thu gọn là $8xy - x^2$, bậc 2."
        },
        {
            "id": "1.12",
            "title": "Bài 1.12 (Trang 14)",
            "problem": "Thu gọn rồi tính giá trị của đa thức:\n$$M = \\frac{1}{3}x^2y + xy^2 - xy + \\frac{1}{2}xy^2 - 5xy - \\frac{1}{3}x^2y \\quad \\text{tại } x = 0,5 \\text{ và } y = 1.$$",
            "method": "Thu gọn nhóm các hạng tử đồng dạng, sau đó thay số $x = 0,5 = \\frac{1}{2}$ và $y = 1$.",
            "steps": [
                "**Bước 1 (Thu gọn M):**\n$$\\begin{aligned} M &= \\left(\\frac{1}{3}x^2y - \\frac{1}{3}x^2y\\right) + \\left(xy^2 + \\frac{1}{2}xy^2\\right) + (-xy - 5xy) \\\\ &= 0 + \\frac{3}{2}xy^2 - 6xy = \\frac{3}{2}xy^2 - 6xy. \\end{aligned}$$",
                "**Bước 2 (Tính giá trị tại $x = 0,5; y = 1$):**\n$$M = \\frac{3}{2} \\cdot 0,5 \\cdot 1^2 - 6 \\cdot 0,5 \\cdot 1 = \\frac{3}{2} \\cdot \\frac{1}{2} - 3 = \\frac{3}{4} - 3 = -\\frac{9}{4} = -2,25.$$"
            ],
            "conclusion": "Dạng thu gọn: $M = \\frac{3}{2}xy^2 - 6xy$. Giá trị là $-\\frac{9}{4}$ (hoặc $-2,25$)."
        },
        {
            "id": "1.13",
            "title": "Bài 1.13 (Trang 14)",
            "problem": "Cho đa thức $P = 8x^2y^2z - 2xyz + 5y^2z - 5x^2y^2z + x^2y^2 - 3x^2y^2z$.\na) Thu gọn và tìm bậc của đa thức $P$;\nb) Tính giá trị của đa thức $P$ tại $x = -4; y = 2$ và $z = 1$.",
            "method": "Nhóm các hạng tử có cùng phần biến $x^2y^2z$ lại với nhau.",
            "steps": [
                "**Bước 1 (Câu a - Thu gọn và tìm bậc):**\n$$\\begin{aligned} P &= (8x^2y^2z - 5x^2y^2z - 3x^2y^2z) + x^2y^2 - 2xyz + 5y^2z \\\\ &= 0 + x^2y^2 - 2xyz + 5y^2z = x^2y^2 - 2xyz + 5y^2z. \\end{aligned}$$\n- Bậc của $x^2y^2$ là $2 + 2 = 4$.\n- Bậc của $-2xyz$ là $1 + 1 + 1 = 3$.\n- Bậc của $5y^2z$ là $2 + 1 = 3$.\n$\\Rightarrow$ Bậc của đa thức $P$ là $4$.",
                "**Bước 2 (Câu b - Tính giá trị):**\nThay $x = -4, y = 2, z = 1$ vào $P$:\n$$\\begin{aligned} P &= (-4)^2 \\cdot 2^2 - 2 \\cdot (-4) \\cdot 2 \\cdot 1 + 5 \\cdot 2^2 \\cdot 1 \\\\ &= 16 \\cdot 4 - (-16) + 5 \\cdot 4 \\\\ &= 64 + 16 + 20 = 100. \\end{aligned}$$"
            ],
            "conclusion": "a) Thu gọn $P = x^2y^2 - 2xyz + 5y^2z$, bậc là 4.\nb) Giá trị tại $x = -4, y = 2, z = 1$ là $100$."
        }
    ],
    "Bai_03_Phep_cong_va_phep_tru_da_thuc.md": [
        {
            "id": "1.14",
            "title": "Bài 1.14 (Trang 16)",
            "problem": "Tính tổng và hiệu của hai đa thức:\n$$P = x^2y + x^3 - xy^2 + 3 \\quad \\text{và} \\quad Q = x^3 + xy^2 - xy - 6.$$",
            "method": "Nối hai đa thức bởi dấu cộng (cho tổng) hoặc dấu trừ (cho hiệu), bỏ dấu ngoặc rồi nhóm các hạng tử đồng dạng.",
            "steps": [
                "**Bước 1 (Tính tổng $P + Q$):**\n$$\\begin{aligned} P + Q &= (x^2y + x^3 - xy^2 + 3) + (x^3 + xy^2 - xy - 6) \\\\ &= (x^3 + x^3) + x^2y + (-xy^2 + xy^2) - xy + (3 - 6) \\\\ &= 2x^3 + x^2y - xy - 3. \\end{aligned}$$",
                "**Bước 2 (Tính hiệu $P - Q$):**\n$$\\begin{aligned} P - Q &= (x^2y + x^3 - xy^2 + 3) - (x^3 + xy^2 - xy - 6) \\\\ &= x^2y + x^3 - xy^2 + 3 - x^3 - xy^2 + xy + 6 \\\\ &= (x^3 - x^3) + x^2y + (-xy^2 - xy^2) + xy + (3 + 6) \\\\ &= x^2y - 2xy^2 + xy + 9. \\end{aligned}$$"
            ],
            "conclusion": "- Tổng $P + Q = 2x^3 + x^2y - xy - 3$.\n- Hiệu $P - Q = x^2y - 2xy^2 + xy + 9$."
        },
        {
            "id": "1.15",
            "title": "Bài 1.15 (Trang 16)",
            "problem": "Rút gọn biểu thức:\na) $(x - y) + (y - z) + (z - x)$;\nb) $(2x - 3y) + (2y - 3z) + (2z - 3x)$.",
            "method": "Bỏ dấu ngoặc (trước ngoặc là dấu cộng nên giữ nguyên dấu các hạng tử), nhóm các biến cùng loại với nhau.",
            "steps": [
                "**Bước 1 (Câu a):**\n$$(x - y) + (y - z) + (z - x) = (x - x) + (-y + y) + (-z + z) = 0 + 0 + 0 = 0.$$",
                "**Bước 2 (Câu b):**\n$$\\begin{aligned} & (2x - 3y) + (2y - 3z) + (2z - 3x) \\\\ = & (2x - 3x) + (-3y + 2y) + (-3z + 2z) \\\\ = & -x - y - z = -(x + y + z). \\end{aligned}$$"
            ],
            "conclusion": "a) Kết quả bằng $0$.\nb) Kết quả là $-x - y - z$ (hoặc $-(x + y + z)$)."
        },
        {
            "id": "1.16",
            "title": "Bài 1.16 (Trang 16)",
            "problem": "Tìm đa thức $M$ biết:\n$$M - 5x^2 + xyz = xy + 2x^2 - 3xyz + 5.$$",
            "method": "Áp dụng quy tắc chuyển vế: Chuyển các hạng tử không chứa $M$ sang vế phải và đổi dấu, sau đó thu gọn vế phải.",
            "steps": [
                "**Bước 1 (Chuyển vế):**\n$$M = (xy + 2x^2 - 3xyz + 5) + 5x^2 - xyz.$$",
                "**Bước 2 (Thu gọn):**\n$$\\begin{aligned} M &= (2x^2 + 5x^2) + (-3xyz - xyz) + xy + 5 \\\\ &= 7x^2 - 4xyz + xy + 5. \\end{aligned}$$"
            ],
            "conclusion": "Đa thức cần tìm là $M = 7x^2 - 4xyz + xy + 5$."
        },
        {
            "id": "1.17",
            "title": "Bài 1.17 (Trang 16)",
            "problem": "Cho hai đa thức $A = 2x^2y + 3xyz - 2x + 5$ và $B = 3xyz - 2x^2y + x - 4$.\na) Tìm các đa thức $A + B$ và $A - B$;\nb) Tính giá trị của các đa thức $A$ và $A + B$ tại $x = 0,5; y = -2$ và $z = 1$.",
            "method": "Thực hiện phép cộng/trừ đa thức, sau đó thay trực tiếp số vào biểu thức đã thu gọn.",
            "steps": [
                "**Bước 1 (Câu a - Tính $A + B$ và $A - B$):**\n$$\\begin{aligned} A + B &= (2x^2y + 3xyz - 2x + 5) + (3xyz - 2x^2y + x - 4) \\\\ &= (2x^2y - 2x^2y) + (3xyz + 3xyz) + (-2x + x) + (5 - 4) \\\\ &= 6xyz - x + 1. \\end{aligned}$$\n$$\\begin{aligned} A - B &= (2x^2y + 3xyz - 2x + 5) - (3xyz - 2x^2y + x - 4) \\\\ &= 2x^2y + 3xyz - 2x + 5 - 3xyz + 2x^2y - x + 4 \\\\ &= 4x^2y - 3x + 9. \\end{aligned}$$",
                "**Bước 2 (Câu b - Tính giá trị tại $x = 0,5 = \\frac{1}{2}; y = -2; z = 1$):**\n- Tính giá trị $A$:\n  $$A = 2 \\cdot (0,5)^2 \\cdot (-2) + 3 \\cdot 0,5 \\cdot (-2) \\cdot 1 - 2 \\cdot 0,5 + 5 = 2 \\cdot 0,25 \\cdot (-2) - 3 - 1 + 5 = -1 - 3 - 1 + 5 = 0.$$\n- Tính giá trị $A + B$:\n  $$A + B = 6 \\cdot 0,5 \\cdot (-2) \\cdot 1 - 0,5 + 1 = -6 - 0,5 + 1 = -5,5.$$"
            ],
            "conclusion": "a) $A + B = 6xyz - x + 1$; $A - B = 4x^2y - 3x + 9$.\nb) Tại điểm đã cho: $A = 0$ và $A + B = -5,5$."
        }
    ],
    "Luyen_tap_chung_trang_17.md": [
        {
            "id": "1.18",
            "title": "Bài 1.18 (Trang 17)",
            "problem": "Cho các biểu thức:\n$$\\frac{4}{5}x;\\quad (\\sqrt{2}-1)xy;\\quad -3xy^2;\\quad \\frac{1}{2}x^2y;\\quad \\frac{1}{x}y^3;\\quad -xy + \\sqrt{2};\\quad -\\frac{3}{2}x^2y;\\quad \\frac{\\sqrt{x}}{5}.$$\na) Trong các biểu thức đã cho, biểu thức nào là đơn thức? Biểu thức nào không là đơn thức?\nb) Hãy chỉ ra hệ số và phần biến của mỗi đơn thức đã cho.\nc) Viết tổng tất cả các đơn thức trên để được một đa thức. Xác định bậc của đa thức đó.",
            "method": "Phân loại đơn thức, xác định hệ số/biến/bậc, lập tổng và thu gọn các đơn thức đồng dạng.",
            "steps": [
                "**Bước 1 (Câu a & b - Phân loại và xác định thành phần):**\n- Các đơn thức:\n  + $\\frac{4}{5}x$: Hệ số $\\frac{4}{5}$, phần biến $x$ (bậc 1).\n  + $(\\sqrt{2}-1)xy$: Hệ số $\\sqrt{2}-1$, phần biến $xy$ (bậc 2).\n  + $-3xy^2$: Hệ số $-3$, phần biến $xy^2$ (bậc 3).\n  + $\\frac{1}{2}x^2y$: Hệ số $\\frac{1}{2}$, phần biến $x^2y$ (bậc 3).\n  + $-\\frac{3}{2}x^2y$: Hệ số $-\\frac{3}{2}$, phần biến $x^2y$ (bậc 3).\n- Các biểu thức không là đơn thức:\n  + $\\frac{1}{x}y^3$ (biến $x$ ở mẫu số).\n  + $-xy + \\sqrt{2}$ (chứa phép cộng hai số hạng).\n  + $\\frac{\\sqrt{x}}{5}$ (biến $x$ nằm trong dấu căn).",
                "**Bước 2 (Câu c - Viết tổng và thu gọn):**\n$$\\begin{aligned} T &= \\frac{4}{5}x + (\\sqrt{2}-1)xy - 3xy^2 + \\frac{1}{2}x^2y + \\left(-\\frac{3}{2}x^2y\\right) \\\\ &= \\frac{4}{5}x + (\\sqrt{2}-1)xy - 3xy^2 - x^2y. \\end{aligned}$$\nCác hạng tử có bậc cao nhất là $-3xy^2$ và $-x^2y$ đều có bậc 3. Do đó bậc của đa thức là 3."
            ],
            "conclusion": "- Đơn thức: $\\frac{4}{5}x; (\\sqrt{2}-1)xy; -3xy^2; \\frac{1}{2}x^2y; -\\frac{3}{2}x^2y$.\n- Đa thức tổng: $\\frac{4}{5}x + (\\sqrt{2}-1)xy - 3xy^2 - x^2y$, bậc là 3."
        },
        {
            "id": "1.19",
            "title": "Bài 1.19 (Trang 18)",
            "problem": "Trong một khách sạn có hai bể bơi dạng hình hộp chữ nhật. Bể thứ nhất có chiều sâu là $1,2\\text{ m}$, đáy là hình chữ nhật có chiều dài $x\\text{ mét}$, chiều rộng $y\\text{ mét}$. Bể thứ hai có chiều sâu là $1,5\\text{ m}$, hai kích thước đáy gấp 5 lần hai kích thước đáy của bể thứ nhất.\na) Hãy tìm đơn thức (hai biến $x$ và $y$) biểu thị số mét khối nước cần có để bơm đầy cả hai bể bơi.\nb) Tính lượng nước bơm đầy hai bể nếu $x = 5\\text{ m}, y = 3\\text{ m}$.",
            "method": "Thể tích hình hộp chữ nhật = chiều dài $\\times$ chiều rộng $\\times$ chiều cao.",
            "steps": [
                "**Bước 1 (Câu a - Tìm biểu thức thể tích):**\n- Thể tích bể 1: $V_1 = 1,2 \\cdot x \\cdot y = 1,2xy$ ($m^3$).\n- Kích thước đáy bể 2 là $5x$ và $5y$, chiều sâu $1,5\\text{ m}$:\n  $$V_2 = 1,5 \\cdot (5x) \\cdot (5y) = 1,5 \\cdot 25xy = 37,5xy\\ (m^3).$$\n- Tổng lượng nước bơm đầy cả hai bể:\n  $$V = V_1 + V_2 = 1,2xy + 37,5xy = 38,7xy\\ (m^3).$$",
                "**Bước 2 (Câu b - Tính với $x = 5\\text{ m}, y = 3\\text{ m}$):**\nThay $x = 5, y = 3$ vào $V$:\n$$V = 38,7 \\cdot 5 \\cdot 3 = 38,7 \\cdot 15 = 580,5\\ (m^3).$$"
            ],
            "conclusion": "a) Đơn thức biểu thị lượng nước là $38,7xy\\ (m^3)$.\nb) Lượng nước cần là $580,5\\text{ m}^3$."
        },
        {
            "id": "1.20",
            "title": "Bài 1.20 (Trang 18)",
            "problem": "Tìm bậc của mỗi đa thức sau rồi tính giá trị của chúng tại $x = 1; y = -2$:\n$$P = 5x^4 - 3x^3y + 2xy^3 - x^3y + 2y^4 - 7x^2y^2 - 2xy^3;$$\n$$Q = x^3 + x^2y + xy^2 - x^2y - xy^2 - x^3.$$",
            "method": "Thu gọn đa thức trước, xác định hạng tử có bậc cao nhất, rồi thay số.",
            "steps": [
                "**Bước 1 (Đa thức $P$):**\n- Thu gọn: $P = 5x^4 + (-3x^3y - x^3y) - 7x^2y^2 + (2xy^3 - 2xy^3) + 2y^4 = 5x^4 - 4x^3y - 7x^2y^2 + 2y^4$.\n- Tất cả các hạng tử đều có bậc là $4 \\Rightarrow$ Bậc của $P$ là $4$.\n- Thay $x = 1, y = -2$:\n  $$P = 5 \\cdot 1^4 - 4 \\cdot 1^3 \\cdot (-2) - 7 \\cdot 1^2 \\cdot (-2)^2 + 2 \\cdot (-2)^4 = 5 + 8 - 28 + 32 = 17.$$",
                "**Bước 2 (Đa thức $Q$):**\n- Thu gọn: $Q = (x^3 - x^3) + (x^2y - x^2y) + (xy^2 - xy^2) = 0$.\n- Đa thức $Q$ bằng 0 (đa thức không) nên **không có bậc**.\n- Giá trị của $Q$ tại mọi $x, y$ luôn bằng $0$."
            ],
            "conclusion": "- Đa thức $P$ có bậc 4, giá trị tại $x = 1, y = -2$ là $17$.\n- Đa thức $Q = 0$ không có bậc, giá trị bằng $0$."
        },
        {
            "id": "1.21",
            "title": "Bài 1.21 (Trang 18)",
            "problem": "Cho hai đa thức:\n$$A = 7xyz^2 - 5xy^2z + 3x^2yz - xyz + 1; \\quad B = 7x^2yz - 5xy^2z + 3xyz^2 - 2.$$\na) Tìm đa thức $C$ sao cho $A - C = B$;\nb) Tìm đa thức $D$ sao cho $A + D = B$;\nc) Tìm đa thức $E$ sao cho $E - A = B$.",
            "method": "Sử dụng các hệ thức tìm số hạng: $C = A - B$; $D = B - A$; $E = A + B$.",
            "steps": [
                "**Bước 1 (Câu a - Tìm $C = A - B$):**\n$$\\begin{aligned} C &= (7xyz^2 - 5xy^2z + 3x^2yz - xyz + 1) - (7x^2yz - 5xy^2z + 3xyz^2 - 2) \\\\ &= (7xyz^2 - 3xyz^2) + (-5xy^2z + 5xy^2z) + (3x^2yz - 7x^2yz) - xyz + (1 + 2) \\\\ &= 4xyz^2 - 4x^2yz - xyz + 3. \\end{aligned}$$",
                "**Bước 2 (Câu b - Tìm $D = B - A$):**\nVì $D = -(A - B) = -C$, ta đổi dấu tất cả các hạng tử của $C$:\n$$D = -4xyz^2 + 4x^2yz + xyz - 3.$$",
                "**Bước 3 (Câu c - Tìm $E = A + B$):**\n$$\\begin{aligned} E &= (7xyz^2 - 5xy^2z + 3x^2yz - xyz + 1) + (7x^2yz - 5xy^2z + 3xyz^2 - 2) \\\\ &= (7xyz^2 + 3xyz^2) + (-5xy^2z - 5xy^2z) + (3x^2yz + 7x^2yz) - xyz + (1 - 2) \\\\ &= 10xyz^2 - 10xy^2z + 10x^2yz - xyz - 1. \\end{aligned}$$"
            ],
            "conclusion": "a) $C = 4xyz^2 - 4x^2yz - xyz + 3$.\nb) $D = -4xyz^2 + 4x^2yz + xyz - 3$.\nc) $E = 10xyz^2 - 10xy^2z + 10x^2yz - xyz - 1$."
        },
        {
            "id": "1.22",
            "title": "Bài 1.22 (Trang 18)",
            "problem": "Từ một miếng bìa, người ta cắt ra hai hình tròn có bán kính $x\\text{ centimét}$ và $y\\text{ centimét}$. Tìm biểu thức biểu thị diện tích phần còn lại của miếng bìa, nếu biết miếng bìa có hình dạng gồm hai hình vuông ghép lại và có kích thước (centimét) như Hình 1.2 (cạnh hình vuông nhỏ là $2x$, cạnh hình vuông lớn là $2,5y$). Biểu thức đó có phải là một đa thức không? Nếu phải thì đó là đa thức bậc mấy?",
            "method": "Diện tích còn lại = Diện tích 2 hình vuông trừ đi Diện tích 2 hình tròn ($S_{\\text{tròn}} = \\pi r^2$).",
            "steps": [
                "**Bước 1 (Tính diện tích miếng bìa ban đầu):**\n- Diện tích hình vuông nhỏ cạnh $2x$: $S_1 = (2x)^2 = 4x^2$.\n- Diện tích hình vuông lớn cạnh $2,5y$: $S_2 = (2,5y)^2 = 6,25y^2$.\n$\\Rightarrow$ Tổng diện tích bìa: $S_{\\text{bìa}} = 4x^2 + 6,25y^2$.",
                "**Bước 2 (Tính diện tích hai hình tròn bị cắt):**\n- Hình tròn bán kính $x$: $S_{t1} = \\pi x^2$.\n- Hình tròn bán kính $y$: $S_{t2} = \\pi y^2$.\n$\\Rightarrow$ Tổng diện tích 2 hình tròn: $S_{\\text{tròn}} = \\pi x^2 + \\pi y^2$.",
                "**Bước 3 (Lập biểu thức diện tích phần còn lại):**\n$$S = S_{\\text{bìa}} - S_{\\text{tròn}} = (4x^2 + 6,25y^2) - (\\pi x^2 + \\pi y^2) = (4 - \\pi)x^2 + (6,25 - \\pi)y^2.$$\nVì $\\pi$ là hằng số ($3,14159...$), $4 - \\pi$ và $6,25 - \\pi$ là các hệ số thực, các biến $x, y$ có số mũ nguyên dương nên biểu thức $S$ là một đa thức bậc hai."
            ],
            "conclusion": "Biểu thức diện tích còn lại là $S = (4 - \\pi)x^2 + (6,25 - \\pi)y^2$. Đây là một đa thức và có bậc là 2."
        },
        {
            "id": "1.23",
            "title": "Bài 1.23 (Trang 18)",
            "problem": "Cho ba đa thức:\n$$M = 3x^3 - 4x^2y + 3x - y; \\quad N = 5xy - 3x + 2; \\quad P = 3x^3 + 2x^2y + 7x - 1.$$\nTính $M + N - P$ và $M - N - P$.",
            "method": "Thay các đa thức vào biểu thức, chú ý mở ngoặc và đổi dấu khi đằng trước là dấu trừ.",
            "steps": [
                "**Bước 1 (Tính $M + N - P$):**\n$$\\begin{aligned} & (3x^3 - 4x^2y + 3x - y) + (5xy - 3x + 2) - (3x^3 + 2x^2y + 7x - 1) \\\\ = & 3x^3 - 4x^2y + 3x - y + 5xy - 3x + 2 - 3x^3 - 2x^2y - 7x + 1 \\\\ = & (3x^3 - 3x^3) + (-4x^2y - 2x^2y) + 5xy + (3x - 3x - 7x) - y + (2 + 1) \\\\ = & -6x^2y + 5xy - 7x - y + 3. \\end{aligned}$$",
                "**Bước 2 (Tính $M - N - P$):**\n$$\\begin{aligned} & (3x^3 - 4x^2y + 3x - y) - (5xy - 3x + 2) - (3x^3 + 2x^2y + 7x - 1) \\\\ = & 3x^3 - 4x^2y + 3x - y - 5xy + 3x - 2 - 3x^3 - 2x^2y - 7x + 1 \\\\ = & (3x^3 - 3x^3) + (-4x^2y - 2x^2y) - 5xy + (3x + 3x - 7x) - y + (-2 + 1) \\\\ = & -6x^2y - 5xy - x - y - 1. \\end{aligned}$$"
            ],
            "conclusion": "- $M + N - P = -6x^2y + 5xy - 7x - y + 3$.\n- $M - N - P = -6x^2y - 5xy - x - y - 1$."
        }
    ],
    "Bai_04_Phep_nhan_da_thuc.md": [
        {
            "id": "1.24",
            "title": "Bài 1.24 (Trang 21)",
            "problem": "Nhân hai đơn thức:\na) $5x^2y$ và $2xy^2$;\nb) $\\frac{3}{4}xy$ và $8x^3y^2$;\nc) $1,5xy^2z^3$ và $2x^3y^2z$.",
            "method": "Nhân hệ số với hệ số, nhân các luỹ thừa cùng biến với nhau ($x^m \\cdot x^n = x^{m+n}$).",
            "steps": [
                "**Bước 1 (Câu a):**\n$$5x^2y \\cdot 2xy^2 = (5 \\cdot 2) \\cdot (x^2 \\cdot x) \\cdot (y \\cdot y^2) = 10x^3y^3.$$",
                "**Bước 2 (Câu b):**\n$$\\frac{3}{4}xy \\cdot 8x^3y^2 = \\left(\\frac{3}{4} \\cdot 8\\right) \\cdot (x \\cdot x^3) \\cdot (y \\cdot y^2) = 6x^4y^3.$$",
                "**Bước 3 (Câu c):**\n$$1,5xy^2z^3 \\cdot 2x^3y^2z = (1,5 \\cdot 2) \\cdot (x \\cdot x^3) \\cdot (y^2 \\cdot y^2) \\cdot (z^3 \\cdot z) = 3x^4y^4z^4.$$"
            ],
            "conclusion": "a) $10x^3y^3$.\nb) $6x^4y^3$.\nc) $3x^4y^4z^4$."
        },
        {
            "id": "1.25",
            "title": "Bài 1.25 (Trang 21)",
            "problem": "Tìm tích của đơn thức với đa thức:\na) $(-0,5)xy^2(2xy - x^2 + 4y)$;\nb) $\\left(x^3y - \\frac{1}{2}x^2 + \\frac{1}{3}xy\\right)6xy^3$.",
            "method": "Nhân đơn thức với từng hạng tử của đa thức rồi cộng các kết quả lại.",
            "steps": [
                "**Bước 1 (Câu a):**\n$$\\begin{aligned} & (-0,5)xy^2 \\cdot 2xy + (-0,5)xy^2 \\cdot (-x^2) + (-0,5)xy^2 \\cdot 4y \\\\ = & -x^2y^3 + 0,5x^3y^2 - 2xy^3. \\end{aligned}$$",
                "**Bước 2 (Câu b):**\n$$\\begin{aligned} & x^3y \\cdot 6xy^3 + \\left(-\\frac{1}{2}x^2\\right) \\cdot 6xy^3 + \\frac{1}{3}xy \\cdot 6xy^3 \\\\ = & 6x^4y^4 - 3x^3y^3 + 2x^2y^4. \\end{aligned}$$"
            ],
            "conclusion": "a) $-x^2y^3 + 0,5x^3y^2 - 2xy^3$.\nb) $6x^4y^4 - 3x^3y^3 + 2x^2y^4$."
        },
        {
            "id": "1.26",
            "title": "Bài 1.26 (Trang 21)",
            "problem": "Rút gọn biểu thức: $x(x^2 - y) - x^2(x + y) + xy(x - 1)$.",
            "method": "Nhân đơn thức với đa thức cho từng cụm, sau đó thu gọn các hạng tử đồng dạng.",
            "steps": [
                "**Bước 1 (Khai triển các tích):**\n- $x(x^2 - y) = x^3 - xy$.\n- $-x^2(x + y) = -x^3 - x^2y$.\n- $xy(x - 1) = x^2y - xy$.",
                "**Bước 2 (Nhóm và thu gọn):**\n$$\\begin{aligned} \\text{Biểu thức} &= (x^3 - xy) - (x^3 + x^2y) + (x^2y - xy) \\\\ &= x^3 - xy - x^3 - x^2y + x^2y - xy \\\\ &= (x^3 - x^3) + (-x^2y + x^2y) + (-xy - xy) \\\\ &= -2xy. \\end{aligned}$$"
            ],
            "conclusion": "Biểu thức rút gọn là $-2xy$."
        },
        {
            "id": "1.27",
            "title": "Bài 1.27 (Trang 21)",
            "problem": "Làm tính nhân:\na) $(x^2 - xy + 1)(xy + 3)$;\nb) $\\left(x^2y^2 - \\frac{1}{2}xy + 2\\right)(x - 2y)$.",
            "method": "Nhân từng hạng tử của đa thức thứ nhất với từng hạng tử của đa thức thứ hai rồi cộng các tích.",
            "steps": [
                "**Bước 1 (Câu a):**\n$$\\begin{aligned} & (x^2 - xy + 1)(xy + 3) \\\\ = & x^2(xy + 3) - xy(xy + 3) + 1(xy + 3) \\\\ = & x^3y + 3x^2 - x^2y^2 - 3xy + xy + 3 \\\\ = & x^3y + 3x^2 - x^2y^2 - 2xy + 3. \\end{aligned}$$",
                "**Bước 2 (Câu b):**\n$$\\begin{aligned} & \\left(x^2y^2 - \\frac{1}{2}xy + 2\\right)(x - 2y) \\\\ = & x^2y^2(x - 2y) - \\frac{1}{2}xy(x - 2y) + 2(x - 2y) \\\\ = & x^3y^2 - 2x^2y^3 - \\frac{1}{2}x^2y + xy^2 + 2x - 4y. \\end{aligned}$$"
            ],
            "conclusion": "a) $x^3y + 3x^2 - x^2y^2 - 2xy + 3$.\nb) $x^3y^2 - 2x^2y^3 - \\frac{1}{2}x^2y + xy^2 + 2x - 4y$."
        },
        {
            "id": "1.28",
            "title": "Bài 1.28 (Trang 21)",
            "problem": "Rút gọn biểu thức sau để thấy rằng giá trị của nó không phụ thuộc vào giá trị của biến:\n$$(x - 5)(2x + 3) - 2x(x - 3) + x + 7.$$",
            "method": "Khai triển các tích đa thức và đơn thức, sau đó thu gọn. Nếu kết quả là một hằng số (không còn biến $x$) thì giá trị biểu thức không phụ thuộc vào biến.",
            "steps": [
                "**Bước 1 (Khai triển):**\n- $(x - 5)(2x + 3) = 2x^2 + 3x - 10x - 15 = 2x^2 - 7x - 15$.\n- $-2x(x - 3) = -2x^2 + 6x$.",
                "**Bước 2 (Thu gọn toàn bộ):**\n$$\\begin{aligned} & (2x^2 - 7x - 15) + (-2x^2 + 6x) + x + 7 \\\\ = & (2x^2 - 2x^2) + (-7x + 6x + x) + (-15 + 7) \\\\ = & 0 + 0 - 8 = -8. \\end{aligned}$$"
            ],
            "conclusion": "Biểu thức rút gọn bằng $-8$ (hằng số), vậy giá trị của biểu thức luôn bằng $-8$ với mọi giá trị của biến $x$ (không phụ thuộc vào $x$)."
        },
        {
            "id": "1.29",
            "title": "Bài 1.29 (Trang 21)",
            "problem": "Chứng minh đẳng thức sau:\n$$(2x + y)(2x^2 + xy - y^2) = (2x - y)(2x^2 + 3xy + y^2).$$",
            "method": "Biến đổi vế trái (VT) và vế phải (VP) thành các đa thức thu gọn. Nếu $VT = VP$ thì đẳng thức được chứng minh.",
            "steps": [
                "**Bước 1 (Biến đổi Vế Trái):**\n$$\\begin{aligned} VT &= (2x + y)(2x^2 + xy - y^2) \\\\ &= 2x(2x^2 + xy - y^2) + y(2x^2 + xy - y^2) \\\\ &= 4x^3 + 2x^2y - 2xy^2 + 2x^2y + xy^2 - y^3 \\\\ &= 4x^3 + 4x^2y - xy^2 - y^3. \\end{aligned}$$",
                "**Bước 2 (Biến đổi Vế Phải):**\n$$\\begin{aligned} VP &= (2x - y)(2x^2 + 3xy + y^2) \\\\ &= 2x(2x^2 + 3xy + y^2) - y(2x^2 + 3xy + y^2) \\\\ &= 4x^3 + 6x^2y + 2xy^2 - 2x^2y - 3xy^2 - y^3 \\\\ &= 4x^3 + 4x^2y - xy^2 - y^3. \\end{aligned}$$"
            ],
            "conclusion": "Vì $VT = VP = 4x^3 + 4x^2y - xy^2 - y^3$, đẳng thức đã được chứng minh."
        }
    ],
    "Bai_05_Phep_chia_da_thuc_cho_don_thuc.md": [
        {
            "id": "1.30",
            "title": "Bài 1.30 (Trang 24)",
            "problem": "a) Tìm đơn thức $M$, biết rằng $\\frac{7}{3}x^3y^2 : M = 7xy^2$.\nb) Tìm đơn thức $N$ sao cho $N : 0,5xy^2z = -xy$.",
            "method": "Áp dụng quan hệ phép chia: Nếu $A : M = B \\Rightarrow M = A : B$; nếu $N : A = B \\Rightarrow N = A \\cdot B$.",
            "steps": [
                "**Bước 1 (Câu a - Tìm $M$):**\n$$M = \\left(\\frac{7}{3}x^3y^2\\right) : (7xy^2) = \\left(\\frac{7}{3} : 7\\right) \\cdot (x^3 : x) \\cdot (y^2 : y^2) = \\frac{1}{3}x^2.$$",
                "**Bước 2 (Câu b - Tìm $N$):**\n$$N = (-xy) \\cdot (0,5xy^2z) = -0,5 \\cdot (x \\cdot x) \\cdot (y \\cdot y^2) \\cdot z = -0,5x^2y^3z.$$"
            ],
            "conclusion": "a) $M = \\frac{1}{3}x^2$.\nb) $N = -0,5x^2y^3z$."
        },
        {
            "id": "1.31",
            "title": "Bài 1.31 (Trang 24)",
            "problem": "Cho đa thức $A = 9xy^4 - 12x^2y^3 + 6x^3y^2$. Với mỗi trường hợp sau đây, xét xem $A$ có chia hết cho đơn thức $B$ hay không? Thực hiện phép chia trong trường hợp $A$ chia hết cho $B$:\na) $B = 3x^2y$;\nb) $B = -3xy^2$.",
            "method": "Đa thức $A$ chia hết cho đơn thức $B$ khi và chỉ khi mọi hạng tử của $A$ đều chia hết cho $B$.",
            "steps": [
                "**Bước 1 (Câu a - Xét $B = 3x^2y$):**\n- Hạng tử đầu tiên của $A$ là $9xy^4$ có số mũ của biến $x$ là $1$, nhỏ hơn số mũ của $x$ trong $B$ (là $2$).\n- Do đó $9xy^4$ không chia hết cho $3x^2y$, nên đa thức $A$ **không chia hết** cho $B = 3x^2y$.",
                "**Bước 2 (Câu b - Xét $B = -3xy^2$):**\n- Trong $B$, số mũ của $x$ là $1$, số mũ của $y$ là $2$.\n- Hạng tử $9xy^4$: số mũ $x$ là 1, $y$ là 4 (đều $\\ge$ số mũ trong $B$) $\\Rightarrow$ chia hết.\n- Hạng tử $-12x^2y^3$: số mũ $x$ là 2, $y$ là 3 (đều $\\ge$ số mũ trong $B$) $\\Rightarrow$ chia hết.\n- Hạng tử $6x^3y^2$: số mũ $x$ là 3, $y$ là 2 (đều $\\ge$ số mũ trong $B$) $\\Rightarrow$ chia hết.\n- Vậy $A$ chia hết cho $B$. Thực hiện phép chia:\n  $$\\begin{aligned} A : B &= (9xy^4 : -3xy^2) + (-12x^2y^3 : -3xy^2) + (6x^3y^2 : -3xy^2) \\\\ &= -3y^2 + 4xy - 2x^2. \\end{aligned}$$"
            ],
            "conclusion": "a) Đa thức $A$ không chia hết cho $3x^2y$.\nb) Đa thức $A$ chia hết cho $-3xy^2$ và thương là $-3y^2 + 4xy - 2x^2$."
        },
        {
            "id": "1.32",
            "title": "Bài 1.32 (Trang 24)",
            "problem": "Thực hiện phép chia:\n$$(7y^5z^2 - 14y^4z^3 + 2,1y^3z^4) : (-7y^3z^2).$$",
            "method": "Chia lần lượt từng hạng tử của đa thức cho đơn thức rồi cộng các thương lại.",
            "steps": [
                "**Bước 1 (Chia từng hạng tử):**\n- $7y^5z^2 : (-7y^3z^2) = [7 : (-7)] \\cdot (y^5 : y^3) \\cdot (z^2 : z^2) = -y^2$.\n- $-14y^4z^3 : (-7y^3z^2) = [-14 : (-7)] \\cdot (y^4 : y^3) \\cdot (z^3 : z^2) = 2yz$.\n- $2,1y^3z^4 : (-7y^3z^2) = [2,1 : (-7)] \\cdot (y^3 : y^3) \\cdot (z^4 : z^2) = -0,3z^2$.",
                "**Bước 2 (Tổng hợp kết quả):**\n$$-y^2 + 2yz - 0,3z^2.$$"
            ],
            "conclusion": "Kết quả phép chia là $-y^2 + 2yz - 0,3z^2$."
        }
    ],
    "Luyen_tap_chung_trang_25.md": [
        {
            "id": "1.33",
            "title": "Bài 1.33 (Trang 25)",
            "problem": "Cho biểu thức $P = 5x(3x^2y - 2xy^2 + 1) - 3xy(5x^2 - 3xy) + x^2y^2$.\na) Bằng cách thu gọn, chứng tỏ rằng giá trị của biểu thức $P$ chỉ phụ thuộc vào biến $x$ mà không phụ thuộc vào biến $y$.\nb) Tìm giá trị của $x$ sao cho $P = 10$.",
            "method": "Khai triển và thu gọn đa thức. Tìm $x$ bằng cách giải phương trình bậc nhất $P(x) = 10$.",
            "steps": [
                "**Bước 1 (Câu a - Khai triển và thu gọn):**\n$$\\begin{aligned} P &= 5x \\cdot 3x^2y - 5x \\cdot 2xy^2 + 5x \\cdot 1 - 3xy \\cdot 5x^2 + 3xy \\cdot 3xy + x^2y^2 \\\\ &= 15x^3y - 10x^2y^2 + 5x - 15x^3y + 9x^2y^2 + x^2y^2 \\\\ &= (15x^3y - 15x^3y) + (-10x^2y^2 + 9x^2y^2 + x^2y^2) + 5x \\\\ &= 0 + 0 + 5x = 5x. \\end{aligned}$$\nVì $P = 5x$ không chứa biến $y$, nên giá trị của $P$ chỉ phụ thuộc vào $x$, không phụ thuộc vào $y$.",
                "**Bước 2 (Câu b - Tìm $x$):**\nĐể $P = 10 \\Rightarrow 5x = 10 \\Rightarrow x = \\frac{10}{5} = 2$."
            ],
            "conclusion": "a) Thu gọn $P = 5x$ (chứng minh xong).\nb) $x = 2$."
        },
        {
            "id": "1.34",
            "title": "Bài 1.34 (Trang 25)",
            "problem": "Rút gọn biểu thức:\n$$(3x^2 - 5xy - 4y^2) \\cdot (2x^2 + y^2) + (2x^4y - x^3y^3 - x^2y^4) : \\left(\\frac{1}{5}xy\\right).$$",
            "method": "Thực hiện phép nhân hai đa thức ở phần thứ nhất, phép chia đa thức cho đơn thức ở phần thứ hai, rồi cộng hai kết quả lại.",
            "steps": [
                "**Bước 1 (Thực hiện phép nhân):**\n$$\\begin{aligned} & (3x^2 - 5xy - 4y^2)(2x^2 + y^2) \\\\ = & 3x^2(2x^2 + y^2) - 5xy(2x^2 + y^2) - 4y^2(2x^2 + y^2) \\\\ = & 6x^4 + 3x^2y^2 - 10x^3y - 5xy^3 - 8x^2y^2 - 4y^4 \\\\ = & 6x^4 - 10x^3y - 5x^2y^2 - 5xy^3 - 4y^4. \\end{aligned}$$",
                "**Bước 2 (Thực hiện phép chia):**\n$$\\begin{aligned} & (2x^4y - x^3y^3 - x^2y^4) : \\left(\\frac{1}{5}xy\\right) \\\\ = & (2 : 0,2)x^3 - (1 : 0,2)x^2y^2 - (1 : 0,2)xy^3 \\\\ = & 10x^3y^0 - 5x^2y^2 - 5xy^3 = 10x^3 - 5x^2y^2 - 5xy^3. \\end{aligned}$$",
                "**Bước 3 (Cộng hai kết quả):**\n$$\\begin{aligned} & (6x^4 - 10x^3y - 5x^2y^2 - 5xy^3 - 4y^4) + (10x^3 - 5x^2y^2 - 5xy^3) \\\\ = & 6x^4 + 10x^3 - 10x^3y - 10x^2y^2 - 10xy^3 - 4y^4. \\end{aligned}$$"
            ],
            "conclusion": "Biểu thức rút gọn là $6x^4 + 10x^3 - 10x^3y - 10x^2y^2 - 10xy^3 - 4y^4$."
        },
        {
            "id": "1.35",
            "title": "Bài 1.35 (Trang 26)",
            "problem": "Bà Khanh dự định mua $x$ hộp sữa, mỗi hộp giá $y$ đồng. Nhưng khi đến cửa hàng, bà Khanh thấy giá sữa đã giảm $1\\ 500$ đồng mỗi hộp nên quyết định mua thêm 3 hộp nữa.\nTìm đa thức biểu thị số tiền bà Khanh phải trả cho tổng số hộp sữa đã mua.",
            "method": "Số tiền = Số hộp sữa thực mua $\\times$ Giá tiền mỗi hộp thực tế.",
            "steps": [
                "**Bước 1 (Xác định các đại lượng):**\n- Số hộp sữa bà Khanh mua thực tế là: $x + 3$ (hộp).\n- Giá tiền mỗi hộp sữa sau khi giảm giá là: $y - 1\\ 500$ (đồng).",
                "**Bước 2 (Lập và khai triển tích):**\n$$\\begin{aligned} T &= (x + 3)(y - 1\\ 500) \\\\ &= xy - 1\\ 500x + 3y - 4\\ 500. \\end{aligned}$$"
            ],
            "conclusion": "Đa thức biểu thị số tiền là $xy - 1\\ 500x + 3y - 4\\ 500$ (đồng)."
        },
        {
            "id": "1.36",
            "title": "Bài 1.36 (Trang 26)",
            "problem": "a) Tìm đơn thức $B$ nếu $4x^3y^2 : B = -2xy$.\nb) Với đơn thức $B$ tìm được ở câu a, hãy tìm đơn thức $H$ để:\n$$(4x^3y^2 - 3x^2y^3) : B = -2xy + H.$$",
            "method": "Áp dụng quy tắc tìm số chia trong phép chia đơn thức và phép chia đa thức cho đơn thức.",
            "steps": [
                "**Bước 1 (Câu a - Tìm $B$):**\n$$B = (4x^3y^2) : (-2xy) = [4 : (-2)](x^3 : x)(y^2 : y) = -2x^2y.$$",
                "**Bước 2 (Câu b - Tìm $H$):**\nThực hiện phép chia vế trái với $B = -2x^2y$:\n$$\\begin{aligned} (4x^3y^2 - 3x^2y^3) : (-2x^2y) &= [4x^3y^2 : (-2x^2y)] + [-3x^2y^3 : (-2x^2y)] \\\\ &= -2xy + \\frac{3}{2}y^2. \\end{aligned}$$\nSo sánh với $-2xy + H$, suy ra $H = \\frac{3}{2}y^2$ (hoặc $1,5y^2$)."
            ],
            "conclusion": "a) $B = -2x^2y$.\nb) $H = \\frac{3}{2}y^2$."
        },
        {
            "id": "1.37",
            "title": "Bài 1.37 (Trang 26)",
            "problem": "a) Tìm đơn thức $C$ nếu $5xy^2 \\cdot C = 10x^3y^3$.\nb) Với đơn thức $C$ tìm được ở câu a, hãy tìm đơn thức $K$ sao cho:\n$$(K + 5xy^2) \\cdot C = 6x^4y + 10x^3y^3.$$",
            "method": "Tìm thừa số chưa biết: $C = \\text{Tích} : \\text{Thừa số đã biết}$. Khai triển vế trái để tìm $K$.",
            "steps": [
                "**Bước 1 (Câu a - Tìm $C$):**\n$$C = 10x^3y^3 : 5xy^2 = (10 : 5)(x^3 : x)(y^3 : y^2) = 2x^2y.$$",
                "**Bước 2 (Câu b - Tìm $K$):**\nThay $C = 2x^2y$ vào đẳng thức:\n$$(K + 5xy^2) \\cdot 2x^2y = 6x^4y + 10x^3y^3$$\n$$\\Leftrightarrow K \\cdot 2x^2y + 10x^3y^3 = 6x^4y + 10x^3y^3$$\n$$\\Leftrightarrow K \\cdot 2x^2y = 6x^4y$$\n$$\\Leftrightarrow K = 6x^4y : 2x^2y = (6 : 2)(x^4 : x^2)(y : y) = 3x^2.$$"
            ],
            "conclusion": "a) $C = 2x^2y$.\nb) $K = 3x^2$."
        },
        {
            "id": "1.38",
            "title": "Bài 1.38 (Trang 26)",
            "problem": "Chuyện rằng Rùa chạy đua với Thỏ. Thỏ chạy nhanh gấp 60 lần rùa, nhưng chỉ sau $t$ phút chạy, Thỏ đã dừng lại mặc dù chưa đến đích. Do mải chơi, Thỏ không biết rằng Rùa vẫn cần mẫn chạy liên tục trong $90t$ phút và đến đích trước Thỏ.\na) Gọi $v$ (m/phút) là vận tốc chạy của Rùa. Hãy viết các đơn thức biểu thị quãng đường mà Thỏ và Rùa đã chạy.\nb) Hỏi Rùa đã chạy được quãng đường dài gấp bao nhiêu lần quãng đường Thỏ đã chạy?",
            "method": "Công thức quãng đường: $s = v \\cdot t$. Lập tỉ số quãng đường của Rùa và Thỏ.",
            "steps": [
                "**Bước 1 (Câu a - Lập đơn thức quãng đường):**\n- Vận tốc của Rùa là $v$, thời gian chạy là $90t$.\n  $\\Rightarrow$ Quãng đường Rùa chạy: $s_{\\text{Rùa}} = v \\cdot 90t = 90vt$ (m).\n- Thỏ chạy nhanh gấp 60 lần Rùa nên vận tốc của Thỏ là $60v$. Thời gian chạy của Thỏ là $t$.\n  $\\Rightarrow$ Quãng đường Thỏ chạy: $s_{\\text{Thỏ}} = 60v \\cdot t = 60vt$ (m).",
                "**Bước 2 (Câu b - So sánh quãng đường):**\nTỉ số quãng đường giữa Rùa và Thỏ là:\n$$\\frac{s_{\\text{Rùa}}}{s_{\\text{Thỏ}}} = \\frac{90vt}{60vt} = \\frac{90}{60} = 1,5.$$"
            ],
            "conclusion": "a) Đơn thức quãng đường: $s_{\\text{Rùa}} = 90vt\\text{ (m)}$; $s_{\\text{Thỏ}} = 60vt\\text{ (m)}$.\nb) Quãng đường Rùa chạy gấp $1,5$ lần quãng đường Thỏ chạy."
        }
    ],
    "Bai_tap_cuoi_chuong_I.md": [
        {
            "id": "1.39",
            "title": "Bài 1.39 (Trắc nghiệm - Trang 27)",
            "problem": "Đơn thức $-2^3x^2yz^3$ có:\nA. hệ số $-2$, bậc 8.\nB. hệ số $-2^3$, bậc 5.\nC. hệ số $-1$, bậc 9.\nD. hệ số $-2^3$, bậc 6.",
            "method": "Hệ số là phần số (bao gồm cả dấu). Bậc là tổng số mũ của tất cả các biến.",
            "steps": [
                "**Bước 1:** Phần hệ số là $-2^3 = -8$.\n**Bước 2:** Các biến là $x, y, z$ với số mũ lần lượt là $2, 1, 3$. Tổng số mũ là $2 + 1 + 3 = 6$."
            ],
            "conclusion": "Chọn đáp án **D** (hệ số $-2^3$, bậc 6)."
        },
        {
            "id": "1.40",
            "title": "Bài 1.40 (Trắc nghiệm - Trang 27)",
            "problem": "Gọi $T$ là tổng, $H$ là hiệu của hai đa thức $3x^2y - 2xy^2 + xy$ và $-2x^2y + 3xy^2 + 1$. Khi đó:\nA. $T = x^2y - xy^2 + xy + 1$ và $H = 5x^2y - 5xy^2 + xy - 1$.\nB. $T = x^2y + xy^2 + xy + 1$ và $H = 5x^2y - 5xy^2 + xy - 1$.\nC. $T = x^2y + xy^2 + xy + 1$ và $H = 5x^2y - 5xy^2 - xy - 1$.\nD. $T = x^2y + xy^2 + xy - 1$ và $H = 5x^2y + 5xy^2 + xy - 1$.",
            "method": "Tính $T$ bằng phép cộng và $H$ bằng phép trừ, chú ý đổi dấu.",
            "steps": [
                "**Bước 1 (Tính tổng T):**\n$$T = (3x^2y - 2x^2y) + (-2xy^2 + 3xy^2) + xy + 1 = x^2y + xy^2 + xy + 1.$$",
                "**Bước 2 (Tính hiệu H):**\n$$H = (3x^2y + 2x^2y) + (-2xy^2 - 3xy^2) + xy - 1 = 5x^2y - 5xy^2 + xy - 1.$$"
            ],
            "conclusion": "Chọn đáp án **B**."
        },
        {
            "id": "1.41",
            "title": "Bài 1.41 (Trắc nghiệm - Trang 27)",
            "problem": "Tích của hai đơn thức $6x^2yz$ và $-2y^2z^2$ là đơn thức:\nA. $4x^2y^3z^3$.\nB. $-12x^2y^3z^3$.\nC. $-12x^3y^3z^3$.\nD. $4x^3y^3z^3$.",
            "method": "Nhân hệ số với hệ số, luỹ thừa cùng biến với nhau.",
            "steps": [
                "**Bước 1:** Hệ số: $6 \\cdot (-2) = -12$.\n**Bước 2:** Phần biến: $x^2 \\cdot (y \\cdot y^2) \\cdot (z \\cdot z^2) = x^2y^3z^3$."
            ],
            "conclusion": "Chọn đáp án **B** ($-12x^2y^3z^3$)."
        },
        {
            "id": "1.42",
            "title": "Bài 1.42 (Trắc nghiệm - Trang 27)",
            "problem": "Khi chia đa thức $8x^3y^2 - 6x^2y^3$ cho đơn thức $-2xy$, ta được kết quả là:\nA. $-4x^2y + 3xy^2$.\nB. $-4xy^2 + 3x^2y$.\nC. $-10x^2y + 4xy^2$.\nD. $-10x^2y + 4xy^2$.",
            "method": "Chia từng hạng tử cho $-2xy$.",
            "steps": [
                "**Bước 1:** $8x^3y^2 : (-2xy) = -4x^2y$.\n**Bước 2:** $-6x^2y^3 : (-2xy) = +3xy^2$."
            ],
            "conclusion": "Chọn đáp án **A** ($-4x^2y + 3xy^2$)."
        },
        {
            "id": "1.43",
            "title": "Bài 1.43 (Tự luận - Trang 27)",
            "problem": "Một đa thức hai biến bậc hai thu gọn có thể có nhiều nhất:\na) bao nhiêu hạng tử bậc hai? Cho ví dụ.\nb) bao nhiêu hạng tử bậc nhất? Cho ví dụ.\nc) bao nhiêu hạng tử khác 0? Cho ví dụ.",
            "method": "Xét hai biến $x$ và $y$:\n- Các hạng tử bậc hai có dạng: $x^2, xy, y^2$.\n- Các hạng tử bậc nhất có dạng: $x, y$.\n- Hạng tử bậc không (hằng số): $c$.",
            "steps": [
                "**Bước 1 (Câu a):**\nCác dạng đơn thức bậc hai của hai biến $x, y$ là: $x^2, xy, y^2$. Do đó có nhiều nhất **3 hạng tử bậc hai**.\nVí dụ: $2x^2 - 3xy + 5y^2$.",
                "**Bước 2 (Câu b):**\nCác dạng đơn thức bậc nhất của hai biến $x, y$ là: $x, y$. Do đó có nhiều nhất **2 hạng tử bậc nhất**.\nVí dụ: $4x - 7y$.",
                "**Bước 3 (Câu c):**\nTổng số hạng tử khác 0 nhiều nhất gồm: 3 hạng tử bậc hai + 2 hạng tử bậc nhất + 1 hạng tử tự do (hằng số) = **6 hạng tử**.\nVí dụ: $x^2 + 2xy + 3y^2 + 4x + 5y + 6$."
            ],
            "conclusion": "a) Nhiều nhất 3 hạng tử bậc hai.\nb) Nhiều nhất 2 hạng tử bậc nhất.\nc) Nhiều nhất 6 hạng tử khác 0."
        },
        {
            "id": "1.44",
            "title": "Bài 1.44 (Tự luận - Trang 27)",
            "problem": "Cho biểu thức $3x^3(x^5 - y^5) + y^5(3x^3 - y^3)$.\na) Rút gọn biểu thức đã cho.\nb) Tính giá trị của biểu thức đã cho nếu biết $y^4 = x^4\\sqrt{3}$.",
            "method": "Khai triển nhân đơn thức với đa thức, thu gọn biểu thức, sau đó biến đổi để sử dụng điều kiện $y^4 = x^4\\sqrt{3}$.",
            "steps": [
                "**Bước 1 (Câu a - Rút gọn):**\n$$\\begin{aligned} & 3x^3(x^5 - y^5) + y^5(3x^3 - y^3) \\\\ = & 3x^8 - 3x^3y^5 + 3x^3y^5 - y^8 \\\\ = & 3x^8 - y^8. \\end{aligned}$$",
                "**Bước 2 (Câu b - Tính giá trị):**\nTừ điều kiện $y^4 = x^4\\sqrt{3}$, bình phương hai vế:\n$$(y^4)^2 = (x^4\\sqrt{3})^2 \\Rightarrow y^8 = x^8 \\cdot 3 = 3x^8.$$\nThay $y^8 = 3x^8$ vào biểu thức rút gọn:\n$$3x^8 - y^8 = 3x^8 - 3x^8 = 0.$$"
            ],
            "conclusion": "a) Biểu thức rút gọn là $3x^8 - y^8$.\nb) Khi $y^4 = x^4\\sqrt{3}$, giá trị biểu thức luôn bằng $0$."
        },
        {
            "id": "1.45",
            "title": "Bài 1.45 (Tự luận - Trang 28)",
            "problem": "Rút gọn biểu thức:\n$$\\frac{1}{4}(2x^2 + y)(x - 2y^2) + \\frac{1}{4}(2x^2 - y)(x + 2y^2).$$",
            "method": "Đặt nhân tử chung $\\frac{1}{4}$ hoặc nhân phân phối từng cụm rồi cộng lại.",
            "steps": [
                "**Bước 1 (Khai triển cụm thứ nhất):**\n$$(2x^2 + y)(x - 2y^2) = 2x^3 - 4x^2y^2 + xy - 2y^3.$$",
                "**Bước 2 (Khai triển cụm thứ hai):**\n$$(2x^2 - y)(x + 2y^2) = 2x^3 + 4x^2y^2 - xy - 2y^3.$$",
                "**Bước 3 (Cộng hai cụm và nhân $\\frac{1}{4}$):**\n$$\\begin{aligned} & (2x^3 - 4x^2y^2 + xy - 2y^3) + (2x^3 + 4x^2y^2 - xy - 2y^3) \\\\ = & (2x^3 + 2x^3) + (-4x^2y^2 + 4x^2y^2) + (xy - xy) + (-2y^3 - 2y^3) \\\\ = & 4x^3 - 4y^3. \\end{aligned}$$\nNhân với $\\frac{1}{4}$:\n$$\\frac{1}{4}(4x^3 - 4y^3) = x^3 - y^3.$$"
            ],
            "conclusion": "Biểu thức rút gọn là $x^3 - y^3$."
        },
        {
            "id": "1.46",
            "title": "Bài 1.46 (Tự luận - Trang 28)",
            "problem": "Bạn Thành dùng một miếng bìa hình chữ nhật để làm một chiếc hộp (không nắp) bằng cách cắt bốn hình vuông cạnh $x\\text{ cm}$ ở bốn góc (H.1.3) rồi gấp lại. Biết rằng miếng bìa có chiều dài là $y\\text{ cm}$, chiều rộng là $z\\text{ cm}$.\nTìm đa thức (ba biến $x, y, z$) biểu thị thể tích của chiếc hộp. Xác định bậc của đa thức đó.",
            "method": "Chiếc hộp là hình hộp chữ nhật. Thể tích = chiều dài đáy $\\times$ chiều rộng đáy $\\times$ chiều cao.",
            "steps": [
                "**Bước 1 (Xác định kích thước chiếc hộp):**\n- Chiều cao chiếc hộp bằng cạnh hình vuông cắt đi: $h = x\\text{ (cm)}$.\n- Chiều dài đáy hộp: $d = y - 2x\\text{ (cm)}$.\n- Chiều rộng đáy hộp: $r = z - 2x\\text{ (cm)}$.",
                "**Bước 2 (Lập biểu thức thể tích):**\n$$\\begin{aligned} V &= x(y - 2x)(z - 2x) \\\\ &= x[yz - 2xy - 2xz + 4x^2] \\\\ &= xyz - 2x^2y - 2x^2z + 4x^3. \\end{aligned}$$",
                "**Bước 3 (Xác định bậc):**\n- Các hạng tử: $xyz$ (bậc 3), $-2x^2y$ (bậc 3), $-2x^2z$ (bậc 3), $4x^3$ (bậc 3).\n- Bậc của đa thức $V$ là 3."
            ],
            "conclusion": "Đa thức biểu thị thể tích hộp là $V = 4x^3 - 2x^2y - 2x^2z + xyz$. Đa thức này có bậc là 3."
        },
        {
            "id": "1.47",
            "title": "Bài 1.47 (Tự luận - Trang 28)",
            "problem": "Biết rằng $D$ là một đơn thức sao cho $-2x^3y^4 : D = xy^2$. Hãy tìm thương của phép chia:\n$$(10x^5y^2 - 6x^3y^4 + 8x^2y^5) : D.$$",
            "method": "Tìm đơn thức chia $D = (-2x^3y^4) : (xy^2)$, sau đó thực hiện phép chia đa thức cho $D$.",
            "steps": [
                "**Bước 1 (Tìm $D$):**\n$$D = (-2x^3y^4) : (xy^2) = [-2 : 1] \\cdot (x^3 : x) \\cdot (y^4 : y^2) = -2x^2y^2.$$",
                "**Bước 2 (Thực hiện phép chia đa thức cho $D$):**\n$$\\begin{aligned} & (10x^5y^2 - 6x^3y^4 + 8x^2y^5) : (-2x^2y^2) \\\\ = & [10x^5y^2 : (-2x^2y^2)] + [-6x^3y^4 : (-2x^2y^2)] + [8x^2y^5 : (-2x^2y^2)] \\\\ = & -5x^3 + 3xy^2 - 4y^3. \\end{aligned}$$"
            ],
            "conclusion": "Thương cần tìm là $-5x^3 + 3xy^2 - 4y^3$."
        },
        {
            "id": "1.48",
            "title": "Bài 1.48 (Tự luận - Trang 28)",
            "problem": "Làm phép chia sau theo hướng dẫn:\n$$[8x^3(2x - 5)^2 - 6x^2(2x - 5)^3 + 10x(2x - 5)^2] : 2x(2x - 5)^2.$$\nHướng dẫn: Đặt $y = 2x - 5$.",
            "method": "Đặt ẩn phụ $y = 2x - 5$, thực hiện phép chia đa thức hai biến $x, y$ cho đơn thức, rồi thay lại $y = 2x - 5$ và thu gọn.",
            "steps": [
                "**Bước 1 (Đặt ẩn phụ):**\nĐặt $y = 2x - 5$, phép chia trở thành:\n$$[8x^3y^2 - 6x^2y^3 + 10xy^2] : (2xy^2).$$",
                "**Bước 2 (Chia từng hạng tử):**\n$$\\begin{aligned} & (8x^3y^2 : 2xy^2) + (-6x^2y^3 : 2xy^2) + (10xy^2 : 2xy^2) \\\\ = & 4x^2 - 3xy + 5. \\end{aligned}$$",
                "**Bước 3 (Thay lại $y = 2x - 5$ và thu gọn):**\n$$\\begin{aligned} & 4x^2 - 3x(2x - 5) + 5 \\\\ = & 4x^2 - 6x^2 + 15x + 5 \\\\ = & -2x^2 + 15x + 5. \\end{aligned}$$"
            ],
            "conclusion": "Kết quả của phép chia là $-2x^2 + 15x + 5$."
        }
    ]
}

target_file = r"G:\My Drive\0_HOME\APP\TOAN LOP 8\Toan8-TuHoc\data\sgk_solutions.json"
with open(target_file, "w", encoding="utf-8") as f:
    json.dump(sgk_solutions, f, ensure_ascii=False, indent=2)

print(f"Generated {sum(len(v) for v in sgk_solutions.values())} SGK solutions across {len(sgk_solutions)} lessons!")

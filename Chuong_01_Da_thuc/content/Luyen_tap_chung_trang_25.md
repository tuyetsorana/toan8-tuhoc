<!-- SECTION: QUICK_NOTES -->
### 💡 Ghi Nhớ Cốt Lõi

> 📖 **Tổng Hợp Kiến Thức:**
> Phối hợp thành thạo các quy tắc nhân đơn thức, nhân đa thức và chia đa thức cho đơn thức; ứng dụng vào bài toán chứng minh biểu thức không phụ thuộc vào giá trị của biến.

---

#### 📐 Công Thức Trọng Tâm:

> **Dấu hiệu biểu thức không phụ thuộc vào biến:**
>
> $$\text{Biểu thức } P(x) \xrightarrow{\text{Rút gọn}} P(x) = C \quad (C \text{ là một hằng số, không còn chứa } x)$$
>
> ---
>
> **Thứ tự ưu tiên thực hiện phép tính:**
>
> $$\text{Trong ngoặc} \implies \text{Nhân & Chia} \implies \text{Cộng & Trừ}$$

---

#### ⚠️ Sai Lầm Thường Gặp Cần Tránh:

> - ❌ **Lỗi 1:** Bỏ sót dấu ngoặc trước biểu thức có dấu trừ dẫn đến sai dấu khi khai triển.
> - ❌ **Lỗi 2:** Không kiểm tra lại bậc của đa thức kết quả xem các hạng tử chứa biến đã triệt tiêu hết chưa.

<!-- SECTION: STEP_EXAMPLES -->
### 📝 Ví Dụ Mẫu Biến Đổi Từng Bước

#### 📌 Ví dụ: Chứng minh biểu thức không phụ thuộc vào biến
Chứng minh giá trị của biểu thức sau không phụ thuộc vào giá trị của biến $x$:
$$P = (2x - 1)(x + 3) - 2x(x + 1) - 3x$$

**🔍 Phương pháp tư duy:**
Khai triển tất cả các tích ra, sau đó nhóm các hạng tử đồng dạng để triệt tiêu các số hạng chứa biến $x^2$ và $x$.

**📝 Lời giải chi tiết:**
- **Bước 1 (Khai triển tích thứ nhất $(2x - 1)(x + 3)$):**
  $$(2x - 1)(x + 3) = 2x^2 + 6x - x - 3 = 2x^2 + 5x - 3$$
- **Bước 2 (Khai triển tích thứ hai $-2x(x + 1)$):**
  $$-2x(x + 1) = -2x^2 - 2x$$
- **Bước 3 (Thu gọn toàn bộ biểu thức $P$):**
  $$\begin{aligned}
  P &= (2x^2 + 5x - 3) + (-2x^2 - 2x) - 3x \\
    &= (2x^2 - 2x^2) + (5x - 2x - 3x) - 3 \\
    &= 0x^2 + 0x - 3 = -3
  \end{aligned}$$
- **Kết luận:** Vì $P = -3$ là hằng số (không còn chứa biến $x$), nên giá trị của biểu thức $P$ không phụ thuộc vào giá trị của biến $x$.

<!-- SECTION: SGK_CONTENT -->
# LUYỆN TẬP CHUNG (Trang 25)

## Ví dụ minh họa

**Ví dụ 1:**
Rút gọn biểu thức $T = (5xy - 4y^2)(3x^2 + 4xy) - 15xy(x + y)(x - y)$.  
Tìm đa thức $D$ sao cho $T : D = xy^2$.

**Giải:**
Ta có:
$$\begin{aligned}
T &= (5xy - 4y^2)(3x^2 + 4xy) - 15xy(x + y)(x - y) \\
  &= 5xy \cdot 3x^2 + 5xy \cdot 4xy + (-4y^2) \cdot 3x^2 + (-4y^2) \cdot 4xy - 15xy(x^2 - xy + xy - y^2) \\
  &= 15x^3y + 20x^2y^2 - 12x^2y^2 - 16xy^3 - 15xy(x^2 - y^2) \\
  &= 15x^3y + 20x^2y^2 - 12x^2y^2 - 16xy^3 - 15x^3y + 15xy^3 \\
  &= (15x^3y - 15x^3y) + (20x^2y^2 - 12x^2y^2) - (16xy^3 - 15xy^3) \\
  &= 8x^2y^2 - xy^3.
\end{aligned}$$

Đẳng thức $T : D = xy^2$ cũng có nghĩa là $T : xy^2 = D$, suy ra:
$$D = (8x^2y^2 - xy^3) : xy^2 = 8x - y.$$

**Ví dụ 2:**
Cho đa thức $A = 2x^2y^2 - 5xy^3$ và đơn thức $B = 3x^my^2$ (với $m \in \mathbb{N}$).  
a) Tìm số nguyên dương $m$ sao cho đa thức $A$ chia hết cho đơn thức $B$.  
b) Với giá trị tìm được của $m$ ở câu a, hãy thực hiện phép chia $A : B$.

**Giải:**  
a) Để mọi hạng tử của đa thức $A$ đều chia hết cho $B$, ta cần có:  
Số mũ của $x$ trong $B$ nhỏ hơn hoặc bằng số mũ của $x$ trong mọi hạng tử của $A$; tức là phải có $m \le 2$ và $m \le 1$.  
Số nguyên dương $m$ duy nhất thoả mãn điều này là $m = 1$.  
b) Khi $m = 1$, ta có $B = 3xy^2$ và phép chia $A : B$ trở thành:
$$(2x^2y^2 - 5xy^3) : 3xy^2 = \frac{2}{3}x - \frac{5}{3}y.$$

---

## BÀI TẬP

**1.33.** Cho biểu thức $P = 5x(3x^2y - 2xy^2 + 1) - 3xy(5x^2 - 3xy) + x^2y^2$.  
a) Bằng cách thu gọn, chứng tỏ rằng giá trị của biểu thức $P$ chỉ phụ thuộc vào biến $x$ mà không phụ thuộc vào biến $y$.  
b) Tìm giá trị của $x$ sao cho $P = 10$.

**1.34.** Rút gọn biểu thức:
$$(3x^2 - 5xy - 4y^2) \cdot (2x^2 + y^2) + (2x^4y - x^3y^3 - x^2y^4) : \left(\frac{1}{5}xy\right).$$

**1.35.** Bà Khanh dự định mua $x$ hộp sữa, mỗi hộp giá $y$ đồng. Nhưng khi đến cửa hàng, bà Khanh thấy giá sữa đã giảm $1\ 500$ đồng mỗi hộp nên quyết định mua thêm 3 hộp nữa.  
Tìm đa thức biểu thị số tiền bà Khanh phải trả cho tổng số hộp sữa đã mua.

**1.36.**  
a) Tìm đơn thức $B$ nếu $4x^3y^2 : B = -2xy$.  
b) Với đơn thức $B$ tìm được ở câu a, hãy tìm đơn thức $H$ để:
$$(4x^3y^2 - 3x^2y^3) : B = -2xy + H.$$

**1.37.**  
a) Tìm đơn thức $C$ nếu $5xy^2 \cdot C = 10x^3y^3$.  
b) Với đơn thức $C$ tìm được ở câu a, hãy tìm đơn thức $K$ sao cho:
$$(K + 5xy^2) \cdot C = 6x^4y + 10x^3y^3.$$

**1.38.** Chuyện rằng Rùa chạy đua với Thỏ. Thỏ chạy nhanh gấp 60 lần rùa, nhưng chỉ sau $t$ phút chạy, Thỏ đã dừng lại mặc dù chưa đến đích. Do mải chơi, Thỏ không biết rằng Rùa vẫn cần mẫn chạy liên tục trong $90t$ phút và đến đích trước Thỏ.  
a) Gọi $v$ (m/phút) là vận tốc chạy của Rùa. Hãy viết các đơn thức biểu thị quãng đường mà Thỏ và Rùa đã chạy.  
b) Hỏi Rùa đã chạy được quãng đường dài gấp bao nhiêu lần quãng đường Thỏ đã chạy?

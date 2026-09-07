<!-- SECTION: QUICK_NOTES -->
<div class="callout-note">
<strong>💡 Định Nghĩa Cô Đọng:</strong><br>
• <strong>Nhân đơn thức với đa thức:</strong> Nhân đơn thức với từng hạng tử của đa thức rồi cộng các tích lại.<br>
• <strong>Nhân đa thức với đa thức:</strong> Lấy mỗi hạng tử của đa thức này nhân lần lượt với từng hạng tử của đa thức kia rồi cộng các kết quả lại.
</div>

#### 📐 Công Thức Trọng Tâm:
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-left: 5px solid #2563eb; border-radius: 8px; padding: 1rem; margin: 1rem 0;">
• <strong>Đơn thức $\times$ Đa thức:</strong>
  $$A(B + C) = A \cdot B + A \cdot C$$
• <strong>Đa thức $\times$ Đa thức:</strong>
  $$(A + B)(C + D) = A \cdot C + A \cdot D + B \cdot C + B \cdot D$$
• <strong>Nhân luỹ thừa cùng cơ số:</strong>
  $$x^m \cdot x^n = x^{m+n} \quad \text{(Cộng số mũ, không phải nhân số mũ!)}$$
</div>

<div class="callout-tip">
<strong>⚠️ Sai Lầm Thường Gặp Cần Tránh:</strong><br>
❌ <strong>Lỗi 1:</strong> Nhân số mũ: $x^2 \cdot x^3 = x^6$ (SAI) ➔ Đúng phải là $x^{2+3} = x^5$.<br>
❌ <strong>Lỗi 2:</strong> Bỏ sót hạng tử: $(A+B)(C+D)$ phải sinh ra đủ 4 tích trước khi thu gọn.<br>
❌ <strong>Lỗi 3:</strong> Quên quy tắc dấu: $(-a) \cdot (-b) = +ab$; $(-a) \cdot b = -ab$.
</div>

<!-- SECTION: STEP_EXAMPLES -->
### 📝 Ví Dụ Mẫu Biến Đổi Từng Bước

#### 📌 Ví dụ 1: Nhân đơn thức với đa thức
Thực hiện phép tính: $$P = 2xy(3x^2 - xy + 4y^2)$$

<div class="example-card">
<strong>🔍 Phương pháp tư duy:</strong> Lấy $2xy$ nhân lần lượt với $3x^2$, $-xy$ và $+4y^2$.<br><br>
<strong>📝 Lời giải chi tiết:</strong><br>
• <strong>Bước 1 (Áp dụng tính chất phân phối):</strong>
  $$P = (2xy) \cdot (3x^2) + (2xy) \cdot (-xy) + (2xy) \cdot (4y^2)$$
• <strong>Bước 2 (Nhân hệ số với hệ số, biến với biến):</strong>
  $$P = (2 \cdot 3)(x \cdot x^2)y + [2 \cdot (-1)](x \cdot x)(y \cdot y) + (2 \cdot 4)x(y \cdot y^2)$$
• <strong>Bước 3 (Thu gọn các luỹ thừa):</strong>
  $$P = 6x^3y - 2x^2y^2 + 8xy^3$$
• <strong>Kết luận:</strong> Tích là <strong>$6x^3y - 2x^2y^2 + 8xy^3$</strong>.
</div>

#### 📌 Ví dụ 2: Nhân hai đa thức và rút gọn
Rút gọn biểu thức: $$Q = (2x - y)(x + 3y) - 2x^2$$

<div class="example-card">
<strong>🔍 Phương pháp tư duy:</strong> Khai triển tích $(2x - y)(x + 3y)$ ra 4 hạng tử rồi trừ $2x^2$ và thu gọn.<br><br>
<strong>📝 Lời giải chi tiết:</strong><br>
• <strong>Bước 1 (Nhân đa thức với đa thức):</strong>
  $$(2x - y)(x + 3y) = 2x \cdot x + 2x \cdot 3y - y \cdot x - y \cdot 3y = 2x^2 + 6xy - xy - 3y^2$$
• <strong>Bước 2 (Thu gọn tích vừa nhân):</strong>
  $$2x^2 + 5xy - 3y^2$$
• <strong>Bước 3 (Trừ $2x^2$ của đề bài):</strong>
  $$Q = (2x^2 + 5xy - 3y^2) - 2x^2 = (2x^2 - 2x^2) + 5xy - 3y^2 = 5xy - 3y^2$$
• <strong>Kết luận:</strong> Biểu thức thu gọn là <strong>$5xy - 3y^2$</strong>.
</div>

<!-- SECTION: SGK_CONTENT -->
# BÀI 4. PHÉP NHÂN ĐA THỨC

| Khái niệm, thuật ngữ | Kiến thức, kĩ năng |
|---|---|
| Tích hai đa thức | - Thực hiện phép tính nhân đơn thức với đa thức và nhân đa thức với đa thức.<br>- Biến đổi, thu gọn biểu thức đại số có sử dụng phép nhân đa thức. |

---

## Tình huống mở đầu

Giả sử độ dài hai cạnh của một hình chữ nhật được biểu thị bởi $M = x + 3y + 2$ và $N = x + y$. Khi đó, diện tích của hình chữ nhật được biểu thị bởi:
$$MN = (x + 3y + 2)(x + y).$$

Trong tình huống này, ta phải nhân hai đa thức $M$ và $N$. Phép nhân đó được thực hiện như thế nào và kết quả có phải là một đa thức hay không? Bài học này sẽ cho các em câu trả lời cho các câu hỏi đó.

---

## 1. Nhân đơn thức với đa thức

### Nhân hai đơn thức

Để nhân hai đơn thức $8x^2yz$ và $-\frac{1}{4}xy$, ta làm như sau:
$$8x^2yz \cdot \left(-\frac{1}{4}xy\right) = 8 \cdot \left(-\frac{1}{4}\right) \cdot (x^2yz)(xy) = (-2) \cdot x^3y^2z = -2x^3y^2z.$$

Qua ví dụ trên, ta có thể nói:

> [!NOTE]
> **Muốn nhân hai đơn thức**, ta nhân hai hệ số với nhau và nhân hai phần biến với nhau.

**Ví dụ 1:**
Thực hiện phép nhân $\left(-\frac{1}{3}xy^3\right) \cdot (9x^2yz)$.

**Giải:**
$$\left(-\frac{1}{3}xy^3\right) \cdot (9x^2yz) = \left(-\frac{1}{3} \cdot 9\right) \cdot (xy^3)(x^2yz) = -3x^3y^4z.$$

**Luyện tập 1:**
Nhân hai đơn thức:
a) $3x^2$ và $2x^3$;  
b) $-xy$ và $4z^3$;  
c) $6xy^3$ và $-0,5x^2$.

---

### Nhân đơn thức với đa thức

**HĐ1:** Hãy nhớ lại quy tắc nhân đơn thức với đa thức trong trường hợp chúng có một biến bằng cách thực hiện phép nhân $(5x^2) \cdot (3x^2 - x - 4)$.

**HĐ2:** Bằng cách tương tự, hãy làm phép nhân $(5x^2y) \cdot (3x^2y - xy - 4y)$.

Ta rút ra quy tắc sau:

> [!NOTE]
> **Muốn nhân một đơn thức với một đa thức**, ta nhân đơn thức với từng hạng tử của đa thức rồi cộng các tích với nhau.

*(Tích của một đơn thức với một đa thức cũng là một đa thức).*

**Ví dụ 2:**
Thực hiện phép nhân: $(-4xy) \cdot (2x^2 + xy - y^2)$.

**Giải:**
$$\begin{aligned}
(-4xy) \cdot (2x^2 + xy - y^2) &= (-4xy)(2x^2) + (-4xy)(xy) + (-4xy)(-y^2) \\
                               &= (-4) \cdot 2(xy)x^2 - 4(xy)(xy) + 4(xy)y^2 \\
                               &= -8x^3y - 4x^2y^2 + 4xy^3.
\end{aligned}$$

**Luyện tập 2:**
Làm tính nhân:
a) $(xy) \cdot (x^2 + xy - y^2)$;  
b) $(xy + yz + zx) \cdot (-xyz)$.

**Vận dụng:**
Rút gọn biểu thức: $x^3(x + y) - x(x^3 + y^3)$.

---

## 2. Nhân đa thức với đa thức

### Nhân hai đa thức

**HĐ3:** Hãy nhớ lại quy tắc nhân hai đa thức một biến bằng cách thực hiện phép nhân:
$$(2x + 3) \cdot (x^2 - 5x + 4).$$

**HĐ4:** Bằng cách tương tự, hãy thử làm phép nhân $(2x + 3y) \cdot (x^2 - 5xy + 4y^2)$.

Ta rút ra quy tắc *nhân hai đa thức* như sau:

> [!NOTE]
> **Muốn nhân một đa thức với một đa thức**, ta nhân mỗi hạng tử của đa thức này với từng hạng tử của đa thức kia rồi cộng các tích với nhau.

> [!TIP]
> **Chú ý:**
> - Phép nhân đa thức cũng có các tính chất tương tự phép nhân các số như:
>   - $A \cdot B = B \cdot A$ (giao hoán);
>   - $(A \cdot B) \cdot C = A \cdot (B \cdot C)$ (kết hợp);
>   - $A \cdot (B + C) = A \cdot B + A \cdot C$ (phân phối đối với phép cộng).
> - Nếu $A, B, C$ là những đa thức tuỳ ý thì $A \cdot B \cdot C = (A \cdot B) \cdot C = A \cdot (B \cdot C)$.

**Ví dụ 3:**
Trở lại *tình huống mở đầu*, ta thực hiện phép nhân như sau:
$$\begin{aligned}
(x + 3y + 2)(x + y) &= x^2 + xy + 3xy + 3y^2 + 2x + 2y \\
                    &= x^2 + 4xy + 3y^2 + 2x + 2y.
\end{aligned}$$
Ta thấy kết quả cũng là một đa thức. *(Tích của hai đa thức cũng là một đa thức).*

**Ví dụ 4:**
Rút gọn biểu thức: $(x + y)(2x - y) - (x - y)(2x + y)$.

**Giải:**
Biểu thức đã cho có dạng $A - B$, trong đó $A = (x + y)(2x - y)$ và $B = (x - y)(2x + y)$.  
Ta rút gọn riêng từng biểu thức $A$ và $B$:
- $A = (x + y)(2x - y) = 2x^2 - xy + 2xy - y^2 = 2x^2 + xy - y^2$;
- $B = (x - y)(2x + y) = 2x^2 + xy - 2xy - y^2 = 2x^2 - xy - y^2$.

Từ đó ta có:
$$\begin{aligned}
(x + y)(2x - y) - (x - y)(2x + y) &= A - B \\
                                  &= (2x^2 + xy - y^2) - (2x^2 - xy - y^2) \\
                                  &= 2x^2 + xy - y^2 - 2x^2 + xy + y^2 = 2xy.
\end{aligned}$$

**Luyện tập 3:**
Thực hiện phép nhân:
a) $(2x + y)(4x^2 - 2xy + y^2)$;  
b) $(x^2y^2 - 3)(3 + x^2y^2)$.

**Thử thách nhỏ:**
Xét biểu thức đại số với hai biến $k$ và $m$ sau:
$$P = (2k - 3)(3m - 2) - (3k - 2)(2m - 3).$$
a) Rút gọn biểu thức $P$.  
b) Chứng minh rằng tại mọi giá trị nguyên của $k$ và $m$, giá trị của biểu thức $P$ luôn là một số nguyên chia hết cho 5.  
*(Gợi ý: Hãy viết $P$ dưới dạng $P = 5n$, trong đó $n$ là một số nguyên nào đó).*

---

## BÀI TẬP

**1.24.** Nhân hai đơn thức:
a) $5x^2y$ và $2xy^2$;  
b) $\frac{3}{4}xy$ và $8x^3y^2$;  
c) $1,5xy^2z^3$ và $2x^3y^2z$.

**1.25.** Tìm tích của đơn thức với đa thức:
a) $(-0,5)xy^2(2xy - x^2 + 4y)$;  
b) $\left(x^3y - \frac{1}{2}x^2 + \frac{1}{3}xy\right)6xy^3$.

**1.26.** Rút gọn biểu thức:
$$x(x^2 - y) - x^2(x + y) + xy(x - 1).$$

**1.27.** Làm tính nhân:
a) $(x^2 - xy + 1)(xy + 3)$;  
b) $\left(x^2y^2 - \frac{1}{2}xy + 2\right)(x - 2y)$.

**1.28.** Rút gọn biểu thức sau để thấy rằng giá trị của nó không phụ thuộc vào giá trị của biến:
$$(x - 5)(2x + 3) - 2x(x - 3) + x + 7.$$

**1.29.** Chứng minh đẳng thức sau:
$$(2x + y)(2x^2 + xy - y^2) = (2x - y)(2x^2 + 3xy + y^2).$$

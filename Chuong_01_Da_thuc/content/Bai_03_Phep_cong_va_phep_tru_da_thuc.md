<!-- SECTION: QUICK_NOTES -->
<div class="callout-note">
<strong>💡 Định Nghĩa Cô Đọng:</strong><br>
Muốn cộng hay trừ hai đa thức, ta viết chúng trong dấu ngoặc, dùng quy tắc phá ngoặc, sau đó nhóm các hạng tử đồng dạng lại rồi thu gọn.
</div>

#### 📐 Công Thức Trọng Tâm:
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-left: 5px solid #2563eb; border-radius: 8px; padding: 1rem; margin: 1rem 0;">
• <strong>Quy tắc bỏ dấu ngoặc:</strong>
  - Trước dấu ngoặc có dấu <strong>$+$</strong>: Giữ nguyên dấu tất cả các hạng tử:
    $$(A + B - C) = A + B - C$$
  - Trước dấu ngoặc có dấu <strong>$-$</strong>: Đổi dấu TẤT CẢ các hạng tử bên trong:
    $$-(A + B - C) = -A - B + C$$
• <strong>Phép tính tổng hiệu:</strong>
  $$P \pm Q = (\text{Biểu thức } P) \pm (\text{Biểu thức } Q)$$
</div>

<div class="callout-tip">
<strong>⚠️ Sai Lầm Thường Gặp Cần Tránh:</strong><br>
❌ <strong>Lỗi kinh điển:</strong> Khi trừ đa thức, chỉ đổi dấu hạng tử đầu tiên mà quên đổi dấu các hạng tử đằng sau!<br>
<em>Ví dụ sai:</em> $-(x^2 - 2xy + y^2) = -x^2 - 2xy + y^2$ (SAI HOÀN TOÀN).<br>
<em>Cách sửa đúng:</em> $-(x^2 - 2xy + y^2) = -x^2 + 2xy - y^2$.
</div>

<!-- SECTION: STEP_EXAMPLES -->
### 📝 Ví Dụ Mẫu Biến Đổi Từng Bước

#### 📌 Ví dụ 1: Tính tổng và hiệu của hai đa thức nhiều biến
Cho hai đa thức:
$$P = 3x^2 - 2xy + y^2 \quad \text{và} \quad Q = x^2 + 2xy - 3y^2$$
Tính $P + Q$ và $P - Q$.

<div class="example-card">
<strong>🔍 Phương pháp tư duy:</strong> Đặt hai đa thức vào ngoặc. Với $P - Q$, chú ý đổi dấu toàn bộ các hạng tử của $Q$ khi bỏ ngoặc.<br><br>
<strong>📝 Lời giải chi tiết:</strong><br>
• <strong>Bước 1 (Tính tổng $P + Q$):</strong>
  $$\begin{aligned}
  P + Q &= (3x^2 - 2xy + y^2) + (x^2 + 2xy - 3y^2) \\
        &= (3x^2 + x^2) + (-2xy + 2xy) + (y^2 - 3y^2) \\
        &= 4x^2 + 0 - 2y^2 = 4x^2 - 2y^2
  \end{aligned}$$
• <strong>Bước 2 (Tính hiệu $P - Q$ - Đổi dấu ngoặc thứ hai):</strong>
  $$\begin{aligned}
  P - Q &= (3x^2 - 2xy + y^2) - (x^2 + 2xy - 3y^2) \\
        &= 3x^2 - 2xy + y^2 - x^2 - 2xy + 3y^2 \\
        &= (3x^2 - x^2) + (-2xy - 2xy) + (y^2 + 3y^2) \\
        &= 2x^2 - 4xy + 4y^2
  \end{aligned}$$
• <strong>Kết luận:</strong> $P + Q = <strong>4x^2 - 2y^2</strong>$ và $P - Q = <strong>2x^2 - 4xy + 4y^2</strong>$.
</div>

<!-- SECTION: SGK_CONTENT -->
# BÀI 3. PHÉP CỘNG VÀ PHÉP TRỪ ĐA THỨC

| Khái niệm, thuật ngữ | Kiến thức, kĩ năng |
|---|---|
| - Tổng của hai đa thức<br>- Hiệu của hai đa thức | Thực hiện các phép tính cộng, trừ đa thức. |

---

## Tình huống mở đầu

Trong buổi sinh hoạt câu lạc bộ Toán học của lớp, hai bạn tính giá trị của hai đa thức:
$$P = 2x^2y - xy^2 + 22 \quad \text{và} \quad Q = xy^2 - 2x^2y + 23$$
tại những giá trị cho trước của $x$ và $y$. Kết quả được ghi lại như bảng bên.

**Bảng 1.1**

| $x$ | $1$ | $-1$ | $2$ | $1$ |
|:---:|:---:|:---:|:---:|:---:|
| $y$ | $-1$ | $1$ | $1$ | $2$ |
| $P$ | $19$ | $25$ | $38$ | $22$ |
| $Q$ | $26$ | $20$ | $17$ | $23$ |

Ban giám khảo cho biết có một cột cho kết quả sai.
*Theo em, làm thế nào để có thể nhanh chóng phát hiện cột có kết quả sai ấy?*

---

## Cộng và trừ hai đa thức

Cho hai đa thức:
$$A = 5x^2y + 5x - 3 \quad \text{và} \quad B = xy - 4x^2y + 5x - 1.$$

*(Bạn còn nhớ quy tắc dấu ngoặc không?)*

**HĐ1:** Thực hiện phép cộng hai đa thức $A$ và $B$ bằng cách tiến hành các bước sau:
- Lập tổng $A + B = (5x^2y + 5x - 3) + (xy - 4x^2y + 5x - 1)$.
- Bỏ dấu ngoặc và thu gọn đa thức nhận được.

**HĐ2:** Thực hiện phép trừ hai đa thức $A$ và $B$ bằng cách lập hiệu:
$$A - B = (5x^2y + 5x - 3) - (xy - 4x^2y + 5x - 1),$$
bỏ dấu ngoặc rồi thu gọn đa thức nhận được.

> [!NOTE]
> **Cộng (hay trừ) hai đa thức** tức là thu gọn đa thức nhận được sau khi nối hai đa thức đã cho bởi dấu "$+$" (hay dấu "$-$").

> [!TIP]
> **Chú ý:**
> - Phép cộng đa thức cũng có các tính chất giao hoán và kết hợp tương tự như phép cộng các số.
> - Với $A, B, C$ là những đa thức tuỳ ý, ta có:
>   $$A + B + C = (A + B) + C = A + (B + C);$$
>   $$\text{Nếu } A - B = C \text{ thì } A = B + C; \text{ ngược lại, nếu } A = B + C \text{ thì } A - B = C.$$

**Ví dụ:**
Tìm tổng và hiệu của hai đa thức:
$$C = 5x^2y + 5x - 3z + 2 \quad \text{và} \quad D = xyz - 4x^2y + 5x - 1.$$

**Giải:**
$$\begin{aligned}
C + D &= (5x^2y + 5x - 3z + 2) + (xyz - 4x^2y + 5x - 1) \\
      &= 5x^2y + 5x - 3z + 2 + xyz - 4x^2y + 5x - 1 \\
      &= (5x^2y - 4x^2y) + (5x + 5x) - 3z + xyz + (2 - 1) \\
      &= x^2y + 10x - 3z + xyz + 1.
\end{aligned}$$

$$\begin{aligned}
C - D &= (5x^2y + 5x - 3z + 2) - (xyz - 4x^2y + 5x - 1) \\
      &= 5x^2y + 5x - 3z + 2 - xyz + 4x^2y - 5x + 1 \\
      &= (5x^2y + 4x^2y) + (5x - 5x) - xyz - 3z + (2 + 1) \\
      &= 9x^2y - xyz - 3z + 3.
\end{aligned}$$

**Luyện tập 1:**
Cho hai đa thức $G = x^2y - 3xy - 3$ và $H = 3x^2y + xy - 0,5x + 5$.
Hãy tính $G + H$ và $G - H$.

**Luyện tập 2:**
Rút gọn và tính giá trị của biểu thức sau tại $x = 2$ và $y = -1$:
$$K = (x^2y + 2xy^3) - (7,5x^3y^2 - x^3) + (3xy^3 - x^2y + 7,5x^3y^2).$$

**Vận dụng:**
Trở lại *tình huống mở đầu*, hãy trình bày ý kiến của em.
*(Gợi ý: Hãy chú ý đến đa thức $P + Q$.)*

---

## BÀI TẬP

**1.14.** Tính tổng và hiệu của hai đa thức:
$$P = x^2y + x^3 - xy^2 + 3 \quad \text{và} \quad Q = x^3 + xy^2 - xy - 6.$$

**1.15.** Rút gọn biểu thức:
a) $(x - y) + (y - z) + (z - x)$;
b) $(2x - 3y) + (2y - 3z) + (2z - 3x)$.

**1.16.** Tìm đa thức $M$ biết:
$$M - 5x^2 + xyz = xy + 2x^2 - 3xyz + 5.$$

**1.17.** Cho hai đa thức $A = 2x^2y + 3xyz - 2x + 5$ và $B = 3xyz - 2x^2y + x - 4$.
a) Tìm các đa thức $A + B$ và $A - B$;
b) Tính giá trị của các đa thức $A$ và $A + B$ tại $x = 0,5; y = -2$ và $z = 1$.

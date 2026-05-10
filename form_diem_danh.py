import tkinter as tk

root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x250")

# CHUẨN: Cột 1 (Ô nhập) sẽ co giãn, cột 0 (Nhãn) giữ nguyên
root.columnconfigure(1, weight=1)

# --- Hàng 0 ---
nhan_ma_sv = tk.Label(root, text="Mã sinh viên:")
nhan_ma_sv.grid(row=0, column=0, padx=10, pady=10, sticky="w")

o_nhap_ma_sv = tk.Entry(root)
# sticky="ew" giúp ô nhập kéo dài hết chiều rộng cột 1
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# --- Hàng 1 ---
nhan_ho_ten = tk.Label(root, text="Họ và tên:")
nhan_ho_ten.grid(row=1, column=0, padx=10, pady=10, sticky="w")

o_nhap_ho_ten = tk.Entry(root)
# Thêm sticky="ew" ở đây để đồng bộ với ô phía trên
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# --- Hàng 2: Nút bấm ---
# Columnspan=2 giúp nút bấm chiếm không gian của cả nhãn và ô nhập
nut_luu = tk.Button(root, text="Lưu thông tin", bg="#007bff", fg="white", width=15)
nut_luu.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()


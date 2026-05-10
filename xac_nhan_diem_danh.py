import tkinter as tk
from tkinter import messagebox  # Yêu cầu 4: Popup thông báo
from datetime import datetime     # Yêu cầu 3: Thời gian thực

def xu_ly_du_lieu():
    # Lấy dữ liệu từ Entry
    mssv = o_nhap_ma_sv.get()
    ho_ten = o_nhap_ho_ten.get()
    
    # Lấy thời gian hiện tại - Yêu cầu 3
    thoi_gian_hien_tai = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
    
    # --- BẮT ĐẦU KIỂM TRA DỮ LIỆU (VALIDATION) ---
    
    # Kiểm tra trống thông tin
    if ho_ten == "" or mssv == "":
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng không để trống thông tin!") # Yêu cầu 4
        return 

    # Kiểm tra MSSV phải là số - Yêu cầu 2
    if not mssv.isdigit():
        messagebox.showerror("Lỗi định dạng", "MSSV phải là ký tự số!") # Yêu cầu 4
        # Xóa riêng ô MSSV để người dùng nhập lại - Yêu cầu 1
        o_nhap_ma_sv.delete(0, tk.END)
        return

    # --- NẾU DỮ LIỆU HỢP LỆ ---

    # 1. In ra Terminal kèm thời gian - Yêu cầu 3
    print(f"[{thoi_gian_hien_tai}] MSSV: {mssv} | Họ tên: {ho_ten} -> Thành công")
    
    # 2. Hiện Popup thông báo thành công - Yêu cầu 4
    messagebox.showinfo("Thành công", f"Đã điểm danh sinh viên: {ho_ten}")
    
    # 3. Cập nhật Label kết quả (giữ lại tính năng cũ của bạn)
    nhan_ket_qua.config(text=f"Vừa điểm danh: {ho_ten}", fg="green")
    
    # 4. Xóa trắng cả 2 ô nhập liệu sau khi thành công - Yêu cầu 1
    o_nhap_ma_sv.delete(0, tk.END)
    o_nhap_ho_ten.delete(0, tk.END)
    
    # Đưa con trỏ chuột về lại ô MSSV để tiện nhập tiếp
    o_nhap_ma_sv.focus_set()

# --- PHẦN GIAO DIỆN (GIỮ NGUYÊN CẤU TRÚC CỦA BẠN) ---
root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x350")
root.columnconfigure(1, weight=1)

tk.Label(root, text="Mã sinh viên:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_ma_sv = tk.Entry(root)
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Họ và tên:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_ho_ten = tk.Entry(root)
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

nut_xac_nhan = tk.Button(root, text="Xác nhận điểm danh", command=xu_ly_du_lieu, bg="#e1e1e1")
nut_xac_nhan.grid(row=2, column=0, columnspan=2, pady=10)

nhan_ket_qua = tk.Label(root, text="Sẵn sàng điểm danh", font=("Arial", 10, "italic"))
nhan_ket_qua.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()

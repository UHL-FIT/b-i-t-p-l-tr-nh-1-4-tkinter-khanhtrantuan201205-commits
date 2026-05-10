import tkinter as tk
root = tk.Tk()
root.title("The sinh vien so ")
root.geometry("400x300")
root.configure(bg="#f8f9fa")

nhan_truong = tk.Label(
    root,
    text="Truong dai hoc ha long",
    font=("Arial",14,"bold"),
    fg="White",
    bg="#0056b3"
)
nhan_truong.pack(fill="x", pady=10)

nhan_khoa = tk.Label(
    root,
    text= "Khoa cong nghe thong tin",
    font=("Arial",14,"bold"),
    fg="green",
    bg="#f8f9fa"
)
nhan_khoa.pack(pady=5)


nhan_ten = tk.Label(root,text="Ho ten: Nguyen Van A",font=("Arial",12))
nhan_ten.pack(pady=5)
nhan_msv = tk.Label(root, text="MSSV: 22010001", font=("Arial", 12), fg="red")
nhan_msv.pack(pady=5)
nut_thoat = tk.Button(
    root, 
    text="Đóng ứng dụng", 
    command=root.destroy, 
    bg="#dc3545", # Màu đỏ cảnh báo
    fg="white",
    font=("Arial",12,"bold"),
    width=20,
    height=2
)
nut_thoat.pack(pady=20)

root.mainloop()

def main():
    danh_sach = []
    print("=" * 45)
    print("       ỨNG DỤNG TO-DO LIST")
    print("=" * 45)
    print("Nhập các công việc cần làm (gõ 'xong' để kết thúc):\n")
 
    while True:
        cong_viec = input(f"  Công việc {len(danh_sach) + 1}: ").strip()
        if cong_viec.lower() == "xong":
            break
        if cong_viec:
            danh_sach.append(cong_viec)
 
    if not danh_sach:
        print("\n⚠  Bạn chưa nhập công việc nào.")
        return
 
    # Hiển thị danh sách ra màn hình
    print("\n" + "=" * 45)
    print("  DANH SÁCH CÔNG VIỆC HÔM NAY:")
    print("=" * 45)
    for i, cv in enumerate(danh_sach, start=1):
        print(f"  {i}. {cv}")
    print("=" * 45)
 
    # Ghi đè toàn bộ danh sách vào file todo_list.txt
    with open("todo_list.txt", "w", encoding="utf-8") as f:
        f.write("DANH SÁCH CÔNG VIỆC HÔM NAY\n")
        f.write("=" * 35 + "\n")
        for i, cv in enumerate(danh_sach, start=1):
            f.write(f"{i}. {cv}\n")
 
    print(f"\n  Đã lưu {len(danh_sach)} công việc vào file 'todo_list.txt'.")
 
if __name__ == "__main__":
    main()
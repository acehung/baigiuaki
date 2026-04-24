import random
import time
import datetime
 
DANH_SACH_TU = ["python", "apple", "river", "luong", "minh", "hung"]
GIOI_HAN_SAI = 5
 
def tao_hien_thi(tu_bi_mat, da_doan_dung):
    """Tạo chuỗi hiển thị với dấu gạch ngang và chữ đã đoán đúng."""
    return " ".join([ch if ch in da_doan_dung else "_" for ch in tu_bi_mat])
 
def ghi_ket_qua(tu_bi_mat, thang, thoi_gian, luot_sai_con_lai):
    """Ghi kết quả vào file hangman_result.txt."""
    with open("hangman_result.txt", "w", encoding="utf-8") as f:
        f.write("KẾT QUẢ TRÒ CHƠI MINI HANGMAN\n")
        f.write("=" * 35 + "\n")
        f.write(f"Thời điểm   : {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write(f"Từ bí mật   : {tu_bi_mat}\n")
        f.write(f"Kết quả     : {'THẮNG ' if thang else 'THUA '}\n")
        f.write(f"Thời gian   : {thoi_gian:.1f} giây\n")
        f.write(f"Lượt sai còn: {luot_sai_con_lai}/{GIOI_HAN_SAI}\n")
 
def main():
    print("=" * 45)
    print("TRÒ CHƠI ĐOÁN CHỮ CÁI ")
    print("=" * 45)
 
    # Chọn từ ngẫu nhiên
    tu_bi_mat = random.choice(DANH_SACH_TU)
    da_doan_dung = set()
    da_doan_sai = set()
    luot_sai = 0
 
    print(f"\n  Từ bí mật có {len(tu_bi_mat)} chữ cái:")
    print(f"    {tao_hien_thi(tu_bi_mat, da_doan_dung)}\n")
 
    bat_dau = time.time()
 
    while luot_sai < GIOI_HAN_SAI:
        # Kiểm tra thắng
        if all(ch in da_doan_dung for ch in tu_bi_mat):
            break
 
        print(f"   Lượt sai: {luot_sai}/{GIOI_HAN_SAI}  |  Đã đoán sai: {sorted(da_doan_sai) or 'Chưa có'}")
        chu_cai = input("Nhập chữ cái: ").strip().lower()
 
        # Kiểm tra hợp lệ
        if len(chu_cai) != 1 or not chu_cai.isalpha():
            print("Vui lòng nhập đúng 1 chữ cái!\n")
            continue
 
        if chu_cai in da_doan_dung or chu_cai in da_doan_sai:
            print("Bạn đã đoán chữ này rồi!\n")
            continue
 
        if chu_cai in tu_bi_mat:
            da_doan_dung.add(chu_cai)
            print(f"Đúng! Chữ '{chu_cai}' có trong từ.\n")
        else:
            da_doan_sai.add(chu_cai)
            luot_sai += 1
            print(f"Sai! Chữ '{chu_cai}' không có trong từ.\n")
 
        print(f" {tao_hien_thi(tu_bi_mat, da_doan_dung)}\n")
 
    ket_thuc = time.time()
    thoi_gian = ket_thuc - bat_dau
    thang = all(ch in da_doan_dung for ch in tu_bi_mat)
    luot_sai_con_lai = GIOI_HAN_SAI - luot_sai
 
    print("=" * 45)
    if thang:
        print(f"  CHÚC MỪNG! Bạn đã đoán đúng: '{tu_bi_mat}'")
    else:
        print(f"  THUA RỒI! Từ bí mật là: '{tu_bi_mat}'")
 
    print(f"Thời gian hoàn thành: {thoi_gian:.1f} giây")
    print(f"Lượt sai còn lại: {luot_sai_con_lai}/{GIOI_HAN_SAI}")
    print("=" * 45)
 
    # Ghi kết quả vào file
    ghi_ket_qua(tu_bi_mat, thang, thoi_gian, luot_sai_con_lai)
    print("  Kết quả đã được lưu vào 'hangman_result.txt'.")
 
if __name__ == "__main__":
    main()

import string
 
def tach_tu(van_ban):
    """Tách đoạn văn bản thành danh sách các từ, bỏ qua dấu câu cơ bản."""
    
    dau_cau = ",.!?;:"
    for dau in dau_cau:
        van_ban = van_ban.replace(dau, "")
    danh_sach_tu = van_ban.split()
    return danh_sach_tu
 
def dem_tu(danh_sach_tu):
    """Đếm tổng số từ."""
    return len(danh_sach_tu)
 
def tu_xuat_hien_nhieu_nhat(danh_sach_tu):
    """Tìm từ xuất hiện nhiều nhất (không phân biệt hoa/thường)."""
    if not danh_sach_tu:
        return None, 0
 
    tan_suat = {}
    for tu in danh_sach_tu:
        tu_lower = tu.lower()
        tan_suat[tu_lower] = tan_suat.get(tu_lower, 0) + 1
 
    tu_max = max(tan_suat, key=tan_suat.get)
    return tu_max, tan_suat[tu_max]
 
def main():
    print("=" * 50)
    print("     PHÂN TÍCH VÀ THỐNG KÊ VĂN BẢN")
    print("=" * 50)
    print("Nhập đoạn văn bản (2-3 câu):")
    van_ban = input(">>> ").strip()
 
    if not van_ban:
        print("⚠  Bạn chưa nhập văn bản.")
        return
 
   
    danh_sach_tu = tach_tu(van_ban)
 
   
    tong_so_tu = dem_tu(danh_sach_tu)
 
    # Tìm từ xuất hiện nhiều nhất
    tu_nhieu_nhat, so_lan = tu_xuat_hien_nhieu_nhat(danh_sach_tu)
 
    # Hiển thị kết quả
    print("\n" + "=" * 50)
    print("  KẾT QUẢ PHÂN TÍCH:")
    print("=" * 50)
    print(f"   Danh sách các từ : {danh_sach_tu}")
    print(f"   Tổng số từ        : {tong_so_tu} từ")
    print(f"   Từ xuất hiện nhiều nhất: '{tu_nhieu_nhat}' ({so_lan} lần)")
    print("=" * 50)
 
if __name__ == "__main__":
    main()
 
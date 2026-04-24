def tinh_bmi(can_nang, chieu_cao):
    """Tính chỉ số BMI. Ném ZeroDivisionError nếu chiều cao = 0."""
    if chieu_cao == 0:
        raise ZeroDivisionError("Chiều cao không được bằng 0!")
    bmi = can_nang / (chieu_cao ** 2)
    return bmi
 
def phan_loai_bmi(bmi):
    """Phân loại kết quả BMI."""
    if bmi < 18.5:
        return "GẦY", "⚠ "
    elif bmi <= 24.9:
        return "BÌNH THƯỜNG", ""
    else:
        return "THỪA CÂN", "⚠ "
 
def main():
    print("=" * 45)
    print("      CÔNG CỤ TÍNH CHỈ SỐ BMI")
    print("=" * 45)
 
    try:
        can_nang = float(input("  Nhập cân nặng (kg): "))
        chieu_cao = float(input("  Nhập chiều cao (m) : "))
 
        bmi = tinh_bmi(can_nang, chieu_cao)
        phan_loai, icon = phan_loai_bmi(bmi)
 
        print("\n" + "=" * 45)
        print("  KẾT QUẢ:")
        print("=" * 45)
        print(f"  Cân nặng   : {can_nang} kg")
        print(f"  Chiều cao  : {chieu_cao} m")
        print(f"  Chỉ số BMI : {bmi:.2f}")
        print(f"  Phân loại  : {icon} {phan_loai}")
        print("=" * 45)
 
    except ValueError:
        # Người dùng nhập chữ thay vì số
        print("\n Lỗi: Vui lòng nhập số, không nhập chữ!")
 
    except ZeroDivisionError as e:
        # Chiều cao bằng 0
        print(f"\n  Lỗi chia cho 0: {e}")
 
if __name__ == "__main__":
    main()

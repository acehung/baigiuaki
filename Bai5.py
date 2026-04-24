import matplotlib.pyplot as plt 
import matplotlib  
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
 
def main():
  
    kho_hang = {'Balo': 150, 'Tui xach': 80, 'Vali': 120}
 
    print("=" * 45)
    print("QUẢN LÝ KHO HÀNG")
    print("=" * 45)
 
   
    try:
        so_luong_vi_da = int(input("  Nhập số lượng 'Vi da' nhập kho: "))
        kho_hang['Vi da'] = so_luong_vi_da
        print(f"   Đã thêm 'Vi da': {so_luong_vi_da} đơn vị.")
    except ValueError:
        print("    Số lượng không hợp lệ. 'Vi da' không được thêm vào.")
 
   
    kho_hang['Balo'] -= 30
    print(f"   Xuất kho 'Balo' 30 đơn vị. Còn lại: {kho_hang['Balo']} đơn vị.")
 
    # --- Hiển thị kho hàng sau khi cập nhật ---
    print("\n" + "=" * 45)
    print("  DANH SÁCH KHO HÀNG SAU CẬP NHẬT:")
    print("=" * 45)
    tong = sum(kho_hang.values())
    for mat_hang, so_luong in kho_hang.items():
        phan_tram = so_luong / tong * 100
        print(f"   {mat_hang:<12}: {so_luong:>4} đơn vị  ({phan_tram:.1f}%)")
    print(f"  {'TỔNG CỘNG':<12}: {tong:>4} đơn vị")
    print("=" * 45)
 
    # --- YÊU CẦU 3: Vẽ biểu đồ tròn với matplotlib ---
    nhan = list(kho_hang.keys())
    gia_tri = list(kho_hang.values())
 
    mau_sac = ['#4A90D9', '#E8734A', "#97425E", '#F0AD4E']
    no_explode = [0.05] * len(nhan)
 
    fig, ax = plt.subplots(figsize=(7, 6))
    fig.patch.set_facecolor('#F8F9FA')
    ax.set_facecolor('#F8F9FA')
 
    wedges, texts, autotexts = ax.pie(
        gia_tri,
        labels=nhan,
        autopct='%1.1f%%',
        colors=mau_sac[:len(nhan)],
        explode=no_explode,
        startangle=140,
        wedgeprops={'edgecolor': 'white', 'linewidth': 2},
        textprops={'fontsize': 12}
    )
 
    for autotext in autotexts:
        autotext.set_fontweight('bold')
        autotext.set_color('white')
 
    ax.set_title('Tỷ Trọng Kho Hàng', fontsize=15, fontweight='bold', pad=20, color='#2C3E50')
 
    # Thêm legend
    ax.legend(
        wedges,
        [f"{nhan[i]}: {gia_tri[i]} đv" for i in range(len(nhan))],
        title="Mặt hàng",
        loc="lower center",
        bbox_to_anchor=(0.5, -0.12),
        ncol=2,
        fontsize=10
    )
 
    plt.tight_layout()
    plt.savefig('bieu_do_kho_hang.png', dpi=150, bbox_inches='tight', facecolor='#F8F9FA')
    print("\n  Biểu đồ đã được lưu vào 'bieu_do_kho_hang.png'.")
    plt.show()
 
if __name__ == "__main__":
    main()
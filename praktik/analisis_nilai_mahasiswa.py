
# Program Analisis Nilai Mahasiswa

# Data nilai 10 mahasiswa
nilai_mahasiswa = [75, 80, 55, 90, 60, 45, 88, 72, 58, 95]

# Fungsi untuk menghitung rata-rata
def hitung_rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


# Fungsi untuk mengambil nilai mahasiswa yang lulus
def filter_nilai_lulus(data, batas=60):
    nilai_lulus = []

    for nilai in data:
        if nilai >= batas:
            nilai_lulus.append(nilai)

    return nilai_lulus


# Menghitung statistik nilai
jumlah_data = len(nilai_mahasiswa)
total_nilai = sum(nilai_mahasiswa)
rata_rata = hitung_rata_rata(nilai_mahasiswa)
nilai_terendah = min(nilai_mahasiswa)
nilai_tertinggi = max(nilai_mahasiswa)

# Menentukan kelulusan
nilai_lulus = filter_nilai_lulus(nilai_mahasiswa)
jumlah_lulus = len(nilai_lulus)
jumlah_tidak_lulus = jumlah_data - jumlah_lulus

# Menampilkan hasil analisis
print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Data nilai          : {nilai_mahasiswa}")
print(f"Jumlah mahasiswa    : {jumlah_data}")
print(f"Total nilai         : {total_nilai}")
print(f"Rata-rata nilai     : {rata_rata:.2f}")
print(f"Nilai terendah      : {nilai_terendah}")
print(f"Nilai tertinggi     : {nilai_tertinggi}")
print(f"Nilai batas lulus   : 60")
print(f"Daftar nilai lulus  : {nilai_lulus}")
print(f"Jumlah mahasiswa lulus      : {jumlah_lulus}")
print(f"Jumlah mahasiswa tidak lulus: {jumlah_tidak_lulus}")

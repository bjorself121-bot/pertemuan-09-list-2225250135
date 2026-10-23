
# Membuat list nilai mahasiswa
nilai = [75, 55, 80, 60, 45, 90]

# Menyiapkan list kosong untuk nilai lulus
lulus = []

# Memeriksa setiap nilai
for x in nilai:
    if x >= 60:
        lulus.append(x)

# Menampilkan hasil
print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")

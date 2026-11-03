# Fadia Azra Kadarisman | 2604687 | 1A
# hitung rata-rata nilai siswa sesuai jumlah n

nilai_list = []  # Kita ubah jadi list agar bisa menampung semua nilai dan diolah
n = int(input("Jumlah siswa yg nilainya akan diinput: "))

for i in range(n):
    data = int(input(f"Masukkan nilai siswa ke-{i+1}: "))
    nilai_list.append(data)

# Hitung rata-rata, nilai tertinggi, dan terendah
total = sum(nilai_list)
avg = total / n
nilai_tertinggi = max(nilai_list)
nilai_terendah = min(nilai_list)

print(f"\n--- Rekap Nilai Siswa ---")
print(f"List nilai siswa: {nilai_list}")
print(f"Rata-rata nilai siswa adalah: {avg}")
print(f"Nilai tertinggi: {nilai_tertinggi}")  # Secuil kode baru
print(f"Nilai terendah: {nilai_terendah}")    # Secuil kode baru
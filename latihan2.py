# Fadia Azra Kadarisman | 2604687 | 1A
# hitung rata-rata nilai siswa sesuai jumlah n

nilai = 0
# nilai = []  # ini kalo pake list
n = int(input("Jumlah siswa yg nilainya akan diinput: "))

for i in range(n):
    data = int(input(f"Masukkan nilai siswa ke-{i+1}: "))
    nilai += data
    # nilai.append(data) # ini kalo pake list

# hitung rata-rata
# total = sum(nilai) # ini kalo pake list
# avg = total/n # ini kalo pake list
avg = nilai/n

# print(f"List nilai siswa: {nilai}") # ini kalo pake list
print(f"Rata-rata nilai siswa adalah: {avg}")
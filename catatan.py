# perulangan / looping
# waktu yg tepat saat menggunakan for atau while
# for -> itu ketika jumlahnya sudah di ketahui
# while -> ketika jumlah tidak diketahui dan tergantung pada kondisi tertentu, harus perhatikan kondisi berhentinya agar tidak jdi infinite loop

# nested loop
buah = ["apel", "belimbing", "ceri"]
angka = [1, 2]

for i in buah:
    for j in angka:
        print(i)
        print(j)

# looping di list
# pakai in range
buah = ["apple", "banana", "cherry"]
for i in range(len(buah)):
    print(buah[i])

# pakai in list
buah = ["apple", "banana", "cherry"]
for i in buah:
    print(buah)
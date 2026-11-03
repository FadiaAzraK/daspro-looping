# Fadia Azra Kadarisman | 2604687 | 1A

hewan = []
n = int(input("Masukkan jumlah hewan: "))

for i in range(n):
    data = input(f"Masukkan nama hewan ke-{i+1}: ")
    hewan.append(data)

if len(hewan) > 0:
    print(f"Data berhasil dimasukkan! Total hewan: {len(hewan)} ekor[cite: 2]")
    print(hewan)
else:
    print("Belum ada data hewan yang dimasukkan.")
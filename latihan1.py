# Fadia Azra Kadarisma | 2604687 | 1A

hewan = []
n = int(input("Masukkan jumlah hewan: "))

for i in range(n):
    data = input(f"Masukkan nama hewan ke-{i+1}: ")
    hewan.append(data)

print(hewan)
print(f"Total hewan yang dimasukkan adalah: {len(hewan)} ekor")  # Tambahan secuil kode baru
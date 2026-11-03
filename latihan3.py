# Fadia Azra Kadarisman | 2604687 | 1A

bilangan = []
n = int(input("Masukkan jumlah bilangan: "))

for i in range(n):
    data = int(input(f"Masukkan bilangan ke-{i+1}: "))
    bilangan.append(data)
    
jumlah_genap = 0
jumlah_ganjil = 0

for x in bilangan: 
    if x % 2 == 0:
        print(f"{x} adalah bilangan genap")
        jumlah_genap += 1
    else:
        print(f"{x} adalah bilangan ganjil")
        jumlah_ganjil += 1

print(f"\nTotal bilangan genap: {jumlah_genap}")
print(f"Total bilangan ganjil: {jumlah_ganjil}")
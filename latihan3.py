# Fadia Azra Kadarisman | 2604687 | 1A

bilangan = []
n = int(input("Masukkan jumlah bilangan: "))

for i in range(n):
    data = int(input(f"Masukkan bilangan ke-{i+1}: "))
    bilangan.append(data)

for x in bilangan: 
    if x % 2 == 0:
        print(f"{x} adalah bilangan genap")
    else:
        print(f"{x} adalah bilangan ganjil")
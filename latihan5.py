# Fadia Azra Kadarisman | 2604687 | 1A
# sistem login sederhana tidak ada batas salah, usernama: dasproRPL, password: RPLfire!123

username = " "
password = " "

while username != "dasproRPL" or password != "RPLfire!123":
    username = input("Masukkan username anda: ")
    password = input("Masukkan kata sandi anda: ")

    if username == "dasproRPL" and password == "RPLfire!123":
        print("Login berhasil!") 
    else:
        print("username atau pw salah!")
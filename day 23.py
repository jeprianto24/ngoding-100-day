#  program untuk menentukan genap ganjil suatu bilangan

angka = int(input("masukkan bilangan yang ingin anda cek :"))

if (angka%2) != 0 :
    print(angka,"adalah bilangan ganjil")

elif (angka%2) == 0 :
    print(angka,"adalah bilangan genap")

print("SELAMAT DATANG DI ATM")
print("MENU :")
print("1.Penarikan")
print("2.Transfer")
print("3.Cek Saldo")

menu=int(input("Silahkan Pilih menu :"))
saldo= 100

if menu == 1:
    jumlah_penarikan=int(input("masukkan jumlah penarikan :")) 
    sisa_saldo= saldo-jumlah_penarikan
    if jumlah_penarikan<=saldo:
        print(f"anda menarik {jumlah_penarikan} sisa uang anda {sisa_saldo}")
    elif jumlah_penarikan>=saldo:
        print("saldo anda tidak mencukupi")
    
   

if menu == 2:
    jumlah_yang_ingin_ditransfer=int(input("masukkan jumlah yang ingin di transfer :"))
    rekening_tujuan=int(input("masukkan rekening tujuan :"))
    sisa_saldo=saldo-jumlah_yang_ingin_ditransfer
    if jumlah_yang_ingin_ditransfer<=saldo:
         print(f"anda mengirim RP{jumlah_yang_ingin_ditransfer} ke rekening {rekening_tujuan} sisa uang anda RP{sisa_saldo}")
    elif jumlah_yang_ingin_ditransfer>=saldo:
        print("saldo anda tidak cukup")


if menu == 3:
    print(f"saldo anda sebesar RP{saldo}")
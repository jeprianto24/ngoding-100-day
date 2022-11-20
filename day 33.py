nilai = int(input("Masukkan nilai: "))
usia = int(input("Masukkan usia: "))

if nilai >= 75:
  if (usia < 15):
    print("Selamat adek, kamu lulus!")
  else:
    print("Selamat kakak, anda lulus!")
else:
  if (usia < 15):
    print("Mohon maaf anda belum lulus")
  else:
    print("Mohon maaf silahkan coba di lain waktu")
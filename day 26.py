print("belajar perulangan python membuat segitiga, segitiga terbalik,dan pyramid")

angka = int(input("kasukkan angka : "))

for i in range(1,angka+1):
	print(i * "*")
	
	
angka =int(input("masukkan angka : "))

for j in range(1,angka+1):
	print((angka-j+1) * "*")
	
	
angka = int(input("masukkan angka"))

for e in range(1,angka+1):
	print((angka-e) * " " +(2*e-1) * "*")
	
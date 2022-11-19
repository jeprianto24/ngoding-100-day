import cmath

z = "(ax**2 + bx + c = 0)"

a = int(input("masukkan nilai dari a :"))
b = int(input("masukkan nilai dari b :"))
c = int(input("masukkan nilai dari c :"))

rumus = int((b**2)-(4*a*c))

#mencari dan menentukan nilai dari x1 dan x2

x1 = (-b - cmath.sqrt(rumus))/(2*a)
x2 = (-b + cmath.sqrt(rumus))/(2*a)

print("\nhasil dari x1 adalah",(x1))
print("hasil dari x2 adalah",(x2))

print("\njadi himpunan penyelesaian dari",z)
print("x1 =",x1,"dan", "x2 =",x2)

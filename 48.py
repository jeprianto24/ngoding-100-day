
'''Cara Cara Membuat Array atau List'''
#DAFTAR
#Daftar Numerik
dari  traceback  impor  print_tb


data_angka  = [ 1 , 2 , 3 , 4 , 5 ]
print ( f"Daftar angka : { data_angka } " )

# daftar String
data_string  = [ 'kaya' , 'rona' , 'marpaung' ]
cetak ( f"Daftar string: { data_string } " )

#daftar boolean
data_boolean  = [ Benar , Salah , Salah , Salah , Benar ]
print ( f"Daftar Boolean : { data_boolean } " )

#List Campuran
data_campuran  = [ 1 , 'kaya' , 2 , 'rona' , 3 , 'marpaung' , Benar ]
print ( f"List Campuran : { data_campuran } \n " )

'''Cara lain membuat daftar menggunakan Range dan For'''
#menggunakan Rentang
data_range  =  range ( 0 , 10 ) #Bagian ini tidak akan menghasilkan List
cetak ( rentang_data )
data_list_range  =  daftar ( data_range )   #<- ini digunakan untuk menghasilkan daftar
print ( f"List Menggunakan range: { data_list_range } " )

#mengguanak UNTUK
data_for  = [ i  untuk  i  dalam  rentang ( 0 , 10 )]
print ( f"List Menggunakan For : { data_for } \n " )

#mengguanakan UNTUK JIKA
#Membuat daftar bilangan ganjil dan genap
data_ganjil  = [ i  untuk  i  dalam  range ( 0 , 10 ) if  i % 2 != 0 ] #ini akan menghasilkan angka ganjil
print ( f"Daftar angka ganjil : { data_ganjil } " )
data_genap  = [ i  untuk  i  dalam  range ( 0 , 10 ) jika  i % 2 == 0 ] #ini akan menghasilkan angka genap
print ( f"Daftar Angka Genap : { data_genap } " )
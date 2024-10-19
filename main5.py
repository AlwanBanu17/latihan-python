# #Belajar Fungsi

# def sapa(nama):
#     print(f"halo,", nama, "!")
# #format string tanpa jarak spasi
#     print(f"Halo, {nama}!")
# #menampilkna Function

# #mmengisi nilai fungsi dengan type data string yaitu alwan 
# sapa("Alwan")
# #output Halo,Alwan


# def tambah(a,b):
#     hasil = a + b
#     return hasil

# def bagi_dua(hasil):
#     return hasil / 2

# hasil_tambah = tambah(5,3)
# print("hasil penjumlahan adalah:", hasil_tambah)

# hasil_bagi = bagi_dua(hasil_tambah)
# print("Hasil pembagian dengan 2 adalah:", hasil_bagi)

# def tambah(a,b,c):
#     hasil = (a + b) / c
#     return hasil

# jumlah = tambah (3, 5, 2)
# print("hasil penjumlahan adalah:", jumlah)


# membuat list
# buah = ["apel", "pisang", "mangga"]

# #mengakses elemen pada buah pada list
# buah[1] = "jeruk"

# #menambhakan list baru dengan index tertentu
# buah.insert(0, "anggur")

# #menambhakna buah
# buah.append("alpukat")

# #menghapus buah
# buah.remove("mangga")
# print(buah)


# #mengakses elemen
# print(buah[0])  #output apel

# # mengubah elemen
# buah[1] = "jeruk"
# print(buah) #output: ['apel', 'jeruk', 'mangga']


#struktur data Tuple
angka1 = (1, 2, 3)
angka2 = (4, 5, 6)

hasil = angka1 + angka2 
print(hasil)
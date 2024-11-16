Jawaban UTS Python Alwan

1.sesuatu kode kode yang ada di pemograman python untuk jalanin tugas tertentu

2.if adalah kode pemograman untuk memeriksa apakah benar(true), dan else di gunakan bisa setelah if fungsi kode else untuk
  memerika apakah perintah yang di ketikan di if terpenuhi jika tidak maka akan (false), dan untuk elif perintah ini bisa di gunakan sebelom 
  else yang di mana perintah ini di gunakan untuk evaluasi if jika salah maka program ini akan mengecek pada kondisi program selanjutnya

3.
harga_nasi_goreng = 20000
harga_mie_goreng = 15000
harga_sate = 30000

uang_saku = 300000

def input_jumlah_porsi(nama_makanan):
    while True:
        try:
            jumlah = int(input(f"Masukkan jumlah porsi {nama_makanan}: "))
            if jumlah < 0:
                print("Jumlah porsi tidak bisa negatif. Silakan coba lagi.")
            else:
                return jumlah
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

jumlah_nasi_goreng = input_jumlah_porsi("Nasi Goreng")
jumlah_mie_goreng = input_jumlah_porsi("Mie Goreng")
jumlah_sate = input_jumlah_porsi("Sate")

total_belanja = (jumlah_nasi_goreng * harga_nasi_goreng +
                 jumlah_mie_goreng * harga_mie_goreng +
                 jumlah_sate * harga_sate)

if total_belanja > 100000:
    diskon = total_belanja * 0.2 
else:
    diskon = 0

total_setelah_diskon = total_belanja - diskon

uang_kembalian = uang_saku - total_setelah_diskon

print("\n--- Rincian Belanja ---")
print(f"Total belanja: Rp{total_belanja}")
if diskon > 0:
    print(f"Diskon: Rp{diskon} (20% untuk belanja di atas Rp100.000)")
print(f"Total setelah diskon: Rp{total_setelah_diskon}")
print(f"Uang kembalian: Rp{uang_kembalian}")


# 4.
fruits = ("banana", "apple", "cherry")

fruits_list = list(fruits)

fruits_list.sort()

if "banana" in fruits_list:
    print("Elemen 'banana' ada dalam list.")

print("List setelah diubah dan urutkan:", fruits_list)

5.
def intersection_set(setA, setB):
    return setA.intersection(setB)

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

result = intersection_set(setA, setB)
print("Intersection:", result)
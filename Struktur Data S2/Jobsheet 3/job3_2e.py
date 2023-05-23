def kaliSendiri(mulai, akhir):
    hasil = []
    for i in range(mulai, akhir):
        hasil.append(i * i)
    return hasil

mulaiAngka = int(input("Masukkan angka awal: "))
akhirAngka = int(input("Masukkan angka akhir: "))

squared_numbers = kaliSendiri(mulaiAngka,akhirAngka)

print("Hasil perkalian dengan angka itu sendiri:")
print(squared_numbers)

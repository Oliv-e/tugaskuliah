nilaiAkhir = float(input("Masukkan Nilai : "))

if 0.00 >= nilaiAkhir <= 34.40 :
    nilaiKuliah = 'E'
    bobotNilai = '0'
    status = "Tidak Lulus"
elif 34.41 >= nilaiAkhir <= 50.50 :
    nilaiKuliah = 'D'
    bobotNilai = '1'
    status = "Tidak Lulus"
elif 50.51 >= nilaiAkhir <= 65.50 :
    nilaiKuliah = 'C'
    bobotNilai = '2'
    status = "Lulus"
elif 65.51 >= nilaiAkhir <= 80.50 :
    nilaiKuliah = 'B'
    bobotNilai = '3'
    status = "Lulus"
elif 80.51 >= nilaiAkhir <= 100 :
    nilaiKuliah = 'A'
    bobotNilai = '4'
    status = "Lulus"

print("""
    Selamat Anda """ , status , """
    Nilai Huruf Anda : """ , nilaiKuliah , """
    Bobot Nilai Anda : """ , bobotNilai, """
""")
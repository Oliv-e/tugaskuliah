IPK = float(input("Masukkan IPK : "))

if 0.00 >= IPK <= 1.99:
    predikatKelulusan = "Tidak Lulus"
elif 1.00 >= IPK <= 1.99:
    predikatKelulusan = "Tidak Lulus"
elif 2.00 >= IPK <= 2.99:
    predikatKelulusan = "Memuaskan"
elif 3.00 >= IPK <= 3.50:
    predikatKelulusan = "Sangat Memuaskan"
elif 3.51 >= IPK <= 4.00:
    predikatKelulusan = "Cumlaude"

if predikatKelulusan != "Tidak Lulus":
    print("Selamat anda lulu dengan predikat",predikatKelulusan)
else :
    print ("Maaf, Anda Belum Lulus")
import os
os.system('cls')

def main():
    menu()

def menu():
    nim = 3202216074
    nama = "Oliver Dillon"
    jurusan = "Teknik Elektro"
    prodi = "Teknik Informatika"
    kelas = "2/D"
    IPS1 = 4.00


    xnim = int(input("Masukkan NIM anda! \n"))

    if xnim == nim :

        os.system('cls')
        print("===FORM NILAI===")
        print("MASUKKAN NILAI DIANTARA 0.00 s.d. 4.00!")
        nmakul1 = -1
        while nmakul1 < 0.00 or nmakul1 > 4.00:
            try:
                nmakul1 = float(input("Nilai Basis Data : ")) #4
            except ValueError:
                print("Nilai yang anda masukkan salah, silahkan coba lagi!")
        nmakul2 = -1
        while nmakul2 < 0.00 or nmakul2 > 4.00:
            try:
                nmakul2 = float(input("Nilai Struktur Data : ")) #4
            except ValueError:
                print("Nilai yang anda masukkan salah, silahkan coba lagi!")
        nmakul3 = -1
        while nmakul3 < 0.00 or nmakul3 > 4.00:
            try:
                nmakul3 = float(input("Nilai Pemrograman Berbasis Objek : ")) #4
            except ValueError:
                print("Nilai yang anda masukkan salah, silahkan coba lagi!")
        nmakul4 = -1
        while nmakul4 < 0.00 or nmakul4 > 4.00:
            try:
                nmakul4 = float(input("Nilai Arsitektur Komputer : ")) #3
            except ValueError:
                print("Nilai yang anda masukkan salah, silahkan coba lagi!")
        nmakul5 = -1
        while nmakul5 < 0.00 or nmakul5 > 4.00:
            try:
                nmakul5 = float(input("Nilai Matematika : ")) #2
            except ValueError:
                print("Nilai yang anda masukkan salah, silahkan coba lagi!")
        nmakul6 = -1
        while nmakul6 < 0.00 or nmakul6 > 4.00:
            try:
                nmakul6 = float(input("Nilai Bahasa Indonesia : ")) #2
            except ValueError:
                print("Nilai yang anda masukkan salah, silahkan coba lagi!")
        nmakul7 = -1
        while nmakul7 < 0.00 or nmakul7 > 4.00:
            try:
                nmakul7 = float(input("Nilai Statistika dan Probabilitas : ")) #2
            except ValueError:
                print("Nilai yang anda masukkan salah, silahkan coba lagi!")

        BD = nmakul1 * 4
        SD = nmakul2 * 4
        PBO = nmakul3 * 4
        AK = nmakul4 * 3
        MTK = nmakul5 * 2
        BHS = nmakul6 * 2
        STT = nmakul7 * 2

        BxK = BD + SD + PBO + AK + MTK + BHS + STT
        IPS2 = ((BxK / 21) + IPS1) / 2
        IPSFIX = "{:.2f}".format(IPS2)

        if IPSFIX >= 3.30 & IPSFIX < 4.01:
            nilaimutu = 'A'
        elif IPSFIX >= 2.70 & IPSFIX < 3.30:
            nilaimutu = 'B'
        elif IPSFIX >= 1.70 & IPSFIX < 2.70:
            nilaimutu = 'C'
        elif IPSFIX >= 1.00 & IPSFIX < 1.70:
            nilaimutu = 'D'
        elif IPSFIX >= 0.00 & IPSFIX < 1.00:
            nilaimutu = 'E'

        os.system('cls')
        print("""
        =====BIODATA MAHASISWA====
        Nama        :""",nama,"""
        Nim         :""",nim,"""
        Jurusan     :""",jurusan,"""
        Prodi       :""",prodi,"""
        Kelas       :""",kelas,"""
        IPS Sem. 2  :""",IPSFIX,"""
        Nilaimutu   :""",nilaimutu,"""
        """)
    elif xnim != nim:   
        print("NIM anda salah, silahkan masukkan lagi!") 
        menu()
main()
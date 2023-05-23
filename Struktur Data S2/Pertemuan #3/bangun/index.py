import os
import datetime as waktu

import luas

import volume

tanggal = waktu.datetime.now().replace(microsecond=0)
os.system('cls')
nama = input("Masukkan Nama Anda! : \n")

def main():
    menu()

def menu():
    os.system('cls')
    print('=' * 10,"WELCOME TO MENU MATEMATIKA",'=' * 10)
    print("Hi,",nama,"Apa yang Ingin Anda Hitung?")
    print("Waktu Sekarang : ",tanggal)

    pilihan = int(input("""
    1. Bangun Datar
    2. Bangun Ruang
    3. Keluar 
    Pilihan Anda : """))

    if pilihan == 1:
        pilihan2 = int(input("""
    1. Persegi
    2. Persegi Panjang
    3. Segitiga
    4. Lingkaran
    5. Jajar Genjang
    6. Trapesium
    7. Belah Ketupat
    8. Layang- Layang
    Pilihan Anda : """))
        pilihan3 = int(input("""
    1. Hitung Luas
    2. Hitung Keliling
    Pilihan Anda : """))
        print()
        if pilihan3 == 1:
            if pilihan2 == 1:
                from luas.persegi import luas_persegi
                i = int(input("Masukkan Sisi Persegi : "))
                print()
                print("Luas Persegi Anda : ",luas_persegi(i))
                print("Waktu Sekarang    : ",tanggal)
                print("Path Persegi      : ",luas.persegi.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 2:
                from luas.persegi_panjang import luas_persegi_panjang
                i = int(input("Masukkan Panjang Persegi Panjang : "))
                j = int(input("Masukkan Lebar Persegi Panjang   : "))
                print()
                print("Luas Persegi Panjang Anda : ",luas_persegi_panjang(i,j))
                print("Waktu Sekarang            : ",tanggal)
                print("Path Persegi Panjang      : ",luas.persegi_panjang.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 3:
                from luas.segitiga import luas_segitiga
                i = int(input("Masukkan Alas Segitiga   : "))
                j = int(input("Masukkan Tinggi Segitiga : "))
                print()
                print("Luas Segitiga Anda : ",luas_segitiga(i,j))
                print("Waktu Sekarang     : ",tanggal)
                print("Path Segitiga      : ",luas.segitiga.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 4:
                from luas.lingkaran import luas_lingkaran
                i = int(input("Masukkan Jari-Jari Lingkaran : "))
                print()
                print("Luas Lingkaran Anda : ",luas_lingkaran(i))
                print("Waktu Sekarang      : ",tanggal)
                print("Path Lingkaran      : ",luas.lingkaran.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 5:
                from luas.jajar_genjang import luas_jajar_genjang
                i = int(input("Masukkan Alas Jajar Genjang   : "))
                j = int(input("Masukkan Tinggi Jajar Genjang : "))
                print()
                print("Luas Jajar Genjang Anda : ",luas_jajar_genjang(i,j))
                print("Waktu Sekarang          : ",tanggal)
                print("Path Jajar Genjang      : ",luas.jajar_genjang.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 6:
                from luas.trapesium import luas_trapesium
                i = int(input("Masukkan Sisi Bawah Trapesium : "))
                J = int(input("Masukkan Sisi Atas Trapesium  : "))
                k = int(input("Masukkan Tinggi Trapesium     : "))
                print()
                print("Luas Trapesium Anda : ",luas_trapesium(i,j,k))
                print("Waktu Sekarang      : ",tanggal)
                print("Path Trapesium      : ",luas.trapesium.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 7:
                from luas.belah_ketupat import luas_belah_ketupat
                i = int(input("Masukkan Diagonal 1 Ketupat : "))
                j = int(input("Masukkan Diagonal 2 Ketupat : "))
                print()
                print("Luas Belah Ketupat Anda : ",luas_belah_ketupat(i,j))
                print("Waktu Sekarang          : ",tanggal)
                print("Path Belah Ketupat      : ",luas.belah_ketupat.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 8:
                from luas.layang_layang import luas_layang_layang
                i = int(input("Masukkan Diagonal 1 Ketupat : "))
                j = int(input("Masukkan Diagonal 2 Ketupat : "))
                print()
                print("Luas Layang Layang Anda : ",luas_layang_layang(i,j))
                print("Waktu Sekarang          : ",tanggal)
                print("Path Layang-Layang      : ",luas.layang_layang.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
        if pilihan3 == 2:
            if pilihan2 == 1:
                from luas.persegi import keliling_persegi
                i = int(input("Masukkan Sisi Persegi : "))
                print()
                print("Keliling Persegi Anda : ",keliling_persegi(i))
                print("Waktu Sekarang        : ",tanggal)
                print("Path Persegi          : ",luas.persegi.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 2:
                from luas.persegi_panjang import keliling_persegi_panjang
                i = int(input("Masukkan Panjang Persegi Panjang : "))
                j = int(input("Masukkan Lebar Persegi Panjang   : "))
                print()
                print("Keliling Persegi Panjang Anda : ",keliling_persegi_panjang(i,j))
                print("Waktu Sekarang                : ",tanggal)
                print("Path Persegi Panjang          : ",luas.persegi_panjang.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 3:
                from luas.segitiga import keliling_segitiga
                i = int(input("Masukkan Alas Segitiga   : "))
                j = int(input("Masukkan Tinggi Segitiga : "))
                print()
                print("Keliling Segitiga Anda : ",keliling_segitiga(i,j))
                print("Waktu Sekarang         : ",tanggal)
                print("Path Segitiga          : ",luas.segitiga.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 4:
                from luas.lingkaran import keliling_lingkaran
                i = int(input("Masukkan Jari-Jari Lingkaran : "))
                print()
                print("Keliling Lingkaran Anda : ",keliling_lingkaran(i))
                print("Waktu Sekarang          : ",tanggal)
                print("Path Lingkaran          : ",luas.lingkaran.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 5:
                from luas.jajar_genjang import keliling_jajar_genjang
                i = int(input("Masukkan Alas Jajar Genjang   : "))
                j = int(input("Masukkan Tinggi Jajar Genjang : "))
                print()
                print("Keliling Jajar Genjang Anda : ",keliling_jajar_genjang(i,j))
                print("Waktu Sekarang              : ",tanggal)
                print("Path Jajar Genjang          : ",luas.jajar_genjang.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 6:
                from luas.trapesium import keliling_trapesium
                i = int(input("Masukkan Sisi Bawah Trapesium : "))
                J = int(input("Masukkan Sisi Atas Trapesium  : "))
                k = int(input("Masukkan Tinggi Trapesium     : "))
                print()
                print("Keliling Trapesium Anda : ",keliling_trapesium(i,j,k))
                print("Waktu Sekarang          : ",tanggal)
                print("Path Trapesium          : ",luas.trapesium.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 7:
                from luas.belah_ketupat import keliling_belah_ketupat
                i = int(input("Masukkan Diagonal 1 Ketupat : "))
                j = int(input("Masukkan Diagonal 2 Ketupat : "))
                print()
                print("Keliling Belah Ketupat Anda : ",keliling_belah_ketupat(i,j))
                print("Waktu Sekarang              : ",tanggal)
                print("Path Belah Ketupat          : ",luas.belah_ketupat.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 8:
                from luas.layang_layang import keliling_layang_layang
                i = int(input("Masukkan Diagonal 1 Ketupat : "))
                j = int(input("Masukkan Diagonal 2 Ketupat : "))
                print()
                print("Keliling Layang Layang Anda : ",keliling_layang_layang(i,j))
                print("Waktu Sekarang              : ",tanggal)
                print("Path Layang-Layang          : ",luas.layang_layang.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
    if pilihan == 2:
        pilihan2 = int(input("""
    1. Kubik
    2. Balok
    3. Kerucut
    4. Bola
    5. Tabung
    6. Limas Segitiga
    7. Limas Segiempat
    8. Prisma Segitiga
    Pilihan Anda : """))
        pilihan3 = int(input("""
    1. Hitung Volume
    2. Hitung Luas Permukaan
    Pilihan Anda : """))
        print()
        if pilihan3 == 1:
            if pilihan2 == 1:
                from volume.kubik import volume_kubik
                i = int(input("Masukkan Panjang Kubik : "))
                j = int(input("Masukkan Lebar Kubik   : "))
                k = int(input("Masukkan Tinggi Kubik  : "))
                print()
                print("Volume Kubik Anda : ",volume_kubik(i,j,k))
                print("Waktu Sekarang    : ",tanggal)
                print("Path Kubik        : ",volume.kubik.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 2:
                from volume.balok import volume_balok
                i = int(input("Masukkan Panjang Balok : "))
                j = int(input("Masukkan Lebar Balok   : "))
                k = int(input("Masukkan Tinggi Balok  : "))
                print()
                print("Volume Balok Anda : ",volume_balok(i,j,k))
                print("Waktu Sekarang    : ",tanggal)
                print("Path Balok        : ",volume.balok.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 3:
                from volume.kerucut import volume_kerucut
                i = int(input("Masukkan Jari-Jari Kerucut : "))
                j = int(input("Masukkan Tinggi Kerucut    : "))
                print()
                print("Volume Kerucut Anda : ",volume_kerucut(i,j))
                print("Waktu Sekarang      : ",tanggal)
                print("Path Kerucut        : ",volume.kerucut.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 4:
                from volume.bola import volume_bola
                i = int(input("Masukkan Jari-Jari Bola : "))
                print()
                print("Luas Persegi Anda : ",volume_bola(i))
                print("Waktu Sekarang    : ",tanggal)
                print("Path Bola         : ",volume.bola.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 5:
                from volume.tabung import volume_tabung
                i = int(input("Masukkan Jari-Jari Tabung : "))
                j = int(input("Masukkan Tinggi Tabung    : "))
                print()
                print("Volume Tabung Anda : ",volume_tabung(i,j))
                print("Waktu Sekarang     : ",tanggal)
                print("Path Tabung        : ",volume.tabung.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 6:
                from volume.limas_segitiga import volume_limas_segitiga
                i = int(input("Masukkan Alas Limas Segitiga        : "))
                j = int(input("Masukkan Tinggi Limas Segitiga      : "))
                k = int(input("Masukkan Tinggi Alas Limas Segitiga : "))
                print()
                print("Volume Limas Segitiga Anda : ",volume_limas_segitiga(i,j,k))
                print("Waktu Sekarang             : ",tanggal)
                print("Path Limas Segitiga        : ",volume.limas_segitiga.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 7:
                from volume.limas_segiempat import volume_limas_segiempat
                i = int(input("Masukkan Alas Limas Segiempat   : "))
                j = int(input("Masukkan Tinggi Limas Segiempat : "))
                print()
                print("Volume Limas Segiempat Anda : ",volume_limas_segiempat(i,j))
                print("Waktu Sekarang              : ",tanggal)
                print("Path Limas Segiempat        : ",volume.limas_segiempat.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 8:
                from volume.prisma_segitiga import volume_prisma_segitiga
                i = int(input("Masukkan Alas Prisma Segitiga        : "))
                j = int(input("Masukkan Tinggi Prisma Segitiga      : "))
                k = int(input("Masukkan Tinggi Alas Prisma Segitiga : "))
                print()
                print("Volume Prisma Segitiga Anda : ",volume_prisma_segitiga(i,j,k))
                print("Waktu Sekarang              : ",tanggal)
                print("Path Prisma Segitiga        : ",volume.prisma_segitiga.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
        if pilihan3 == 2:
            if pilihan2 == 1:
                from volume.kubik import luas_permukaan_kubik
                i = int(input("Masukkan Sisi Kubik : "))
                print()
                print("Luas Permukaan Kubik Anda   : ",luas_permukaan_kubik(i))
                print("Waktu Sekarang              : ",tanggal)
                print("Path Kubik                  : ",volume.kubik.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 2:
                from volume.balok import luas_permukaan_balok
                i = int(input("Masukkan Panjang Balok : "))
                j = int(input("Masukkan Lebar Balok   : "))
                k = int(input("Masukkan Tinggi Balok  : "))
                print()
                print("Luas Permukaan Balok Anda : ",luas_permukaan_balok(i,j,k))
                print("Waktu Sekarang            : ",tanggal)
                print("Path Balok                : ",volume.balok.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 3:
                from volume.kerucut import luas_permukaan_kerucut
                i = int(input("Masukkan Jari-Jari Kerucut : "))
                j = int(input("Masukkan Selimut Kerucut   : "))
                print()
                print("Luas Permukaan Kerucut Anda : ",luas_permukaan_kerucut(i,j))
                print("Waktu Sekarang              : ",tanggal)
                print("Path Kerucut                : ",volume.kerucut.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 4:
                from volume.bola import luas_permukaan_bola
                i = int(input("Masukkan Jari-Jari Bola : "))
                print()
                print("Luas Permukaan Bola Anda : ",luas_permukaan_bola(i))
                print("Waktu Sekarang           : ",tanggal)
                print("Path Bola                : ",volume.bola.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 5:
                from volume.tabung import luas_permukaan_tabung
                i = int(input("Masukkan Jari-Jari Tabung : "))
                j = int(input("Masukkan Tinggi Tabung    : "))
                print()
                print("Luas Permukaan Tabung Anda : ",luas_permukaan_tabung(i,j))
                print("Waktu Sekarang             : ",tanggal)
                print("Path Tabung                : ",volume.tabung.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 6:
                from volume.limas_segitiga import luas_permukaan_limas_segitiga
                i = int(input("Masukkan Luas Sisi 1 Limas Segitiga : "))
                j = int(input("Masukkan Luas Sisi 2 Limas Segitiga : "))
                k = int(input("Masukkan Luas Sisi 3 Limas Segitiga : "))
                l = int(input("Masukkan Luas Sisi 4 Limas Segitiga : "))
                print()
                print("Luas Permukaan Limas Segitiga Anda : ",luas_permukaan_limas_segitiga(i,j,k,l))
                print("Waktu Sekarang                     : ",tanggal)
                print("Path Limas Segitiga                : ",volume.limas_segitiga.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 7:
                from volume.limas_segiempat import luas_permukaan_limas_segiempat
                i = int(input("Masukkan Luas Sisi 1 Limas Segiempat : "))
                j = int(input("Masukkan Luas Sisi 2 Limas Segiempat : "))
                k = int(input("Masukkan Luas Sisi 3 Limas Segiempat : "))
                l = int(input("Masukkan Luas Sisi 4 Limas Segiempat : "))
                m = int(input("Masukkan Luas Sisi 5 Limas Segiempat : "))
                print()
                print("Luas Permukaan Limas Segiempat Anda : ",luas_permukaan_limas_segiempat(i,j,k,l,m))
                print("Waktu Sekarang                      : ",tanggal)
                print("Path Limas Segiempat                : ",volume.limas_segiempat.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
            if pilihan2 == 8:
                from volume.prisma_segitiga import luas_permukaan_prisma_segitiga
                i = int(input("Masukkan Alas Prisma Segitiga        : "))
                j = int(input("Masukkan Tinggi Prisma Segitiga      : "))
                k = int(input("Masukkan Tinggi Alas Prisma Segitiga : "))
                l = int(input("Masukkan Luas Sisi 1 Prisma Segitiga : "))
                m = int(input("Masukkan Luas Sisi 2 Prisma Segitiga : "))
                n = int(input("Masukkan Luas Sisi 3 Prisma Segitiga : "))
                print()
                print("Luas Permukaan Prisma Segitiga Anda : ",luas_permukaan_prisma_segitiga(i,j,k,l,m,n))
                print("Waktu Sekarang                      : ",tanggal)
                print("Path Prisma Segitiga                : ",volume.prisma_segitiga.__file__)
                print()
                input("Tekan Enter untuk Kembali ")
                menu()
main()
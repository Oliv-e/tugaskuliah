def segitigarkb(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end='  ')
        print()

def segitigarka(n):
    for i in range(n):
        for j in range(n - i):
            print('*', end='  ')
        print()

banyak = int(input("Masukkan jumlah baris yang ingin ditampilkan: "))

segitigarka(banyak)
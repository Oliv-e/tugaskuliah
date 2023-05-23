def faktorial(a):
    faktorial = 1
    ufaktorial = str(a) + "!"

    for i in range(1, a + 1):
        faktorial *= i

    for i in range(1, a):
        ufaktorial += " " + str(i) + " x"
    ufaktorial += " " + str(a)

    return faktorial, ufaktorial

a = int(input("Masukkan Angka: "))
hfaktorial, uraian = faktorial(a)

print("Nilai faktorial dari", a, "adalah :", hfaktorial)
print("Uraian faktorial dari", a, "adalah :", uraian)
def pascal_segitiga(n):
    segitiga = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = segitiga[i-1][j-1] + segitiga[i-1][j]
        segitiga.append(row)
    return segitiga

inputAngka = int(input("Masukkan jumlah baris yang ingin ditampilkan: "))

segitiga = pascal_segitiga(inputAngka)
for row in segitiga:
    print(' '.join(map(str, row)))

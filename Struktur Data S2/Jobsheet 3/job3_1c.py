hari = input("Masukkan nama Hari : ")

match hari:
    case "Senin":
        ruang = "Kelas TI-4"
        matkul = "Basis Data"
        waktu = "07:00 s.d. 15:00 WIB"
        dresscode = "Program Studi Warna Merah Abu"
        dosen = "Sarah Bibi"
    case "Selasa":
        ruang = "Kelas TI-4"
        matkul = "Struktur Data"
        waktu = "07:00 s.d. 15:00 WIB"
        dresscode = "Baju Formal, Bebas dan Rapi"
        dosen = "Suharsono"
    case "Rabu":
        ruang = "Kelas TI-4"
        matkul = "Pemrograman Berbasis Objek"
        waktu = "07:00 s.d. 15:00 WIB"
        dresscode = "Baju Formal, Bebas dan Rapi"
        dosen = "Budianingsih"
    case "Kamis":
        ruang = "Kelas TI-4"
        matkul = "Arsitektur Pemrograman & Matematika"
        waktu = "07:00 s.d. 15:00 WIB"
        dresscode = "Program Studi Warna Merah Biru"
        dosen = "Suharsono & Ramli"
    case "Jum'at":
        ruang = "Kelas TI-4"
        matkul = "Pemrograman Berbasis Objek, Bahasa Indonesia dan Statistika"
        waktu = "07:00 s.d. 15:00 WIB"
        dresscode = "Baju Formal, Bebas dan Rapi"
        dosen = "Budianingsih, Sajidin dan Mariana"

print("Jadwal anda hari ",hari)
print("Ruang Kuliah Anda di ",ruang)
print("Mata Kuliah ",matkul)
print("Waktu Kuliah pukul ",waktu)
print("Baju yang digunakan adalah ",dresscode)
print("Dosen Pengampu ",dosen)
pi = 3.14

def volume_tabung(r, tinggi):
    return pi * (r**2) * tinggi

def luas_permukaan_tabung(r, tinggi):
    Ls = 2 * pi * r * tinggi
    return Ls + (2 * pi * (r**2))
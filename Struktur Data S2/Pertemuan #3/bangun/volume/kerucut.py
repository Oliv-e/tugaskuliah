pi = 3.14

def volume_kerucut(r, tinggi):
    return (pi * (r**2) * tinggi) / 3

def luas_permukaan_kerucut(r, s):
    Ls = pi * r * s
    return Ls + (pi * (r**2))
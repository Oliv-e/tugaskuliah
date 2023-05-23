def volume_prisma_segitiga(alas, tinggi, tinggi_prisma):
    return (0.5 * alas * tinggi) * tinggi_prisma

def luas_permukaan_prisma_segitiga(alas, tinggi, tinggi_prisma, s1, s2, s3):
    Ls = (s1 + s2 + s3) * tinggi
    return Ls + (alas * tinggi_prisma)
import sys

username = "oliversmk7rpl@gmail.com"
password = "3202216074"

i = 0
while i < 3:
    xlogin = str(input("Masukkan email : "))
    xpass = str(input("Masukkan password : "))
    if xlogin == username and xpass == password:
        print("benar")
        break
    else:
        print("salah")
        i+=1
sys.exit()


    
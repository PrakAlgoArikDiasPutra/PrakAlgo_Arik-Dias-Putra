# -*- coding: utf-8 -*-
"""PrakAlgo 4 Arik Dias Putra

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KvDho-W0hrw4pxTr2zu2hJ9RtLBiLafy
"""

# Banner Python
banner = """

@@@@ @@@@  @ @  @
@  @ @   @ @ @ @
@@@@ @  @@ @ @@
@  @ @ @   @ @ @
@  @ @  @  @ @   @

"""

# Menampilkan banner pada layar
print(banner)

while True:
    print("----PROGRAM KONVERSI BILANGAN----")
    print("1-> Angka ke Biner")
    print("2-> Biner ke Angka")
    print("3-> Exit")

    choice = input("Masukkan pilihan anda-> ")

    if choice == '1':
        angka = int(input("Masukkan angka: "))
        biner = bin(angka)[2:]
        print(f"Hasil {angka} dalam biner adalah {biner}")
    elif choice == '2':
        biner = input("Masukkan biner: ")
        angka = int(biner, 2)
        print(f"Hasil {biner} dalam angka angka {angka}")
    elif choice == '3':
        print("Terima kasih!!!!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

# Banner Python
banner = """

@@@@ @@@@  @ @  @
@  @ @   @ @ @ @
@@@@ @  @@ @ @@
@  @ @ @   @ @ @
@  @ @  @  @ @   @

"""

# Menampilkan banner pada layar
print(banner)

def cek_angka_genap(lst):
    for angka in lst:
        if angka % 2 == 0:
            return True
    return False

input_str = input("Masukkan list angka (integer)-> ")
angka_list = [int(x) for x in input_str.split()]

hasil = cek_angka_genap(angka_list)

if hasil:
    print("List memiliki angka genap.")
else:
    print("List tidak memiliki angka genap.")
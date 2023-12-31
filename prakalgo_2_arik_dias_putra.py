# -*- coding: utf-8 -*-
"""PrakAlgo 2_Arik Dias Putra

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13A2NTDIy-4dHz2cgv7t38bCwBJEIYsIm
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


import math

def hitung_sisi():
    print("Selamat datang di Kalkulator Pythagoras!")

    while True:
        print("Pilih sisi yang ingin dihitung:")
        print("1. Sisi a")
        print("2. Sisi b")
        print("3. Sisi c")

        pilihan = input("Masukkan nomor pilihan Anda (1/2/3): ")

        try:
            pilihan = int(pilihan)
            if pilihan not in [1, 2, 3]:
                raise ValueError("Pilihan tidak valid. Pilih 1, 2, atau 3.")
        except ValueError as e:
            print(f"Terjadi kesalahan: {e}")
            continue

        if pilihan == 1:
            b = float(input("Masukkan panjang sisi b: "))
            while True:
                c = float(input("Masukkan panjang sisi c: "))
                if c <= b:
                    print("Nilai c harus lebih besar dari nilai b. Silakan coba lagi.")
                else:
                    break

            a = math.sqrt(c**2 - b**2)
            print(f"Panjang sisi a adalah: {a}")

        elif pilihan == 2:
            a = float(input("Masukkan panjang sisi a: "))
            while True:
                c = float(input("Masukkan panjang sisi c: "))
                if c <= a:
                    print("Nilai c harus lebih besar dari nilai a. Silakan coba lagi.")
                else:
                    break

            b = math.sqrt(c**2 - a**2)
            print(f"Panjang sisi b adalah: {b}")

        elif pilihan == 3:
            a = float(input("Masukkan panjang sisi a: "))
            b = float(input("Masukkan panjang sisi b: "))

            while True:
                c = float(input("Masukkan panjang sisi c: "))
                if c <= a/b:
                    print("Nilai c harus lebih besar dari a/b. Silakan coba lagi.")
                else:
                    break

            c = math.sqrt(a**2 + b**2)
            print(f"Panjang sisi c adalah: {c}")

        ulang = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
        if ulang.lower() != "ya":
            break

if __name__ == "__main__":
    hitung_sisi()

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

import math

def hitung_sisi():
    print("Selamat datang di Kalkulator Pythagoras!")
    print("Pilih sisi yang ingin dihitung:")
    print("1. Sisi a")
    print("2. Sisi b")
    print("3. Sisi c")

    while True:
        pilihan = input("Masukkan nomor pilihan Anda (1/2/3): ")

        if pilihan not in ['1', '2', '3']:
            print("Pilihan tidak valid. Pilih 1, 2, atau 3.")
            continue

        pilihan = int(pilihan)

        if pilihan == 1:
            b = float(input("Masukkan panjang sisi b: "))
            c = float(input("Masukkan panjang sisi c: "))

            if c < b:
                print("Nilai c tidak boleh lebih kecil dari nilai b.")
            else:
                a = math.sqrt(c**2 - b**2)
                print(f"Panjang sisi a adalah: {a}")

        elif pilihan == 2:
            a = float(input("Masukkan panjang sisi a: "))
            c = float(input("Masukkan panjang sisi c: "))

            if c < a:
                print("Nilai c tidak boleh lebih kecil dari nilai a.")
            else:
                b = math.sqrt(c**2 - a**2)
                print(f"Panjang sisi b adalah: {b}")

        elif pilihan == 3:
            a = float(input("Masukkan panjang sisi a: "))
            b = float(input("Masukkan panjang sisi b: "))
            c = math.sqrt(a**2 + b**2)

            if c < a / b:
                print("Nilai c tidak boleh lebih kecil dari a / b.")
            else:
                print(f"Panjang sisi c adalah: {c}")

        ulang = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
        if ulang.lower() != "ya":
            break

if __name__ == "__main__":
    hitung_sisi()

3# Banner Python
banner = """

@@@@ @@@@  @ @  @
@  @ @   @ @ @ @
@@@@ @  @@ @ @@
@  @ @ @   @ @ @
@  @ @  @  @ @   @

"""

# Menampilkan banner pada layar
print(banner)

# Input tiga angka dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
angka3 = float(input("Masukkan angka ketiga: "))

# Temukan angka terbesar menggunakan fungsi max()
angka_terbesar = max(angka1, angka2, angka3)

# Tampilkan hasil
print("Hasil running program:")
print(f"Angka terbesar adalah: {angka_terbesar}")
# -*- coding: utf-8 -*-
"""PrakAlgo 9 Arik Dias Putra

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14k6sKISdHGzz4wVQMHPBTKehpon4xhKO
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

def konversi_list_ke_tuple(list_data):
    return tuple(list_data)

# Meminta pengguna untuk memasukkan nilai-nilai list
input_list = input("Masukkan list: ")
list_data = list(map(int, input_list.split(',')))

# Mengkonversi list menjadi tuple
tuple_result = konversi_list_ke_tuple(list_data)

# Menampilkan hasil
print("List Data:", list_data)
print("hasil revese ke tuple")
print("Tuple Result:", tuple_result)

banner = """

@@@@ @@@@  @ @  @
@  @ @   @ @ @ @
@@@@ @  @@ @ @@
@  @ @ @   @ @ @
@  @ @  @  @ @   @

"""

# Menampilkan banner pada layar
print(banner)

a = ('1021, 1022, 1023', '1025, 1026, 1027', '1029, 1030, 1030')
print(a)
def rata_rata(angka):
    rata_rata = [int(x) for x in angka.split(', ')]
    return int(sum(rata_rata) / len(rata_rata))

averages = [rata_rata(group) for group in a]
print(f"rata rata dari tuple adalah : {averages} ")

banner = """

@@@@ @@@@  @ @  @
@  @ @   @ @ @ @
@@@@ @  @@ @ @@
@  @ @ @   @ @ @
@  @ @  @  @ @   @

"""

# Menampilkan banner pada layar
print(banner)

def hitung_hasil_kali(list_data):
    hasil_kali = 1

    for nilai in list_data:
        hasil_kali *= nilai

    return hasil_kali

# Meminta pengguna untuk memasukkan nilai-nilai list
input_list = input("")
list_data = list(map(float, input_list.split(',')))

# Menghitung hasil kali
hasil_kali = hitung_hasil_kali(list_data)

# Menampilkan hasil
print(hasil_kali)

def hitung_string_sama(list_string):
    jumlah_string = 0

    for string in list_string:
        if len(string) >= 2 and string[0] == string[-1]:
            jumlah_string += 1

    return jumlah_string

# Contoh penggunaan
list_string = ["z", "xvc", "cac", "244"]
hasil = hitung_string_sama(list_string)

print(f"Terdapat {hasil} string yang memenuhi syarat")
import math

luas_lingkaran = lambda r: math.pi * r**2
jari_jari = float(input("Masukkan jari-jari: "))
hasil = luas_lingkaran(jari_jari)
print(f"Luas lingkaran = {hasil}")
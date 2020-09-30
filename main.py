from geometry.bangunruang import BangunRuang
from geometry.persegipanjang import PersegiPanjang
from geometry.segitiga import Segitiga

print('Menggunakan OOP')

p1 = PersegiPanjang(30,3)
print(p1.info())
print(p1.hitung_luas())

s3 = Segitiga(4, 8)
print(s3.info())
print(s3.hitung_luas())

print("\nMencoba membuat objek dari kelas BangunRuang")
b3 = BangunRuang()
print(b3.info())
print(b3.hitung_luas())

#Polymorphism = kemampuan object utk merespon berbeda, pada method yg sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s3)

print("\nPolymorphism")
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())
    print(bangun_ruang.hitung_luas())
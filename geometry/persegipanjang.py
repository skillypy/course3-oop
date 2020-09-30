from geometry.bangunruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        #fungsi yg di panggil pertama kali saat obel di ciptakan
        self.p = p
        self.l = l

    def info(self):
        return f'Ini adalah objek persegi panjang dgn panjang = {self.p} dan lebar = {self.l}'

    def hitung_luas(self):
        return self.p * self.l
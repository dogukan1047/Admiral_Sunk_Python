import random


class Game_Area():
    def __init__(self, n_satir, n_sutun):  # satir ve sutun boyutunu instance veriable olarak aldık
        self.n_satir = n_satir
        self.n_sutun = n_sutun
        self.savas_alani = self.init_savas_alani()
        self.bilgisyar_savas_alani = self.init_savas_alani()

    def init_savas_alani(self):  # savaş alanını satır sayısı ve sutun sayısına göre oluşturduk
        matris = []
        for satir in range(self.n_satir):
            matris.append(["-"] * self.n_sutun)
        return matris

    def __str__(self):
        satir_numaralari = list(range(1, self.n_satir + 1))  # satir numaralarından bir liste oluşturduk
        satir_numaralari = list(map(str, satir_numaralari))  # burada ise liste int oluştugundan bunu str çevirdik

        sutun_numaralari = list(range(1, self.n_sutun + 1))  # sutun numaralarından bir liste oluşturduk
        sutun_numaralari = list(map(str, sutun_numaralari))  # burada ise liste int oluştugundan bunu str çevirdik

        max_satir_numaralari = len(satir_numaralari[-1]) + 1  # en büyük satır numarasının uzunluğunu bulduk boşluklar için
        max_sutun_numaralari = len(sutun_numaralari[-1])      # en büyük sutun numarasının uzunluğunu bulduk boşluklar için
        bosluk_str = " " * max_satir_numaralari
        savas_alani_str = bosluk_str

        for sutun_numarasi in satir_numaralari:# listeyi okuduk
            bosluk_sayisi = max_sutun_numaralari - len(sutun_numarasi) + 1 # dinamik olarak savaş alanın boşluklarını hesapladık
            bosluk_str = " " * bosluk_sayisi
            savas_alani_str += sutun_numarasi + bosluk_str
        savas_alani_str += "\n"

        for satir_numarasi in satir_numaralari:
            satir = self.savas_alani[int(satir_numarasi) - 1]
            satir_alani_str = (max_sutun_numaralari * " ").join(satir)  # bir listedeki elemanları belli bir elemana göre birleştirir
            if int(satir_numarasi) < 10:
                savas_alani_str += satir_numarasi + "  " + satir_alani_str + "\n"
            else:
                savas_alani_str += satir_numarasi + " " + satir_alani_str + "\n"

        return savas_alani_str

import random


class Game_Area():
    def __init__(self, n_satir, n_sutun):  # satir ve sutun boyutunu instance veriable olarak aldık
        self.n_satir = n_satir
        self.n_sutun = n_sutun
        self.gemiSekli="O"
        self.savas_alani = self.init_savas_alani()
        self.bilgisyar_savas_alani = self.init_savas_alani()


    def gemi_yerlestir(self,gemi,satir_numara,sutun_numara,Yatay_dikey):
      for i in range(gemi):
        if Yatay_dikey=="yatay":
            self.savas_alani[satir_numara][sutun_numara+i]=self.gemiSekli
        else:
            self.savas_alani[satir_numara+i][sutun_numara ] = self.gemiSekli






    def init_savas_alani(self):  # savaş alanını satır sayısı ve sutun sayısına göre oluşturduk
        matris = []
        for satir in range(self.n_satir):
            matris.append(["-"] * self.n_sutun)
        return matris

    def __str__(self):
        my_Game_Area = self.savas_alani_olustur(self.savas_alani)
        pc_Game_Area = self.savas_alani_olustur(self.bilgisyar_savas_alani)

        my_Game_Area_liste = my_Game_Area.split("\n")  # \n göre ayırdı ve yeni bir liste oluşturdu
        pc_Game_Area_liste = pc_Game_Area.split("\n")  # \n göre ayırdı ve yeni bir liste oluşturdu
        fazla_karakter=len(str(self.n_sutun)) -1
        pc_Game_Area_liste[0]=pc_Game_Area_liste[0][fazla_karakter:]

        my_Game_Area_str=[(10*" ").join([kendi,diger]) for kendi,diger in zip(my_Game_Area_liste,pc_Game_Area_liste)]

        return "\n".join(my_Game_Area_str)

    def savas_alani_olustur(self, savas_alani):
        satir_numaralari = list(range( self.n_satir))  # satir numaralarından bir liste oluşturduk
        satir_numaralari = list(map(str, satir_numaralari))  # burada ise liste int oluştugundan bunu str çevirdik

        sutun_numaralari = list(range( self.n_sutun))  # sutun numaralarından bir liste oluşturduk
        sutun_numaralari = list(map(str, sutun_numaralari))  # burada ise liste int oluştugundan bunu str çevirdik

        max_satir_numaralari = len(
            satir_numaralari[-1]) + 1  # en büyük satır numarasının uzunluğunu bulduk boşluklar için
        max_sutun_numaralari = len(sutun_numaralari[-1])  # en büyük sutun numarasının uzunluğunu bulduk boşluklar için
        bosluk_str = " " * max_satir_numaralari
        savas_alani_str = bosluk_str

        for sutun_numarasi in sutun_numaralari:  # listeyi okuduk
            bosluk_sayisi = max_sutun_numaralari - len(
                sutun_numarasi) + 1  # dinamik olarak savaş alanın boşluklarını hesapladık
            bosluk_str = " " * bosluk_sayisi
            savas_alani_str += sutun_numarasi + bosluk_str
        savas_alani_str = savas_alani_str[:-len(bosluk_str)]
        savas_alani_str += "\n"

        for satir_numarasi in satir_numaralari:
            satir = savas_alani[int(satir_numarasi) - 1]
            satir_alani_str = (max_sutun_numaralari * " ").join(satir)  # bir listedeki elemanları belli bir elemana göre birleştirir
            if int(satir_numarasi) < 10:
                savas_alani_str += satir_numarasi + "  " + satir_alani_str + "\n"
            else:
                savas_alani_str += satir_numarasi + " " + satir_alani_str + "\n"

        return savas_alani_str

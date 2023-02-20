import random


def renkli_print(print_str, renk):
    renkler = {"kirmizi": 31, "yesil": 32, "sari": 33}
    renk_kodu = renkler[renk]
    return f"\033[1;{renk_kodu}m{print_str}\033[0m"


class Game_Area():
    def __init__(self, n_satir, n_sutun):  # satir ve sutun boyutunu instance veriable olarak aldık
        self.n_satir = n_satir
        self.n_sutun = n_sutun
        self.gemiSekli = "O"
        self.toplam_gemi_boyutu_noktalari = 0

        self.savas_alani = self.init_savas_alani()
        self.bilgisyar_savas_alani = self.init_savas_alani()

        self.savas_alanlari = {
            "kendi": self.savas_alani,
            "diger": self.bilgisyar_savas_alani
        }

        self.guncelleme_kodlari = {
            "karavana": renkli_print("x", "sari"),
            "isabet": renkli_print("x", "yesil"),
            "hasar": renkli_print("x", "kirmizi")

        }

    def gemi_yerlestir(self, gemi, satir_numara, sutun_numara, Yatay_dikey):
        for i in range(gemi):
            if Yatay_dikey == "yatay":
                self.savas_alani[satir_numara][sutun_numara + i] = self.gemiSekli
            else:
                self.savas_alani[satir_numara + i][sutun_numara] = self.gemiSekli

        self.toplam_gemi_boyutu_noktalari += gemi

    def girilen_koordinat_uygun_mu(self, boat, satir_numarasi, sutun_numarasi, yatay_dikey):
        self.gemi_savas_alanina_sigiyor_mu(boat, satir_numarasi, sutun_numarasi, yatay_dikey)

    def gemi_savas_alanina_sigiyor_mu(self, boat, satir_numarasi, sutun_numarasi, yatay_dikey):
        konum = sutun_numarasi if yatay_dikey == "yatay" else satir_numarasi  # yatay veya dikey olmasına göre konum bilgisine satır veya sutun boyutu atanır
        kenar = self.n_sutun if yatay_dikey == "yatay" else self.n_satir

        alan_yeterli_mi = self.savas_alani_yeterli_mi(boat, konum, kenar)

        pozisyon_dolu_mu = self.pozisyon_uygun_mu(boat, satir_numarasi, sutun_numarasi, yatay_dikey)

        if not alan_yeterli_mi or not pozisyon_dolu_mu:
            raise ValueError

    def savas_alani_yeterli_mi(self, boat, konum, kenar):
        if boat + konum >= kenar:
            return False
        return True

    def pozisyon_uygun_mu(self, boat, satir_numarasi, sutun_numarasi, yatay_dikey):
        for i in range(boat):
            if yatay_dikey == "yatay":
                sembol = self.savas_alani[satir_numarasi][sutun_numarasi + i]
            else:
                sembol = self.savas_alani[satir_numarasi + i][sutun_numarasi]
            if sembol == self.gemiSekli:
                return False
        return True

    def guncelle(self, satir_numarasi, sutun_numarasi, bilgisayar_savas_alani):
        if bilgisayar_savas_alani.savas_alani[satir_numarasi][sutun_numarasi] == self.gemiSekli:
            self._guncelle("diger", satir_numarasi, sutun_numarasi, "isabet")
            self.toplam_gemi_boyutu_noktalari -= 1
            bilgisayar_savas_alani._guncelle("kendi", satir_numarasi, sutun_numarasi, "hasar")
        else:
            self._guncelle("diger", satir_numarasi, sutun_numarasi, "karavana")
            bilgisayar_savas_alani._guncelle("kendi", satir_numarasi, sutun_numarasi, "karavana")

    def _guncelle(self, hangi, satir_numarasi, sutun_numarasi, sonuc):
        self.savas_alanlari[hangi][satir_numarasi][sutun_numarasi] = self.guncelleme_kodlari[sonuc]

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
        fazla_karakter = len(str(self.n_sutun)) - 1
        pc_Game_Area_liste[0] = pc_Game_Area_liste[0][fazla_karakter:]

        my_Game_Area_str = [(10 * " ").join([kendi, diger]) for kendi, diger in
                            zip(my_Game_Area_liste, pc_Game_Area_liste)]

        return "\n".join(my_Game_Area_str)

    def savas_alani_olustur(self, savas_alani):
        satir_numaralari = list(range(self.n_satir))  # satir numaralarından bir liste oluşturduk
        satir_numaralari = list(map(str, satir_numaralari))  # burada ise liste int oluştugundan bunu str çevirdik

        sutun_numaralari = list(range(0, self.n_sutun))  # sutun numaralarından bir liste oluşturduk
        sutun_numaralari = list(map(str, sutun_numaralari))  # burada ise liste int oluştugundan bunu str çevirdik

        max_satir_numaralari = len(
            satir_numaralari[-1]) + 1  # en büyük satır numarasının uzunluğunu bulduk boşluklar için
        max_sutun_numaralari = len(sutun_numaralari[-1])  # en büyük sutun numarasının uzunluğunu bulduk boşluklar için
        bosluk_str = " " * max_satir_numaralari
        savas_alani_str = bosluk_str

        for sutun_numarasi in sutun_numaralari:  # listeyi okuduk
            bosluk_sayisi = max_sutun_numaralari - len(sutun_numarasi) + 1  # dinamik olarak savaş alanın boşluklarını hesapladık
            bosluk_str = " " * bosluk_sayisi
            savas_alani_str += sutun_numarasi + bosluk_str
        savas_alani_str = savas_alani_str[:-len(bosluk_str)]
        savas_alani_str += "\n"

        for satir_numarasi in satir_numaralari:
            satir = savas_alani[int(satir_numarasi)]
            satir_alani_str = (max_sutun_numaralari * " ").join(
                satir)  # bir listedeki elemanları belli bir elemana göre birleştirir
            if int(satir_numarasi) < 10:
                savas_alani_str += satir_numarasi + "  " + satir_alani_str + "\n"
            else:
                savas_alani_str += satir_numarasi + " " + satir_alani_str + "\n"

        return savas_alani_str

    def atis_yapilan_koordinatlar_uygun_mu(self, satir_numarasi, sutun_numarasi):

        if not (0 <= satir_numarasi and satir_numarasi < self.n_satir):
            return False
        if not (0 <= sutun_numarasi and sutun_numarasi < self.n_sutun):
            return False

        yesil_x = self.guncelleme_kodlari["isabet"]
        sari_x = self.guncelleme_kodlari["karavana"]
        kirmizi_x = self.guncelleme_kodlari["hasar"]

        if self.bilgisyar_savas_alani[satir_numarasi][sutun_numarasi] in [yesil_x, sari_x]:
            return False

        return True

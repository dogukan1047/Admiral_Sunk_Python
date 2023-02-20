import random
from Game_Area import Game_Area
from Player import Player
from War_Boat import War_Boat


class Admiral_sunk:
    def __init__(self, n_satir, n_sutun, n_gemi):
        oyuncu_savas_alani = Game_Area(n_satir, n_sutun)
        bilgisayar_savas_alani = Game_Area(n_satir, n_sutun)

        self.gemiler = self.gemi_yarat(n_gemi)

        oyuncu_savas_gemileri = War_Boat(self.gemiler, oyuncu_savas_alani)
        bilgisayar_savas_gemileri = War_Boat(self.gemiler, bilgisayar_savas_alani)

        self.oyuncu = Player(oyuncu_savas_alani, oyuncu_savas_gemileri, False)
        self.bilgisayar = Player(bilgisayar_savas_alani, bilgisayar_savas_gemileri, True)

    def basla(self):
        rasgele_mi = self.rasgele_mi_manuel_mi()
        self.oyuncu.War_Boat.input_boat_coordinate(rastgele=rasgele_mi, bilgisayar_mi=False)
        self.bilgisayar.War_Boat.input_boat_coordinate(rastgele=True, bilgisayar_mi=True)
        while True:
            oyuncu_kazandi = self.oyuncu.play(self.bilgisayar)
            if oyuncu_kazandi:
                print(60*"*")
                print(60*"*")
                print("Tebrikler kazandiniz")
                print(60*"*")
                print(60*"*")
                break
            bilgisayar_kazandi = self.bilgisayar.play(self.oyuncu)

            if bilgisayar_kazandi:
                print(60 * "*")
                print(60 * "*")
                print("Kaybettiniz :_)")
                print(60 * "*")
                print(60 * "*")
                break

    @staticmethod
    def gemi_yarat(n_gemi):
        gemiler = list()
        for gemi in range(n_gemi):
            gemiler.append(random.randint(1, 5))

        return gemiler

    def rasgele_mi_manuel_mi(self):
        rasgele_mi = None
        while rasgele_mi is None:
            rasgele_mi = input("Savas gemilerinizi rasgele mi yerlestirmek istersiniz yoksa manuel mi ?(True or False)")

            if rasgele_mi not in ["True", "False"]:
                rasgele_mi = None
            else:
                bool_rasgele_mi = rasgele_mi == "True"
        return bool_rasgele_mi

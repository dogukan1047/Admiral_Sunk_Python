import random


class Player():
    def __init__(self, Game_Area, War_Boat, is_pc):
        self.savas_alani = Game_Area
        self.War_Boat = War_Boat
        self.is_pc = is_pc

    def play(self, bilgisayar):
        for i in range(3):
            satir_numarasi = None
            sutun_numarasi = None
            while satir_numarasi is None or sutun_numarasi is None:
                try:
                    if self.is_pc:
                        input_result = self.rastgele_konum_yarat()
                    else:
                        input_result = self.input_user_result()
                    satir_numarasi, sutun_numarasi= input_result.split(" ")
                    satir_numarasi = int(satir_numarasi)
                    sutun_numarasi = int(sutun_numarasi)

                except:
                    satir_numarasi = None
                    sutun_numarasi = None

                else:
                    self.savas_alani.guncelle(satir_numarasi, sutun_numarasi, bilgisayar.savas_alani)
        print(self.savas_alani)

    def input_user_result(self):
        input_result = input(f" lütfen atis yapmak istediginiz satir ve sutun koordinatlarini giriniz:")
        return input_result

    def rastgele_konum_yarat(self):
        satir_numarasi = random.randint(0, self.savas_alani.n_satir-1)
        sutun_numarasi = random.randint(0, self.savas_alani.n_sutun-1)
        input_result=f"{satir_numarasi} {sutun_numarasi} "
        return input_result

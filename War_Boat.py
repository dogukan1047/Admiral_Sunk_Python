import random


class War_Boat():
    def __init__(self, boat, game_area):
        self.boat = boat  # [3,5,7,4] gemiler bir liste ve her sayı gemi uzunluğunu belirtiyor
        self.savas_alani = game_area

    def input_boat_coordinate(self, rastgele=False,bilgisayar_mi=False):
        for boat in self.boat:
            satir_numarasi = None
            sutun_numarasi = None
            yatay_dikey = None
            while satir_numarasi is None or sutun_numarasi is None or yatay_dikey is None:
                try:
                    if rastgele:
                        input_result=self.rastgele_konum_yarat()
                    else:
                        input_result = self.input_user_result(boat)
                    satir_numarasi, sutun_numarasi, yatay_dikey = input_result.split(" ")
                    if yatay_dikey not in ["yatay", "dikey"]:
                        raise ValueError
                    satir_numarasi = int(satir_numarasi)
                    sutun_numarasi = int(sutun_numarasi)
                    self.savas_alani.girilen_koordinat_uygun_mu(boat, satir_numarasi, sutun_numarasi,yatay_dikey)
                except:
                    if not rastgele:
                        print("Yanlis deger girdiniz lütfren acıklamayı dikkatlice okuyunuz :")
                    satir_numarasi = None
                    sutun_numarasi = None
                    yatay_dikey = None

                else:
                    self.savas_alani.gemi_yerlestir(boat, satir_numarasi, sutun_numarasi, yatay_dikey)
        if not bilgisayar_mi:
            print(self.savas_alani)

    def input_user_result(self, boat):
        input_result = input(f""" 
Lutfen aralarında boşluk bırakarak {boat} boyutundaki geminizini savaş alanında nereye koymak istediğinizi giriniz:. 
Girilen degerler sıarsıyla : satır_numarası(int) , sutun_numarası(int) ,yatay yada dikey(str) ,
savas alanınızın şu anki hali:
{self.savas_alani} 
                  """)
        return input_result

    def rastgele_konum_yarat(self):
        satir_numarasi = random.randint(0,self.savas_alani.n_satir-1)
        sutun_numarasi = random.randint(0,self.savas_alani.n_sutun-1)
        yatay_dikey=random.choice(["yatay","dikey"])
        return f"{satir_numarasi} {sutun_numarasi} {yatay_dikey}"
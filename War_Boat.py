class War_Boat():
    def __init__(self, boat, game_area):
        self.boat = boat  # [3,5,7,4] gemiler bir liste ve her sayı gemi uzunluğunu belirtiyor
        self.game_area = game_area

    def input_boat_coordinate(self):
        for boat in self.boat:
            satir_numarasi = None
            sutun_numarasi = None
            yatay_dikey = None
            while satir_numarasi is None or sutun_numarasi is None or yatay_dikey is None:
                try:
                    input_result = self.input_user_result(boat)
                    satir_numarasi, sutun_numarasi, yatay_dikey = input_result.split(" ")
                    satir_numarasi = int(satir_numarasi)
                    sutun_numarasi = int(sutun_numarasi)
                except:
                    print("Yanlis deger girdiniz lütfren acıklamayı dikkatlice okuyunuz :")
                    satir_numarasi = None
                    sutun_numarasi = None
                    yatay_dikey = None

                else:
                    self.game_area.gemi_yerlestir(boat, satir_numarasi, sutun_numarasi, yatay_dikey)
        print(self.game_area)

    def input_user_result(self, boat):
        input_result = input(f""" 
Lutfen aralarında boşluk bırakarak {boat} boyutundaki geminizini savaş alanında nereye koymak istediğinizi giriniz:. 
Girilen degerler sıarsıyla : satır_numarası(int) , sutun_numarası(int) ,yatay yada dikey(str) ,
savas alanınızın şu anki hali:
 {self.game_area} 
                  """)
        return input_result

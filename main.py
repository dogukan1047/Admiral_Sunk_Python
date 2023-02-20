from Game_Area import Game_Area
from Player import Player
from War_Boat import War_Boat


savas_alanim=Game_Area(15,15)
bilgisayar_savas_alani=Game_Area(15,15)



gemiler=[3,5,7]

savas_gemim=War_Boat(gemiler,savas_alanim)
savas_gemim.input_boat_coordinate(rastgele=True,bilgisayar_mi=False)

bilgisayar_savas_gemileri=War_Boat(gemiler,bilgisayar_savas_alani)
bilgisayar_savas_gemileri.input_boat_coordinate(rastgele=True,bilgisayar_mi=True)

player1=Player(savas_alanim,savas_gemim,False)
bilgisayar=Player(bilgisayar_savas_alani,savas_gemim,True)

player1.play(bilgisayar)
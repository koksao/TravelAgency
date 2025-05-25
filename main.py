#### BIBLIOTECZKI: pydantic, email-validator

from Classes import Dodatki, Klient, Rezerwacja, Wariant, Wycieczka, Transport
from datetime import date

Klient1_Tomek = Klient(imie="Tomek",nazwisko="Kozlowski",email="tomekkoz@o2.pl")

Trans1 = Transport(typ="bus",koszt=100)

Dod1_Zakopane = Dodatki(tytul="Zwiedzanie Morskiego Oka", termin=date(2025,6,6),koszt=100,liczba_miejsc=5)

War1_Zakopane = Wariant(termin=date(2025,6,5),koszt=1500,ilosc_miejsc=5,lista_dodatkow=[Dod1_Zakopane],opis="bóbr")

Wyc1_Zakopane = Wycieczka(tytul="Wycieczka grupowa do zakopanego",organizator="Jamal Jamal", lokalizacja="Zakopane",warianty=[War1_Zakopane])

Rez1_Zakopane_Tomek = Rezerwacja(klient=Klient1_Tomek,dodatki=[Dod1_Zakopane], wariant=War1_Zakopane,data_zakupu=date(2025,5,1))

print(Rez1_Zakopane_Tomek)
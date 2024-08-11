import numpy as np
import pandas as pd
import seaborn as sns

class Film:
    def __init__(self):
        self.data=pd.read_csv("C:/Users/Emir Kaçar/Desktop/netflix_titles.csv", sep=';', on_bad_lines='skip')
    
    def bilgileriGoster(self):
        print(f"{self.data.head(5)}")
    
    def sutunlariGoster(self):
        print(f"{self.data.columns}")

    def oyunculariGoster(self):
        oyuncular = self.data["cast"].unique().tolist()
        print(oyuncular[0:6])

        
    def oyuncularinOynadigiFilmler(self,oyuncu):
        if "cast " not in self.data.columns:
            print("Dataframe'de cast isimli sutun bulunamadi.")

        filmler = self.data[self.data["cast"].str.contains(oyuncu, na=False, case=False)]
        if(not filmler.empty):
            print(f"{oyuncu} adali oyuncunun rol aldigi filmler")
            print(filmler.head(5))
        else:
            print(f"{oyuncu} adli oyuncunun rol aldigi film bulunamadi.")

    def ulkelereGoreFilmListele(self,ulkeIsmi):
        
        if(ulkeIsmi in self.data["country"].values):
            filmler=self.data[self.data["country"]==ulkeIsmi]
            print("Cekilen filmler")
            print(filmler.head(5))
        else:
            print(f"{ulkeIsmi} adli ulke bulunamadi.")
    
    def cekilenUlkeleriListele(self):
        print(f"{self.data["country"].unique()}")
    
    def oyuncularinOynadigiFilmlerBaskaSekilde  (self):
        # Oyuncularin oynadigi filmleri gruplandir.
        oyuncu_filmler = self.data.groupby("cast")["title"].apply(list)
        
        # Her oyuncu ve onun oynadigi film.
        for oyuncu, filmler in oyuncu_filmler.items():
            print(f"'{oyuncu}' oyuncusunun oynadigi filmler:")
            for film in filmler:
                print(f" - {film}")
            print()  # Her oyuncudan sonra bos bir satir birakilmis hali.
        print(oyuncu_filmler)

film=Film()

film.oyuncularinOynadigiFilmlerBaskaSekilde()


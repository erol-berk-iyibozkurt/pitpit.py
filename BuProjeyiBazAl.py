import pandas as pd
import seaborn as sns


class Film:
    def __init__(self):
        try:
            self.data = pd.read_csv("/Users/erolberkiyibozkurt/Desktop/netflix_titles.csv", on_bad_lines='skip')
        except FileNotFoundError:
            print(f"Hata: Dosya bulunamadi.Lutfen dogru yolu girin.")
            self.data = None  # Veri yoksa `data` None olarak ayarlanır.

        self.favori_liste = []  # Favori film listesini tutar.
        
    def bilgileriGoster(self):
        if self.data is not None:
           print(self.data.head())
        else:
           print("Veri yok.Lutfen dosya yolunun dogru oldugundan emin olun.")
    
    def filmEkle(self,filmAdi):
        if self.data is not None:
            if filmAdi in self.data['title'].values:
                self.favori_liste.append(filmAdi)
                print(f"{filmAdi} adlı film favori listenize eklendi.")
            else:
                print(f"{filmAdi} adlı film verilerde bulunamadı.")
        else:
            print("Veri yok.Film eklemek için once verileri yükleyin.")
    
    def yilaGoreFilmler(self, yil):  #Yila gore filmleri listeler.
        if self.data is not None:
            yil_filmleri = self.data[self.data['release_year'] == yil]
            return yil_filmleri
        else:
            print("Veri yok.Film aramak için once verileri yukleyin.")
            return None

    def favoriListeyiGoster(self):
        if len(self.favori_liste) > 0:
            print("Favori Filmleriniz:")
            for film in self.favori_liste:
                print(film)
        else:
            print("Henüz favori film eklemediniz.")
    
  
    def ulkelereGoreFilmSayisi(self):   #Ulkeye gore filmleri listeler.
        if self.data is not None:
            ulke_sayilari = self.data['country'].value_counts()
            print("Ulkelere Göre Film Sayilari:\n", ulke_sayilari.head(10))
        else:
            print("Veri yok.Ulkelere göre film sayisini gormek icin verileri yükleyin.")
    
    def verilerinSutunlariniGoster(self): #Sutunlari gormeliyiz ki sutunlara gore islem yapabilelim.
        if (self.data is not None):
            print(f"{self.data.columns}")
        else:
            print("Veri yok.")
    
    def tureGoreFilmler(self,tur):  #Belirli bir turdeki filmleri listeler.
        if self.data is not None:
            turFilmler=self.data[self.data["listed_in"].str.contains(tur, case=False)]
            if not turFilmler.empty:
                print(turFilmler[['title', 'release_year']])
            else:
                print(f"{tur} türünde film bulunamadı.")
        else:
            print("Veri yok.")
            
        
    def menu(self):
        while True:
            print("\n1. Veri Bilgilerini Göster")
            print("2. Favori Film Ekle")
            print("3. Yila Göre Filmler")
            print("4. Ulkelere Göre Film Sayısı")
            print("5. Favori Listeyi Göster")
            print("6. Verilerin Sutunlarini Goster")
            print("7. Ture gore filmleri listele")
            print("7. Cikis")
            secim = input("Bir secim yapin: ")
            
            if secim == '1':
                self.bilgileriGoster()
            elif secim == '2':
                film_adi = input("Eklenecek film adini giriniz: ")
                self.filmEkle(film_adi)
            elif secim == '3':
                yil = int(input("Yili girin: "))
                print(self.yilaGoreFilmler(yil))
            elif secim == '4':
                self.ulkelereGoreFilmSayisi()
            elif secim == '5':
                self.favoriListeyiGoster()
            elif secim == '6':
                self.verilerinSutunlariniGoster()
            elif secim== '7':
                tur=input("Turu giriniz: ")
                self.tureGoreFilmler(tur)
            else:
                print("Gecersiz secim. Tekrar deneyin.")

# Programı çalıştır.
film = Film()
film.menu()




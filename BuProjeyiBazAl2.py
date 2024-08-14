import pandas as pd
import seaborn as sns
import numpy as np


class Film:
    def __init__(self):
        try:
            self.data = pd.read_csv("/Users/erolberkiyibozkurt/Desktop/IMDB-Movie-Data.csv", on_bad_lines='skip')
        except FileNotFoundError:
            print(f"Hata: Dosya bulunamadi.Lutfen dogru yolu girin.")
            self.data = None  # Veri yoksa `data` None olarak ayarlanır.

        self.favori_liste = []  # Favori film listesini tutar.
        
    def bilgileriGoster(self):
        print("\n1. Tüm Listeyi göster \n2. ilk 5 filmi göster \n 3. Son 5 filmi göster \n 4. ilk ... filmi göster \n 5. Son ... filmi göster")
        choice = input("Kaç filmi daha görüntülemek istersiniz? (Lütfen sayı giriniz): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print(pd.DataFrame(self.data))
            elif choice == 2:
                return self.data.head(5)
            elif choice == 3:
                return self.data.tail(5)
            elif choice == 4:
                x = int(input("Kaç tane veri görmek istersiniz?"))
                return self.data.head(x)
            elif choice == 5:
                x = int(input("Kaç tane veri görmek istersiniz?"))
                return self.data.tail(x)
            else:
                print("İstediğiniz iişlemi gerçekleştiremedik. Lütfen tekrar deneyin.")
        else:
            print("Geçersiz bir işlem yapmaktasınız. Litfen bir numara giriniz.")
    
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

    def filmoner(self):
        print("\n1. Seçtiğim Filme göre film öner.")
        print("2. Rastgele Film öner")
        secim = int(input("Bir secim yapin: "))
        if secim == 1:
            filmAdi = input("Film adını girin: ")
            oneriler = self.filmeGoreOneri(filmAdi)
            if oneriler is not None:
                print("Önerilen Filmler:")
                print(oneriler[['Title', 'Genre', 'Director', 'Actors', 'Rating', 'Öneri Yüzdesi']].head(6))
            else:
                print("Öneri bulunamadı.")
        elif secim == 2:
            self.rastgeleFilm()
    
    # Daha deyatlı bilgi için planlama.ipynb dosyasında algoritma çalışma prensibine bakabilirsiniz
    def filmeGoreOneri(self, filmAdi):
        # Seçilecek filmi csv doyası içinde bulur ve ayri bir DataFrame oluşturulur.
        secilen_film = self.data[self.data['Title'].str.contains(filmAdi, case=False)]
        
        # Film yok ise;
        if secilen_film.empty:
            print(f"{filmAdi} adlı film verilerde bulunamadı.")
            return
        
        # Seçilen film ismindeki DataFrame'deki ilk filmi seçme
        secilen_film = secilen_film.iloc[0]
        
        #Öneri Puanı isminde bir sütun oluşturulur
        self.data['Öneri Puanı'] = 0
        
        # iterrows her satır içinde döngüyü (loop'u) sağlar
        # DataFrame içinde satır satır dönme sağlanır
        # i değişkeni satır belirtir
        # film değişkeni satır içindeki verileri belirtir (esas veri içindeki teker teker dönen kısım)
        for i, film in self.data.iterrows():
            # En baştaki puan 0 olarak tanımlanır
            puan = 0
            
            # Title puanı için
            if secilen_film['Title'][0] in film['Title']:
                puan += 70
            
            # Genre puanı için
            if secilen_film['Genre'] == film['Genre']:
                puan += 25
            
            # Yönetmen puanı için
            if secilen_film['Director'] == film['Director']:
                puan += 15
            
            # Aktör ve Aktris puanı için
            # Ortak aktör ve aktrisler set tipinde saklanarak her biri tek bir kere set tipinde bulunur
            # Karşılaştırmada '&' ile her ikisinde bulunursa set kısmına eklenmiş olur.
            ortak_aktorler = set(secilen_film['Actors'].split(',')) & set(film['Actors'].split(','))
            puan += len(ortak_aktorler) * 10
            
            # Rating puanı için
            if film['Rating'] > secilen_film['Rating']:
                puan += 10
            
            # Puanı güncelle
            # at DataFrame içinde (bu örnekte i satırını ve 'Öneri Puanı' sütununun) güncellenmesi sağlanır
            self.data.at[i, 'Öneri Puanı'] = puan
        
        # Önerme puanını Önerme Yüzdesine çevirme
        max_puan = 70+25+15+(10* len(ortak_aktorler))+10  # Maksimum puan
        self.data['Öneri Yüzdesi'] = (self.data['Öneri Puanı'] / max_puan)
        
        # Öneri Yüzdesini en yüksekten en düşüğe göre sırala
        oneriler = self.data.sort_values('Öneri Yüzdesi', ascending=False)
        return oneriler

    def rastgeleFilm(self):
        row_count = len(self.data)
        randomNumbers = np.random.randint(1,row_count)
        print(self.data.iloc[randomNumbers-1 :randomNumbers])
        if self.data is not None:
            row_count = len(self.data)
            random_index = np.random.randint(0, row_count)
            print(self.data.iloc[random_index])
        else:
            print("Veri yok. Rastgele film önerisi yapmak için verileri yükleyin.")       
        
    def menu(self):
        while True:
            print("\n1. Veri Bilgilerini Göster")
            print("2. Favori Film Ekle")
            print("3. Yila Göre Filmler")
            print("4. Ulkelere Göre Film Sayısı")
            print("5. Favori Listeyi Göster")
            print("6. Verilerin Sutunlarini Goster")
            print("7. Ture gore filmleri listele")
            print("8. Film öner")
            print("9. Cikis")
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
            elif secim =='8':
                self.filmoner()
            elif secim =='9':
                break
            else:
                print("Gecersiz secim. Tekrar deneyin.")

# Programı çalıştır.

def main(): 
    film = Film()
    film.menu()

main()
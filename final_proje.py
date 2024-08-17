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
        self.favori_filmler = {}  # Kullanıcıya bağlı favori film listelerini tutar.

    def kullanici_olustur(self):
        self.kullanici_adi = input("Lütfen bir kullanıcı adı girin: ")
        self.favori_filmler[self.kullanici_adi] = []
        
    def bilgileriGoster(self):
        print("\n1. Tüm Listeyi göster \n2. ilk 5 filmi göster \n3. Son 5 filmi göster \n4. ilk ... filmi göster \n5. Son ... filmi göster\n6. Kullanıcı hesabı")
        choice = input("Kaç filmi daha görüntülemek istersiniz? (Lütfen sayı giriniz): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print(self.data)
            elif choice == 2:
                print(self.data.head(5))
            elif choice == 3:
                print(self.data.tail(5))
            elif choice == 4:
                x = int(input("Kaç tane veri görmek istersiniz?"))
                print( self.data.head(x))
            elif choice == 5:
                x = int(input("Kaç tane veri görmek istersiniz?"))
                print(self.data.tail(x))
            elif choice == 6:
                pass
            else:
                print("İstediğiniz iişlemi gerçekleştiremedik. Lütfen tekrar deneyin.")
        else:
            print("Geçersiz bir işlem yapmaktasınız. Litfen bir numara giriniz.")
    
    def favori_film_ekle(self):
        film_adi = input("Favori Listenize Eklemek İstediğiniz Filmi Arayın: ")

        # Film adını içeren filmleri filtrele
        bulunan_filmler = self.data[self.data['Title'].str.contains(film_adi, case=False, na=False)]

        if bulunan_filmler.empty:
            print(f"{film_adi} ile eşleşen film bulunamadı.")
            return

        # İlk 10 sonucu göster
        print("Bulunan Filmler:")
        for i, (idx, row) in enumerate(bulunan_filmler.head(10).iterrows(), 1):
            print(f"{i}. {row['Title']} ({row['Year']})")

        # Kullanıcıdan seçim yapmasını iste
        secim = input("Eklemek istediğiniz filmin numarasını girin: ")

        if not secim.isdigit() or int(secim) < 1 or int(secim) > min(10, len(bulunan_filmler)):
            print("Geçersiz seçim. İşlem iptal edildi.")
            return

        # Seçilen filmi favori listeye ekle
        secim_index = int(secim) - 1
        secilen_film = bulunan_filmler.iloc[secim_index]
        self.favori_filmler[self.kullanici_adi].append(secilen_film['Title'])
        print(f"{secilen_film['Title']} favori listenize eklendi.")
    
    def yilaGoreFilmler(self, yil):  #Yila gore filmleri listeler.
        if self.data is not None:
            yil_filmleri = self.data[self.data['Year'] == yil]
            return yil_filmleri
        else:
            print("Veri yok.Film aramak için once verileri yukleyin.")
            return None

    def favoriListeyiGoster(self):
        if self.kullanici_adi in self.favori_filmler and len(self.favori_filmler[self.kullanici_adi]) > 0:
            print(f"{self.kullanici_adi}'nın Favori Filmleri:")
            for film in self.favori_filmler[self.kullanici_adi]:
                print(film)
        else:
            print("Henüz favori film eklemediniz.")

    def yonetmeneGoreFilmler(self, yonetmen):  # Yönetmene göre filmleri listeler.
        if self.data is not None:
            yonetmen_filmleri = self.data[self.data['Director'].str.contains(yonetmen, case=False)]
            if not yonetmen_filmleri.empty:
                print(yonetmen_filmleri[['Title', 'Year', 'Director']])
            else:
                print(f"{yonetmen} yönetmenine ait film bulunamadı.")
        else:
            print("Veri yok.")
    
    def yonetmenleriListele(self):
        if self.data is not None:
            yonetmenler = self.data['Director'].value_counts()
            print("Yönetmenler:\n", yonetmenler.head(20))
        else:
            print("Veri yok.")

    def yonetmenAltMenu(self):
        print("\n1. Yönetmenleri Listele")
        print("2. Yönetmene Göre Film Ara")
        secim = input("Bir seçim yapın: ")
        
        if secim == '1':
            self.yonetmenleriListele()
        elif secim == '2':
            yonetmen_adi = input("Yönetmen adını girin: ")
            self.yonetmeneGoreFilmler(yonetmen_adi)
        else:
            print("Geçersiz seçim. Tekrar deneyin.")

    def oyuncuyaGoreFilmler(self, oyuncu):
        if self.data is not None:
            oyuncu_filmleri = self.data[self.data['Actors'].str.contains(oyuncu, case=False)]
            if not oyuncu_filmleri.empty:
                print(oyuncu_filmleri[['Title', 'Year', 'Actors']])
            else:
                print(f"{oyuncu} aktörüne ait film bulunamadı.")
        else:
            print("Veri yok.")

    def oyunculariListele(self):
        if self.data is not None:
            oyuncular = self.data['Actors'].str.split(',').explode().str.strip().value_counts()
            print("Oyuncular:\n", oyuncular.head(20))
        else:
            print("Veri yok.")

    def oyuncuAltMenu(self):
        print("\n1. Oyuncuları Listele")
        print("2. Oyuncuya Göre Film Ara")
        secim = input("Bir seçim yapın: ")
        
        if secim == '1':
            self.oyunculariListele()
        elif secim == '2':
            oyuncu_adi = input("Oyuncu adını girin: ")
            self.oyuncuyaGoreFilmler(oyuncu_adi)
        else:
            print("Geçersiz seçim. Tekrar deneyin.")
    
    def verilerinSutunlariniGoster(self): #Sutunlari gormeliyiz ki sutunlara gore islem yapabilelim.
        if (self.data is not None):
            print(f"{self.data.columns}")
        else:
            print("Veri yok.")
    
    def tureGoreFilmler(self, tur):  
        if self.data is not None:
            # Tür sütunundaki filmleri ayırıp, filtreleme yapacağız
            turFilmler = self.data[self.data['Genre'].str.contains(tur, case=False, na=False)]
            if not turFilmler.empty:
                print(f"{tur} türünde bulunan filmler:")
                print(turFilmler[['Title', 'Year', 'Genre']])
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
                print("Tespit edilen Film:")
                print(oneriler[['Title', 'Genre', 'Director', 'Actors', 'Rating', 'Öneri Yüzdesi']].head(1))
                print("Önerilen Filmler:")
                print(oneriler[['Title', 'Genre', 'Director', 'Actors', 'Rating', 'Öneri Yüzdesi']].iloc[1:6])
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
        self.kullanici_olustur()
        print(f"Hoşgeldin {self.kullanici_adi}, \n ---")
        while True:
            print("\n1. Veri Bilgilerini Göster")
            print("2. Favori Film Ekle")
            print("3. Yila Göre Filmler")
            print("4. Yönetmene göre Filmler")
            print("5. Favori Listeyi Göster")
            print("6. oyuncuya göre Filmler")
            print("7. Ture gore filmleri listele")
            print("8. Film öner")
            print("9. Cikis")
            secim = input("Bir secim yapin: ")
            
            if secim == '1':
                self.bilgileriGoster()
            elif secim == '2':
                self.favori_film_ekle()
            elif secim == '3':
                yil = int(input("Yili girin: "))
                print(self.yilaGoreFilmler(yil))
            elif secim == '4':
                self.yonetmenAltMenu()
            elif secim == '5':
                self.favoriListeyiGoster()
            elif secim == '6':
                self.oyuncuAltMenu()
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
import pandas as pd
import random
from datetime import datetime

class FilmChatbot:
    def __init__(self):
        try:
            self.veri = pd.read_csv("netflix_titles.csv", on_bad_lines='skip')
        except FileNotFoundError:
            print("Hata: Dosya bulunamadı. 'netflix_titles.csv' dosyasının doğru konumda olduğundan emin olun.")
            self.veri = None
        
        self.kullanici_tercihleri = {}

    def kullaniciyi_selamla(self):
        print("Film Öneri Chatbot'una Hoş Geldiniz!")
        ad = input("Lütfen adınızı girin: ")
        soyad = input("Lütfen soyadınızı girin: ")
        tam_ad = f"{ad} {soyad}"
        if tam_ad not in self.kullanici_tercihleri:
            self.kullanici_tercihleri[tam_ad] = {"izlenen_filmler": []}
        return tam_ad

    def gorevi_acikla(self):
        print("\nSize çeşitli kriterlere göre film önerileri sunmak için buradayım.")
        print("Yönetmenlerden, oyunculara, çıkış yıllarına ve daha fazlasına göre film önerebilirim.")
        print("Gelecekte daha iyi öneriler sunmak için tercihlerinizi hatırlayacağım.")

    def menu_goster(self):
        print("\nSize nasıl yardımcı olabilirim?")
        print("1. Yönetmene göre")
        print("2. Oyuncuya göre")
        print("3. Çıkış yılına göre")
        print("4. Tüm filmler listesinden")
        print("5. Rastgele")
        print("6. Bu ay çıkan filmler")
        print("7. Çıkış")

    def kullanici_secimini_al(self):
        while True:
            try:
                secim = int(input("Seçiminizi girin (1-7): "))
                if 1 <= secim <= 7:
                    return secim
                else:
                    print("Geçersiz seçim. Lütfen 1 ile 7 arasında bir sayı girin.")
            except ValueError:
                print("Geçersiz giriş. Lütfen bir sayı girin.")

    def yonetmene_gore_oner(self):
        yonetmen = input("Yönetmenin adını girin: ")
        filmler = self.veri[self.veri['director'].str.contains(yonetmen, case=False, na=False)]
        return self.onerileri_formatla(filmler)

    def oyuncuya_gore_oner(self):
        oyuncu = input("Oyuncunun adını girin: ")
        filmler = self.veri[self.veri['cast'].str.contains(oyuncu, case=False, na=False)]
        return self.onerileri_formatla(filmler)

    def yila_gore_oner(self):
        yil = input("Çıkış yılını girin: ")
        filmler = self.veri[self.veri['release_year'] == int(yil)]
        return self.onerileri_formatla(filmler)

    def listeden_oner(self):
        print("Veritabanımızdan 10 rastgele film:")
        ornek_filmler = self.veri.sample(10)
        for i, (_, film) in enumerate(ornek_filmler.iterrows(), 1):
            print(f"{i}. {film['title']} ({film['release_year']})")
        
        secim = int(input("İlgilendiğiniz filmin numarasını girin: "))
        secilen_film = ornek_filmler.iloc[secim - 1]
        return self.icerik_bazli_filtreleme(secilen_film)

    def rastgele_oner(self):
        return self.onerileri_formatla(self.veri.sample(5))

    def bu_ay_cikan_filmler(self):
        mevcut_ay = datetime.now().month
        filmler = self.veri[pd.to_datetime(self.veri['date_added']).dt.month == mevcut_ay]
        return self.onerileri_formatla(filmler)

    def onerileri_formatla(self, filmler):
        if len(filmler) == 0:
            return pd.DataFrame(), "Kriterlere uyan film bulunamadı."
        
        oneriler = filmler.sample(min(5, len(filmler)))
        return oneriler[['title', 'release_year', 'director', 'cast', 'description']], "İşte önerileriniz:"

    def icerik_bazli_filtreleme(self, film):
        def benzerlik_hesapla(satir):
            puan = 0
            if satir['director'] == film['director']:
                puan += 2
            if satir['country'] == film['country']:
                puan += 1
            if satir['type'] == film['type']:
                puan += 1
            if set(satir['listed_in'].split(', ')) & set(film['listed_in'].split(', ')):
                puan += 2
            return puan

        self.veri['benzerlik'] = self.veri.apply(benzerlik_hesapla, axis=1)
        benzer_filmler = self.veri.sort_values('benzerlik', ascending=False).head(6)
        benzer_filmler = benzer_filmler[benzer_filmler['title'] != film['title']]
        
        benzer_filmler['eslesme_yuzdesi'] = (benzer_filmler['benzerlik'] / 6) * 100
        return benzer_filmler[['title', 'release_year', 'director', 'cast', 'description', 'eslesme_yuzdesi']], f"{film['title']} filmine benzer filmler:"

    def calistir(self):
        kullanici_adi = self.kullaniciyi_selamla()
        self.gorevi_acikla()

        while True:
            self.menu_goster()
            secim = self.kullanici_secimini_al()

            if secim == 7:
                print("Film Öneri Chatbot'unu kullandığınız için teşekkürler. Güle güle!")
                break

            oneri_df, mesaj = pd.DataFrame(), ""
            if secim == 1:
                oneri_df, mesaj = self.yonetmene_gore_oner()
            elif secim == 2:
                oneri_df, mesaj = self.oyuncuya_gore_oner()
            elif secim == 3:
                oneri_df, mesaj = self.yila_gore_oner()
            elif secim == 4:
                oneri_df, mesaj = self.listeden_oner()
            elif secim == 5:
                oneri_df, mesaj = self.rastgele_oner()
            elif secim == 6:
                oneri_df, mesaj = self.bu_ay_cikan_filmler()

            print(mesaj)
            if not oneri_df.empty:
                print(oneri_df.to_string(index=False))
            else:
                print("Üzgünüm, bu kriterlere uygun film bulunamadı.")
            
            izlenen_film = input("Bu filmlerden herhangi birini izlediniz mi? Evet ise başlığı girin (veya 'hayır'): ")
            if izlenen_film.lower() != 'hayır':
                self.kullanici_tercihleri[kullanici_adi]["izlenen_filmler"].append(izlenen_film)
                print(f"Harika! '{izlenen_film}' filminizi izlenen listesine ekledim.")

            baska_oneri = input("Başka bir öneri ister misiniz? (evet/hayır): ")
            if baska_oneri.lower() != 'evet':
                print("Film Öneri Chatbot'unu kullandığınız için teşekkürler. Güle güle!")
                break

if __name__ == "__main__":
    chatbot = FilmChatbot()
    chatbot.calistir()
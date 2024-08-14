import pandas as pd
import numpy as np


veri = pd.read_csv("/Users/erolberkiyibozkurt/Desktop/IMDB-Movie-Data.csv", on_bad_lines='skip')

#veri.head()

def tümfilmler():
    print("\n1. Tüm Listeyi göster \n2. ilk 5 filmi göster \n 3. Son 5 filmi göster \n 4. ilk ... filmi göster \n 5. Son ... filmi göster")
    choice = input("Verilerimizi nasıl görüntülemek istersiniz? (Lütfen sayı giriniz): ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            return pd.DataFrame(veri)
        elif choice == 2:
            return veri.head(5)
        elif choice == 3:
            return veri.tail(5)
        elif choice == 4:
            x = int(input("Kaç tane veri görmek istersiniz? "))
            return veri.head(x)
        elif choice == 5:
            x = int(input("Kaç tane veri görmek istersiniz? "))
            return veri.tail(x)
        else:
            print("İstediğiniz iişlemi gerçekleştiremedik. Lütfen tekrar deneyin.")
    else:
        print("Geçersiz bir işlem yapmaktasınız. Litfen bir numara giriniz.")

def rastgele_filmler():
    row_count = sum(1 for row in veri)
    randomNumbers = np.random.randint(row_count)

tümfilmler()

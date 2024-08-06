
import numpy as np

# Film bilgilerini tanımla
# Film bilgilerinin tanimlanmasi.
filmler = np.array([
    ["Film A", "Yönetmen 1", "Oyuncu 1, Oyuncu 2", "Tür 1", "2010", "8.2"],
    ["Film B", "Yönetmen 2", "Oyuncu 3, Oyuncu 4", "Tür 2", "2012", "7.5"],
    ["Film C", "Yönetmen 3", "Oyuncu 5, Oyuncu 6", "Tür 1", "2015", "9.0"],
    ["Film D", "Yönetmen 4", "Oyuncu 7, Oyuncu 8", "Tür 3", "2018", "8.0"],
    ["Film E", "Yönetmen 5", "Oyuncu 9, Oyuncu 10", "Tür 2", "2020", "7.8"]
])


filmAdlari=filmler[:,0]
yonetmenler=filmler[:,1]
oyuncular=filmler[:,2]
turler=filmler[:,3]
yillar=filmler[:,4]
puanlar=filmler[:,5].astype(float)

enYuksekPuanIndex=np.argmax(puanlar)
enYuksekPuanFilm=filmAdlari[enYuksekPuanIndex]
enYuksekPuan=puanlar[enYuksekPuanIndex]
enYuksekPuanYonetmen=yonetmenler[enYuksekPuanIndex]
enYuksekPuanOyuncular=oyuncular[enYuksekPuanIndex]
enYuksekPuanTur=turler[enYuksekPuanIndex]
enYuksekPuanYil=yillar[enYuksekPuanIndex]


print("Filmler ve bilgiler:")

for i in range(len(filmAdlari)):
    print(f"Film:{filmAdlari[i]} Yonetmen: {yonetmenler[i]} Oyuncular: {oyuncular[i]} Turu: {turler[i]} Yil:{yillar[i]} Aldigi Puan: {puanlar[i]}")

print("En Cok Puan Alan Film")
print(f"Film Adi:{enYuksekPuanFilm}")
print(f"Filmin Yonetmeni: {enYuksekPuanYonetmen}")
print(f"Filmin Oyunculari : {enYuksekPuanOyuncular}")
print(f"Filmin Turu: {enYuksekPuanTur}")
print(f"Filmin yayinlandigi yil: {enYuksekPuanYil}")
print(f"Filmin aldigi puan {enYuksekPuan}")







import numpy as np

#Bir sinema salonu simülasyonu.
class SinemaSalonu:
    def __init__(self, satirSayisi, sutunSayisi):
        """
        SinemaSalonu sinifinin yapici metodu.
        Belirtilen boyutlarda bir sinema salonu oluşturur.

        Args:
        satirsayisi (int): Salonun satir sayisi.
        sutunSayisi (int): Salonun sütun sayisi.
        """
        self.satirSayisi = satirSayisi
        self.sutunSayisi = sutunSayisi
        self.salon = np.zeros((satirSayisi, sutunSayisi), dtype=int)
    
    def koltukRezerveEt(self, satir, sutun):
        """
        Belirtilen koltugu rezerve eder.

        Args:
        satir (int): Rezerve edilecek koltuğun satir numarasi.
        sutun (int): Rezerve edilecek koltuğun sütun numarasi.

        Returns:
        bool: Rezervasyon basarili ise True, degilse False.
        """
        if self.salon[satir, sutun] == 0:
            self.salon[satir, sutun] = 1
            return True
        else:
            return False

    def koltukDurumu(self):
        """
        Salonun koltuk durumunu gosterir.

        Returns:
        numpy.ndarray: Salonun koltuk durumunu iceren matris.
        """
        return self.salon
    
    def bosKoltuklar(self):
        """
        Bos koltuklarin listesini döndürür.

        Returns:
        list: Boş koltuklarin (satir, sütun) koordinatlarini iceren liste.
        """
        bosKoltuklar = []
        for i in range(self.satirSayisi):
            for j in range(self.sutunSayisi):
                if self.salon[i, j] == 0:
                    bosKoltuklar.append((i, j))
        return bosKoltuklar
    
# Örnek kullanım
satirSayisi = 5
sutunSayisi = 5

# Sinema salonunu olustur
salon = SinemaSalonu(satirSayisi, sutunSayisi)

# Bazı koltuklari rezerve et
salon.koltukRezerveEt(2, 3)
salon.koltukRezerveEt(0, 1)
salon.koltukRezerveEt(4, 4)

# Salonun koltuk durumunu goster
print("Salonun koltuk durumu:")
print(salon.koltukDurumu())

# Bos koltukları göster
print("Boş koltuklar:")
print(salon.bosKoltuklar())
    

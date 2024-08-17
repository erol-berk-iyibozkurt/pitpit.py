## PıtPıt.Py Ekibi Sunar

<img src="images/PıtPıt.Py.png" alt="Logo PıtPıt.Py" width="250" height="250"/>


# Film Öneri ve Yönetim Sistemi

Bu proje, IMDB film veritabanını csv formatındaki bir dosyadan kullanarak kullanıcılara çeşitli film işlemleri ve önerileri sunan bir Python projesi olması amacıyla tasarlandı. Proje ürünümüzün adı Pıtırflix.

## Özellikler

- Kullanıcı hesabı oluşturma
- Film bilgilerini görüntüleme
- Favori film ekleme ve listeleme
- Yıla göre film arama
- Yönetmene göre film arama
- Oyuncuya göre film arama
- Türe göre film listeleme
- Film önerisi alma (seçilen filme göre veya rastgele)

gibi özellikleri menü yardımıyla gerçekleştirirken menü içinde detaylı bir şekilde film dünyasını keşfedebilirsiniz. 

## Kurulum

1. Python 3.x'in yüklü olduğundan emin olun.
2. Gerekli kütüphaneleri yükleyin:
- pandas
- numphy
- seaborn

## Film Önerme Algoritması

Puan bazlı 

- 70P Başlık benzerliği
- 25P aynı Genre
- 15P Aynı yönetmen
- 10P * her aynı oyuncu
- 10P seçilen filmden yüksek rating

Örnek:

- **Seçilen Film:** Star Wars 1

Star Wars 2 + 70P
aynı Genre + 25P
aynı yönetmen 15P
aynı oyuncular kaç tanes ise x 10P
daha yüksek puanlı ise 10P alır

Sonra yüzde olması için toplam puana filmin puanı bölünür.

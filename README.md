# letterboxMutual

Letterboxd kullanıcıları arasında **ortak (mutual)** film/geçmiş karşılaştırması yapan Python tabanlı bir araç.  
Amaç: İki kullanıcının izledikleri/oyladıkları filmleri karşılaştırıp ortakları raporlamak ve bunları kolayca görüntülemek.

> Bu README, deponun mevcut dosya yapısına göre hazırlanmıştır ve **hazır kullanıma** uygundur. Bilinmeyen kısımlar boş bırakılmıştır.

---

## 🔧 Kurulum

```bash
git clone https://github.com/Roalexx/letterboxMutual.git
cd letterboxMutual
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Çalıştırma

### GUI
```bash
python gui.py
```

### CLI
```bash
python main.py
```

> Çalıştırdıktan sonra iki Letterboxd kullanıcı adı girerek karşılaştırma yapabilirsiniz. (Varsa GUI üzerinde ilgili alanlara giriniz.)

---

## 📁 Proje Yapısı

```
letterboxMutual/
├─ gui.py                 # Basit arayüz (GUI) ile kullanıcı adı girişi ve sonuç gösterimi
├─ main.py                # Komut satırı (CLI) çalıştırma noktası
├─ letterboxd_scraper.py  # Letterboxd sayfalarından veri toplama/sayfa işleme
├─ movie_functions.py     # Karşılaştırma/filtreleme/yardımcı fonksiyonlar
└─ requirements.txt       # Bağımlılıklar
```

---

## 📝 Kullanım Notları

- İnternet bağlantısı gereklidir.
- Letterboxd HTML yapısı değişirse scraper fonksiyonlarını güncellemeniz gerekebilir.
- Çoklu isteklerde gecikme (sleep) ve tekrar deneme (retry) stratejisi kullanmanız önerilir.
- Yüksek hacimli tarama yapmayın; kişisel kullanım için makul aralıklarla çalıştırın.

---

## 🔒 Yasal/Uyumluluk

- Bu araç yalnızca **kişisel kullanım** içindir.
- Letterboxd kullanım şartlarına ve robots yönergelerine saygı gösterin.
- Toplanan verileri üçüncü kişilerle paylaşmadan önce ilgili izinleri alınız.

---

## 🤝 Katkı

1. Fork → yeni branch (`feat/xyz`) açın  
2. Kod standartlarına uyarak geliştirin  
3. Açıklayıcı bir Pull Request gönderin




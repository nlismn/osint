OSINT

Termux üzerinde çalışan, kullanıcı adı ve isim araştırması için geliştirilmiş interaktif bir OSINT aracı.

Public kaynaklarda kullanıcı adı ve isim araştırması yapmayı kolaylaştırmak için tasarlanmıştır. Araç, desteklenen platformları kontrol eder, HTTP yanıtlarını gösterir ve sonuçların yorumlanmasına yardımcı olan interaktif bir yardım sistemi sunar.

«Not: Bu araç yalnızca kamuya açık bilgiler üzerinde araştırma amacıyla kullanılmalıdır.»

---

Özellikler

- 🔎 Kullanıcı adı araştırması
- 👤 İsim araştırması
- 🌐 Çok sayıda public platformda profil kontrolü
- 📊 HTTP durum kodlarının gösterilmesi
- ⚡ Eşzamanlı platform taraması
- 🎨 Renkli terminal arayüzü
- 📚 İnteraktif yardım sistemi
- 🛠️ Otomatik kurulum scripti
- 🚀 "osint" komutu ile doğrudan çalıştırma
- ❓ "osint help" ile detaylı yardım

Desteklenen platformlar

Araç; sosyal medya, geliştirici platformları, video/streaming servisleri, oyun platformları, yaratıcı platformlar ve çeşitli topluluk servislerinde public profil URL'lerini kontrol edebilir.

Desteklenen platformlar proje sürümlerine göre değişebilir.

---

Gereksinimler

- Android
- Termux
- Python 3
- Git
- İnternet bağlantısı

Python tarafında kullanılan harici paket:

requests

"install.sh" gerekli Python bağımlılıklarını otomatik olarak kurar.

---

Kurulum

Termux'u açın.

1. Repoyu klonlayın

git clone https://github.com/nlismn/osint.git

2. Proje klasörüne girin

cd osint

3. Kurulum scriptini çalıştırın

bash install.sh

Kurulum tamamlandığında "osint" komutu kullanılabilir hale gelir.

4. Programı başlatın

osint

---

Kullanım

Program başlatıldığında ana menü görüntülenir:

1) Yeni arama
2) Help
0) Çıkış

Kullanıcı adı araştırması

"Yeni arama" seçeneğini kullanarak araştırmak istediğiniz kullanıcı adını girin.

Araç, desteklenen public platformları eşzamanlı olarak kontrol eder.

Örneğin:

Kullanıcı adı: example

Sonuçlar platformlara göre gösterilir.

---

Sonuçların Anlamı

Tarama sırasında aşağıdaki sonuç türleri görülebilir:

✓ Bulundu
✗ Bulunamadı
? 403
? 429
? TIMEOUT
? BAĞLANTI HATASI

"✓ Bulundu"

Sunucu, profil URL'sinin mevcut olduğuna işaret eden bir HTTP yanıtı vermiştir.

Bu sonuç profilin araştırılan kişiye ait olduğunu kesin olarak kanıtlamaz.

"✗ Bulunamadı"

Sunucu genellikle profilin mevcut olmadığını belirten bir yanıt vermiştir.

"403"

Sunucu isteği reddetmiştir.

Bunun nedeni erişim kısıtlaması, bot koruması veya platform politikaları olabilir.

"429"

Çok fazla istek gönderildiği için hız sınırlaması uygulanmış olabilir.

"TIMEOUT"

Sunucudan belirlenen süre içerisinde yanıt alınamamıştır.

"BAĞLANTI HATASI"

Ağ bağlantısı veya sunucu iletişimi sırasında hata oluşmuştur.

---

İsim Araştırması

İsim araştırması, arama motorları ve platformlara özel arama bağlantıları oluşturmak için kullanılabilir.

Örneğin bir isim için:

Google
Bing
DuckDuckGo
Brave

gibi arama motorlarında araştırma yapılabilir.

Ayrıca platforma özel arama sorguları oluşturularak public sonuçların bulunması kolaylaştırılabilir.

---

Yardım Sistemi

Detaylı yardım merkezini açmak için:

osint help

Ana program içerisinden de:

2) Help

seçeneği kullanılabilir.

Yardım merkezi şu konuları içerir:

[1] OSINT nedir?
[2] Kullanıcı adı araştırması
[3] İsim araştırması
[4] Platformlar
[5] HTTP durum kodları
[6] Sonuçları yorumlama
[7] OSINT doğrulama
[8] Güvenli kullanım
[9] Komutlar
[0] Ana menüye dön

Platformlara özel yardım bölümleri de bulunmaktadır.

---

OSINT Doğrulama

Bir kullanıcı adı veya profil bulunduğunda sonucu tek başına kesin kimlik bilgisi olarak değerlendirmeyin.

Daha güvenilir araştırma için farklı public kaynaklardaki bilgileri karşılaştırın.

Örneğin:

Kullanıcı adı
        ↓
Platform profili
        ↓
Public profil bilgileri
        ↓
Public bağlantılar
        ↓
Diğer bağımsız kaynaklar
        ↓
Sonuçların karşılaştırılması

Aynı kullanıcı adının farklı platformlarda bulunması tek başına aynı kişinin kullanıldığını kanıtlamaz.

---

Güvenli Kullanım

Bu proje yalnızca kamuya açık bilgilerin araştırılması amacıyla kullanılmalıdır.

Aşağıdaki işlemler bu aracın kullanım amacı değildir:

- Özel hesaplara erişmeye çalışma
- Parola veya kimlik bilgisi ele geçirme
- Oturum çerezleri veya token toplama
- Erişim kontrollerini aşma
- Yetkisiz sistemlere erişme
- Gizli veya özel bilgileri elde etmeye çalışma

Araştırma yaparken ilgili platformların kullanım şartlarına ve yürürlükteki yasalara uyun.

---

Güncelleme

Projeyi daha önce klonladıysanız:

cd ~/osint
git pull
bash install.sh

Ardından:

osint

komutuyla güncel sürümü çalıştırabilirsiniz.

---

Proje Yapısı

osint/
├── bin/
│   └── osint
├── install.sh
├── osint.py
└── osint_help.py

"osint.py"

Ana OSINT uygulamasını içerir.

"osint_help.py"

İnteraktif yardım merkezini içerir.

"install.sh"

Kurulum işlemlerini otomatikleştirir.

"bin/osint"

"osint" komutunun çalıştırılmasını sağlar.

---

Komutlar

Programı başlat

osint

Yardım merkezini aç

osint help

Projeyi güncelle

cd ~/osint
git pull
bash install.sh

---

Teknik Bilgiler

Program Python ile geliştirilmiştir.

Kullanılan temel Python modülleri:

requests
concurrent.futures
urllib.parse
os
sys
time

Platform kontrollerinde eşzamanlı istekler kullanılarak tarama süresi azaltılmaya çalışılır.

Sonuçlar HTTP yanıtlarına ve bağlantı durumlarına göre sınıflandırılır.

---

Katkıda Bulunma

Projeyi geliştirmek isteyenler GitHub üzerinden katkıda bulunabilir.

Öneriler, hata bildirimleri ve geliştirme fikirleri için GitHub Issues kullanılabilir.

Yeni platform desteği eklerken:

- Platformun public profil URL yapısını kontrol edin.
- Özel hesaplara erişmeye çalışmayın.
- Platformun kullanım şartlarını dikkate alın.
- HTTP yanıtlarının yanlış pozitif üretebileceğini göz önünde bulundurun.

---

Proje

GitHub:
https://github.com/nlismn/osint

Repository:
"nlismn/osint"

---

Lisans

Bu proje için henüz ayrı bir açık kaynak lisansı belirtilmemiştir.

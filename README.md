OSINT

Termux üzerinde çalışan, kullanıcı adı ve isim araştırması için geliştirilmiş bir OSINT aracıdır.

Özellikler

- Kullanıcı adı araştırması
- Çok sayıda public platformda profil kontrolü
- İsim araştırması için arama motoru bağlantıları
- HTTP durum kodlarının gösterilmesi
- İnteraktif yardım sistemi
- Renkli terminal arayüzü
- Otomatik kurulum
- "osint" ve "osint help" komutları

Kurulum

Termux'u açın ve:

git clone https://github.com/nlismn/osint.git
cd osint
bash install.sh

Kurulum tamamlandıktan sonra:

osint

komutuyla programı başlatabilirsiniz.

Yardım

Detaylı yardım menüsünü açmak için:

osint help

Yardım menüsünde kullanıcı adı araştırması, platformlar, HTTP durum kodları, sonuçların yorumlanması ve doğrulama gibi bölümler bulunur.

Kullanım

Programı başlatın:

osint

Ana menüden:

1) Yeni arama
3) Help
0) Çıkış

seçeneklerini kullanabilirsiniz.

Kullanıcı adı araştırması

Araştırmak istediğiniz kullanıcı adını girin.

Araç, desteklenen public platformları kontrol ederek bulunan ve bulunamayan profilleri gösterir.

İsim araştırması

İsim araştırması, arama motorları ve platforma özel arama bağlantıları oluşturmak için kullanılabilir.

HTTP Durum Kodları

Araştırma sırasında bazı sonuçlar şu şekilde gösterilebilir:

✓ Bulundu
✗ Bulunamadı
? 403
? 429
? TIMEOUT
? BAĞLANTI HATASI

Bunlar tek başına kesin kimlik doğrulaması anlamına gelmez. Özellikle "403" ve "429" durumlarında platformun erişim veya hız sınırlaması olabilir.

Güvenli Kullanım

Bu araç yalnızca kamuya açık bilgiler üzerinde araştırma amacıyla kullanılmalıdır.

Özel hesaplara erişmeye, kimlik doğrulamasını aşmaya, parolaları veya oturum bilgilerini ele geçirmeye ya da erişim kontrollerini atlatmaya yönelik kullanılmamalıdır.

Bir profilin gerçekten araştırılan kişiye ait olduğunu varsaymadan önce sonuçlar farklı kaynaklardan doğrulanmalıdır.

Güncelleme

Projeyi daha önce klonladıysanız:

cd osint
git pull
bash install.sh

Ardından:

osint

ile güncel sürümü çalıştırabilirsiniz.

Proje Yapısı

osint/
├── bin/
│   └── osint
├── install.sh
├── osint.py
└── osint_help.py

Gereksinimler

- Android
- Termux
- Python 3
- Git
- Python "requests" paketi

"install.sh" gerekli Python bağımlılığını otomatik olarak kurar.

Lisans

Bu proje için henüz ayrı bir açık kaynak lisansı belirtilmemiştir.

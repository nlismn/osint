import os
import sys
import time


# ============================================================
# RENKLER
# ============================================================

RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"


# ============================================================
# YARDIMCI FONKSİYONLAR
# ============================================================

def clear():
    os.system("clear")


def pause():
    input(
        f"\n{GRAY}Devam etmek için ENTER'a bas...{RESET}"
    )


def header(title):
    clear()

    print(
        f"{CYAN}{BOLD}"
        "╔════════════════════════════════════════════════════════════╗"
        f"{RESET}"
    )

    print(
        f"{CYAN}{BOLD}║{RESET}"
        f"{WHITE}{BOLD}{title:^58}{RESET}"
        f"{CYAN}{BOLD}║{RESET}"
    )

    print(
        f"{CYAN}{BOLD}"
        "╚════════════════════════════════════════════════════════════╝"
        f"{RESET}"
    )

    print()


def section(title):
    print(
        f"\n{CYAN}{BOLD}"
        f"  {title}"
        f"{RESET}"
    )

    print(
        f"{GRAY}  "
        "──────────────────────────────────────────────────────────"
        f"{RESET}"
    )


def option(number, text):
    print(
        f"  {BLUE}{BOLD}[{number}]{RESET}"
        f" {WHITE}{text}{RESET}"
    )


def info(title, text):
    print(
        f"\n{GREEN}{BOLD}  {title}{RESET}"
    )

    for line in text.split("\n"):
        print(
            f"{GRAY}      {line}{RESET}"
        )


def warning(text):
    print(
        f"\n{YELLOW}{BOLD}  ! UYARI{RESET}"
    )

    for line in text.split("\n"):
        print(
            f"{YELLOW}      {line}{RESET}"
        )


# ============================================================
# ANA HELP MENÜSÜ
# ============================================================

def help_menu():
    while True:
        header("OSINT HELP CENTER")

        print(
            f"{GRAY}"
            "  OSINT aracını kullanmak için hangi konuda yardım"
            " almak istediğini seç."
            f"{RESET}"
        )

        section("YARDIM KONULARI")

        option("1", "OSINT nedir?")
        option("2", "Kullanıcı adı araştırması")
        option("3", "İsim araştırması")
        option("4", "Platformlar")
        option("5", "HTTP durum kodları")
        option("6", "Sonuçları yorumlama")
        option("7", "OSINT doğrulama")
        option("8", "Güvenli kullanım")
        option("9", "Komutlar")
        option("0", "Ana menüye dön")

        print()

        choice = input(
            f"{CYAN}{BOLD}  Seçim: {RESET}"
        ).strip()

        if choice == "1":
            osint_info()

        elif choice == "2":
            username_help()

        elif choice == "3":
            name_help()

        elif choice == "4":
            platform_menu()

        elif choice == "5":
            http_help()

        elif choice == "6":
            result_help()

        elif choice == "7":
            verification_help()

        elif choice == "8":
            safety_help()

        elif choice == "9":
            command_help()

        elif choice == "0":
            return

        else:
            print(
                f"\n{RED}  Geçersiz seçim.{RESET}"
            )
            time.sleep(1)


# ============================================================
# 1 - OSINT NEDİR?
# ============================================================

def osint_info():
    header("OSINT NEDİR?")

    section("AÇIK KAYNAK İSTİHBARATI")

    print(
        f"{WHITE}"
        "  OSINT, herkese açık kaynaklardan bilgi toplama ve"
        " analiz etme\n"
        "  yöntemidir.\n\n"
        "  Bu araç özellikle herkese açık kullanıcı profillerini,"
        " profil\n"
        "  bağlantılarını ve arama motoru sonuçlarını araştırmaya"
        " yardımcı olur."
        f"{RESET}"
    )

    info(
        "ÖRNEK KAYNAKLAR",
        "Sosyal medya profilleri\n"
        "Arama motorları\n"
        "Public GitHub repository'leri\n"
        "Public forum gönderileri\n"
        "Public geliştirici profilleri\n"
        "Public portföyler"
    )

    warning(
        "Bir bilginin internette bulunması, o bilginin doğru olduğu"
        " anlamına gelmez.\n"
        "Kaynaklar mümkün olduğunca doğrulanmalıdır."
    )

    pause()


# ============================================================
# 2 - KULLANICI ADI
# ============================================================

def username_help():
    header("KULLANICI ADI ARAŞTIRMASI")

    section("KULLANICI ADI NE İŞE YARAR?")

    print(
        f"{WHITE}"
        "  Kullanıcı adı, farklı platformlarda aynı veya benzer"
        " şekilde\n"
        "  kullanılmış olabilir.\n\n"
        "  Araç, girilen kullanıcı adı için desteklenen"
        " platformlarda\n"
        "  herkese açık profil adreslerini kontrol eder."
        f"{RESET}"
    )

    info(
        "ARAŞTIRILABİLECEK BİLGİLER",
        "Profilin mevcut olup olmadığı\n"
        "Profil URL'si\n"
        "HTTP durum kodu\n"
        "Platformun erişim durumu\n"
        "Herkese açık profil açıklamaları"
    )

    warning(
        "Aynı kullanıcı adının iki platformda bulunması,"
        " hesapların aynı kişiye ait olduğunu kanıtlamaz."
    )

    pause()


# ============================================================
# 3 - İSİM
# ============================================================

def name_help():
    header("İSİM ARAŞTIRMASI")

    section("İSİM ARAMASI")

    print(
        f"{WHITE}"
        "  İsim araması, arama motorlarında herkese açık olarak"
        " indekslenmiş\n"
        "  sonuçları bulmaya yardımcı olur.\n\n"
        "  Araç, doğrudan bir kişinin kimliğini doğrulamaz."
        f"{RESET}"
    )

    info(
        "ARAMA MOTORLARI",
        "Google\n"
        "Bing\n"
        "DuckDuckGo\n"
        "Brave Search"
    )

    info(
        "PLATFORM ARAMASI",
        "Instagram\n"
        "X\n"
        "YouTube\n"
        "TikTok\n"
        "GitHub\n"
        "Reddit\n"
        "LinkedIn"
    )

    warning(
        "Aynı isme sahip kişilerin birbirinden farklı kişiler"
        " olabileceğini unutma."
    )

    pause()
# ============================================================
# 4 - PLATFORM MENÜSÜ
# ============================================================

def platform_menu():
    while True:
        header("PLATFORM YARDIMI")

        print(
            f"{GRAY}"
            "  Hangi platform hakkında yardım almak istiyorsun?"
            f"{RESET}\n"
        )

        section("SOSYAL")

        option("1", "Instagram")
        option("2", "X")
        option("3", "TikTok")
        option("4", "Facebook")
        option("5", "Reddit")
        option("6", "Telegram")

        section("VİDEO / YAYIN")

        option("7", "YouTube")
        option("8", "Twitch")
        option("9", "Kick")

        section("GELİŞTİRİCİ")

        option("10", "GitHub")
        option("11", "GitLab")
        option("12", "Dev.to")
        option("13", "Medium")
        option("14", "Hugging Face")
        option("15", "Kaggle")

        section("OYUN")

        option("16", "Steam")
        option("17", "Roblox")
        option("18", "Chess.com")
        option("19", "Lichess")

        section("TASARIM / YARATICI")

        option("20", "Behance")
        option("21", "Dribbble")
        option("22", "ArtStation")
        option("23", "DeviantArt")
        option("24", "SoundCloud")

        section("DİĞER")

        option("25", "Linktree")
        option("26", "Patreon")
        option("27", "Ko-fi")

        option("0", "Geri")

        print()

        choice = input(
            f"{CYAN}{BOLD}  Seçim: {RESET}"
        ).strip()

        if choice == "1":
            instagram_help()

        elif choice == "2":
            x_help()

        elif choice == "3":
            tiktok_help()

        elif choice == "4":
            facebook_help()

        elif choice == "5":
            reddit_help()

        elif choice == "6":
            telegram_help()

        elif choice == "7":
            youtube_help()

        elif choice == "8":
            twitch_help()

        elif choice == "9":
            kick_help()

        elif choice == "10":
            github_help()

        elif choice == "11":
            gitlab_help()

        elif choice == "12":
            devto_help()

        elif choice == "13":
            medium_help()

        elif choice == "14":
            huggingface_help()

        elif choice == "15":
            kaggle_help()

        elif choice == "16":
            steam_help()

        elif choice == "17":
            roblox_help()

        elif choice == "18":
            chess_help()

        elif choice == "19":
            lichess_help()

        elif choice == "20":
            behance_help()

        elif choice == "21":
            dribbble_help()

        elif choice == "22":
            artstation_help()

        elif choice == "23":
            deviantart_help()

        elif choice == "24":
            soundcloud_help()

        elif choice == "25":
            linktree_help()

        elif choice == "26":
            patreon_help()

        elif choice == "27":
            kofi_help()

        elif choice == "0":
            return

        else:
            print(
                f"\n{RED}  Geçersiz seçim.{RESET}"
            )
            time.sleep(1)


# ============================================================
# PLATFORM YARDIMLARI - 1
# ============================================================

def instagram_help():
    header("INSTAGRAM")

    info(
        "KULLANICI ADI",
        "Herkese açık profil adresini belirler."
    )

    info(
        "BIO",
        "Kullanıcının kendi yazdığı herkese açık açıklamadır."
    )

    info(
        "WEB SİTESİ / BAĞLANTILAR",
        "Kullanıcının kendi eklediği diğer herkese açık"
        " bağlantıları gösterebilir."
    )

    info(
        "GÖNDERİLER",
        "Kullanıcının herkese açık olarak paylaştığı içerikleri"
        " gösterir."
    )

    info(
        "PROFİL FOTOĞRAFI",
        "Herkese açık profil görselidir."
    )

    warning(
        "Özel hesapların içeriğine erişim sağlamaya çalışılmaz."
    )

    pause()


def x_help():
    header("X")

    info(
        "KULLANICI ADI",
        "Hesabın herkese açık profil adresini oluşturur."
    )

    info(
        "BIO",
        "Kullanıcının kendi yazdığı herkese açık açıklamadır."
    )

    info(
        "WEB SİTESİ",
        "Kullanıcının kendi eklediği herkese açık bağlantıyı"
        " gösterebilir."
    )

    info(
        "GÖNDERİLER",
        "Herkese açık paylaşımları incelemeye yardımcı olur."
    )

    pause()


def tiktok_help():
    header("TIKTOK")

    info(
        "KULLANICI ADI",
        "Herkese açık profil adresini belirler."
    )

    info(
        "BIO",
        "Kullanıcının kendi yazdığı profil açıklamasıdır."
    )

    info(
        "VİDEOLAR",
        "Herkese açık video içeriklerini gösterir."
    )

    info(
        "BAĞLANTILAR",
        "Kullanıcının kendi eklediği diğer platformları"
        " gösterebilir."
    )

    pause()


def facebook_help():
    header("FACEBOOK")

    info(
        "PROFİL",
        "Herkese açık profil bilgilerini gösterebilir."
    )

    info(
        "PUBLIC GÖNDERİLER",
        "Kullanıcının herkese açık bıraktığı gönderileri"
        " gösterebilir."
    )

    info(
        "PROFİL BAĞLANTISI",
        "Herkese açık profil adresidir."
    )

    pause()


def reddit_help():
    header("REDDIT")

    info(
        "KULLANICI ADI",
        "Herkese açık Reddit profil adresini oluşturur."
    )

    info(
        "PUBLIC POST",
        "Kullanıcının herkese açık gönderilerini gösterir."
    )

    info(
        "PUBLIC COMMENT",
        "Kullanıcının herkese açık yorumlarını gösterebilir."
    )

    info(
        "SUBREDDIT",
        "Herkese açık topluluk aktivitelerini anlamaya yardımcı"
        " olabilir."
    )

    pause()


def telegram_help():
    header("TELEGRAM")

    info(
        "KULLANICI ADI",
        "Herkese açık kullanıcı adı profil bağlantısını"
        " oluşturabilir."
    )

    info(
        "PUBLIC PROFİL",
        "Platformun herkese açık olarak sunduğu bilgilerle"
        " sınırlıdır."
    )

    warning(
        "Kullanıcı adı bulunması özel Telegram bilgilerine"
        " erişim anlamına gelmez."
    )

    pause()


def youtube_help():
    header("YOUTUBE")

    info(
        "KANAL ADI",
        "Kanalın herkese açık görünen ismidir."
    )

    info(
        "HANDLE",
        "Kanalın herkese açık profil adresini belirler."
    )

    info(
        "KANAL AÇIKLAMASI",
        "Kanal sahibinin kendi yazdığı herkese açık bilgileri"
        " içerebilir."
    )

    info(
        "VİDEO AÇIKLAMALARI",
        "Kullanıcının kendi eklediği herkese açık bağlantıları"
        " içerebilir."
    )

    info(
        "SOSYAL BAĞLANTILAR",
        "Kanal sahibinin kendi eklediği diğer platformları"
        " gösterebilir."
    )

    pause()


def twitch_help():
    header("TWITCH")

    info(
        "KULLANICI ADI",
        "Herkese açık kanal adresini belirler."
    )

    info(
        "KANAL AÇIKLAMASI",
        "Yayıncının kendi yazdığı bilgileri gösterebilir."
    )

    info(
        "SOSYAL BAĞLANTILAR",
        "Yayıncının kendi eklediği diğer platformları"
        " gösterebilir."
    )

    pause()


def kick_help():
    header("KICK")

    info(
        "KULLANICI ADI",
        "Herkese açık kanal adresini belirler."
    )

    info(
        "PROFİL",
        "Yayıncının herkese açık profil bilgilerini gösterebilir."
    )

    pause()
# ============================================================
# PLATFORM YARDIMLARI - 2
# GELİŞTİRİCİ PLATFORMLARI
# ============================================================

def github_help():
    header("GITHUB")

    info(
        "KULLANICI ADI",
        "Herkese açık GitHub profil adresini belirler."
    )

    info(
        "PUBLIC REPOSITORY",
        "Kullanıcının herkese açık projelerini incelemeye"
        " yardımcı olabilir."
    )

    info(
        "README",
        "Proje hakkında kullanıcı tarafından yazılmış"
        " herkese açık bilgileri içerebilir."
    )

    info(
        "PROFİL BİLGİLERİ",
        "Bio, public repository'ler ve kullanıcının kendi"
        " eklediği bağlantılar görülebilir."
    )

    info(
        "OSINT İPUCU",
        "Aynı kullanıcı adının farklı platformlarda kullanılması"
        " araştırma için başlangıç noktası olabilir."
    )

    warning(
        "Private repository veya private hesap içeriklerine"
        " erişmeye çalışılmaz."
    )

    pause()


def gitlab_help():
    header("GITLAB")

    info(
        "KULLANICI ADI",
        "Herkese açık profil adresini belirler."
    )

    info(
        "PUBLIC PROJECT",
        "Kullanıcının herkese açık projelerini gösterebilir."
    )

    info(
        "README / DOKÜMANLAR",
        "Proje hakkında public teknik bilgiler içerebilir."
    )

    info(
        "PROFİL",
        "Kullanıcının public profil bilgilerini ve bağlantılarını"
        " gösterebilir."
    )

    pause()


def devto_help():
    header("DEV.TO")

    info(
        "KULLANICI ADI",
        "Geliştiricinin herkese açık profil adresini belirler."
    )

    info(
        "BIO",
        "Kullanıcının kendi yazdığı public profil açıklamasıdır."
    )

    info(
        "YAZILAR",
        "Kullanıcının public olarak yayınladığı teknik yazıları"
        " incelemeye yardımcı olur."
    )

    info(
        "TAGS",
        "Yazılarda kullanılan teknik konular hakkında fikir"
        " verebilir."
    )

    pause()


def medium_help():
    header("MEDIUM")

    info(
        "KULLANICI ADI",
        "Herkese açık profil adresini belirleyebilir."
    )

    info(
        "YAZILAR",
        "Kullanıcının public olarak yayınladığı makaleleri"
        " gösterebilir."
    )

    info(
        "BIO",
        "Kullanıcının kendi yazdığı public açıklamadır."
    )

    info(
        "YAYINLAR",
        "Kullanıcının katkıda bulunduğu public yayınları"
        " anlamaya yardımcı olabilir."
    )

    pause()


def huggingface_help():
    header("HUGGING FACE")

    info(
        "KULLANICI ADI",
        "Herkese açık profil adresini belirler."
    )

    info(
        "MODELLER",
        "Kullanıcının public olarak yayınladığı modelleri"
        " gösterebilir."
    )

    info(
        "DATASET",
        "Kullanıcının public olarak yayınladığı veri setlerini"
        " gösterebilir."
    )

    info(
        "SPACES",
        "Kullanıcının public projelerini ve demolarını"
        " gösterebilir."
    )

    info(
        "PROFİL",
        "Bio ve kullanıcının kendi eklediği public bilgileri"
        " içerebilir."
    )

    pause()


def kaggle_help():
    header("KAGGLE")

    info(
        "KULLANICI ADI",
        "Herkese açık Kaggle profil adresini belirler."
    )

    info(
        "PUBLIC NOTEBOOK",
        "Kullanıcının herkese açık notebook çalışmalarını"
        " gösterebilir."
    )

    info(
        "COMPETITIONS",
        "Public yarışmalardaki görünür katılım bilgileri"
        " araştırmaya yardımcı olabilir."
    )

    info(
        "DATASET",
        "Kullanıcının public olarak yayınladığı veri setlerini"
        " gösterebilir."
    )

    pause()


# ============================================================
# PLATFORM YARDIMLARI - 3
# OYUN PLATFORMLARI
# ============================================================

def steam_help():
    header("STEAM")

    info(
        "KULLANICI ADI",
        "Public Steam profil adresini belirleyebilir."
    )

    info(
        "PUBLIC PROFİL",
        "Kullanıcının herkese açık bıraktığı profil bilgilerini"
        " gösterebilir."
    )

    info(
        "PUBLIC OYUN BİLGİLERİ",
        "Profil gizlilik ayarlarına bağlı olarak bazı oyun"
        " bilgileri görülebilir."
    )

    warning(
        "Steam'de görünürlük gizlilik ayarlarına bağlıdır."
    )

    pause()


def roblox_help():
    header("ROBLOX")

    info(
        "KULLANICI ADI",
        "Herkese açık kullanıcı profilini bulmaya yardımcı olabilir."
    )

    info(
        "PUBLIC PROFİL",
        "Platformun public olarak gösterdiği profil bilgilerini"
        " içerebilir."
    )

    info(
        "PUBLIC İÇERİK",
        "Kullanıcının herkese açık bıraktığı içerikler"
        " araştırılabilir."
    )

    warning(
        "Kullanıcının private bilgilerinin bulunması veya"
        " erişim kısıtlamalarının aşılması OSINT değildir."
    )

    pause()


def chess_help():
    header("CHESS.COM")

    info(
        "KULLANICI ADI",
        "Herkese açık oyuncu profilini belirler."
    )

    info(
        "PUBLIC PROFİL",
        "Oyuncunun herkese açık profil bilgilerini gösterebilir."
    )

    info(
        "PUBLIC OYUNLAR",
        "Görünürlük ayarlarına bağlı olarak public oyun geçmişi"
        " bulunabilir."
    )

    info(
        "İSTATİSTİKLER",
        "Platformun public olarak gösterdiği oyun istatistikleri"
        " incelenebilir."
    )

    pause()


def lichess_help():
    header("LICHESS")

    info(
        "KULLANICI ADI",
        "Herkese açık oyuncu profilini belirler."
    )

    info(
        "PUBLIC PROFİL",
        "Kullanıcının public profil bilgilerini gösterebilir."
    )

    info(
        "OYUN GEÇMİŞİ",
        "Public olarak erişilebilen oyun kayıtları araştırılabilir."
    )

    info(
        "İSTATİSTİKLER",
        "Platformun public olarak sunduğu oyun istatistikleri"
        " incelenebilir."
    )

    pause()


# ============================================================
# PLATFORM YARDIMLARI - 4
# TASARIM / YARATICI PLATFORMLAR
# ============================================================

def behance_help():
    header("BEHANCE")

    info(
        "KULLANICI ADI",
        "Herkese açık tasarımcı profilini belirler."
    )

    info(
        "PORTFÖY",
        "Kullanıcının public olarak yayınladığı tasarım"
        " çalışmalarını gösterebilir."
    )

    info(
        "BIO",
        "Tasarımcının kendi yazdığı public açıklamadır."
    )

    pause()


def dribbble_help():
    header("DRIBBBLE")

    info(
        "KULLANICI ADI",
        "Herkese açık tasarımcı profilini belirler."
    )

    info(
        "SHOTLAR",
        "Kullanıcının public olarak yayınladığı tasarım"
        " çalışmalarını gösterebilir."
    )

    info(
        "PROFİL",
        "Public bio ve portföy bilgilerini içerebilir."
    )

    pause()


def artstation_help():
    header("ARTSTATION")

    info(
        "KULLANICI ADI",
        "Herkese açık sanatçı profilini belirler."
    )

    info(
        "PORTFÖY",
        "Kullanıcının public olarak yayınladığı sanat"
        " çalışmalarını gösterebilir."
    )

    info(
        "PROFİL",
        "Public bio ve bağlantılar içerebilir."
    )

    pause()


def deviantart_help():
    header("DEVIANTART")

    info(
        "KULLANICI ADI",
        "Herkese açık sanatçı profilini belirler."
    )

    info(
        "GALERİ",
        "Kullanıcının public olarak yayınladığı çalışmalar"
        " incelenebilir."
    )

    info(
        "PROFİL",
        "Public profil açıklaması ve bağlantılar bulunabilir."
    )

    pause()


def soundcloud_help():
    header("SOUNDCLOUD")

    info(
        "KULLANICI ADI",
        "Herkese açık sanatçı veya kullanıcı profilini"
        " belirleyebilir."
    )

    info(
        "PARÇALAR",
        "Kullanıcının public olarak yayınladığı ses içeriklerini"
        " gösterebilir."
    )

    info(
        "PROFİL",
        "Public bio ve kullanıcının kendi eklediği bağlantıları"
        " içerebilir."
    )

    pause()


# ============================================================
# PLATFORM YARDIMLARI - 5
# DİĞER PLATFORMLAR
# ============================================================

def linktree_help():
    header("LINKTREE")

    info(
        "PROFİL",
        "Kullanıcının oluşturduğu public bağlantı sayfasıdır."
    )

    info(
        "BAĞLANTILAR",
        "Kullanıcının kendi eklediği diğer platformlara"
        " yönlendirebilir."
    )

    info(
        "OSINT KULLANIMI",
        "Farklı platformlarda kullanılan kullanıcı adlarını"
        " ilişkilendirmek için başlangıç noktası olabilir."
    )

    warning(
        "Bir Linktree bağlantısının bulunması, bağlantıların"
        " aynı kişiye ait olduğunu tek başına kanıtlamaz."
    )

    pause()


def patreon_help():
    header("PATREON")

    info(
        "PROFİL",
        "İçerik üreticisinin herkese açık profil bilgilerini"
        " gösterebilir."
    )

    info(
        "BIO",
        "Üreticinin kendi yazdığı public açıklamadır."
    )

    info(
        "PUBLIC BAĞLANTILAR",
        "Kullanıcının kendi eklediği diğer platformları"
        " gösterebilir."
    )

    warning(
        "Üyelik gerektiren veya private içerikler OSINT araması"
        " kapsamında değerlendirilmez."
    )

    pause()


def kofi_help():
    header("KO-FI")

    info(
        "PROFİL",
        "İçerik üreticisinin public profilini gösterebilir."
    )

    info(
        "AÇIKLAMA",
        "Kullanıcının kendi yazdığı public bilgileri içerebilir."
    )

    info(
        "BAĞLANTILAR",
        "Kullanıcının kendi eklediği diğer platformlara"
        " yönlendirebilir."
    )

    pause()
# ============================================================
# 5 - HTTP DURUM KODLARI
# ============================================================

def http_help():
    header("HTTP DURUM KODLARI")

    section("OSINT ARACINDA GÖRÜLEN KODLAR")

    info(
        "200 - OK",
        "Sunucu isteği başarıyla kabul etti.\n"
        "Bu genellikle sayfanın mevcut olduğunu gösterir."
    )

    info(
        "3xx - YÖNLENDİRME",
        "İstek başka bir adrese yönlendirilmiş olabilir.\n"
        "Platforma göre yorumlanmalıdır."
    )

    info(
        "403 - FORBIDDEN",
        "Sunucu isteği anladı ancak erişime izin vermedi.\n"
        "Bu sonuç hesabın kesin olarak var olduğunu kanıtlamaz."
    )

    info(
        "404 - NOT FOUND",
        "İstenen kaynak bulunamadı.\n"
        "Kullanıcı adı veya profil mevcut olmayabilir."
    )

    info(
        "429 - TOO MANY REQUESTS",
        "Sunucu çok fazla istek gönderildiğini algılamış olabilir.\n"
        "Rate limit uygulanıyor olabilir."
    )

    info(
        "TIMEOUT",
        "Sunucudan zamanında cevap alınamadı.\n"
        "Bu sonuç profilin bulunmadığı anlamına gelmez."
    )

    info(
        "BAĞLANTI HATASI",
        "İstemci sunucuya bağlantı kuramamış olabilir.\n"
        "İnternet veya DNS gibi sorunlar etkili olabilir."
    )

    warning(
        "HTTP durum kodunu tek başına kesin kanıt olarak"
        " değerlendirme."
    )

    pause()


# ============================================================
# 6 - SONUÇLARI YORUMLAMA
# ============================================================

def result_help():
    header("SONUÇLARI YORUMLAMA")

    section("BİR SONUÇ NE ANLAMA GELİR?")

    info(
        "✓ BULUNDU",
        "Araç ilgili URL'den başarılı bir cevap aldı.\n"
        "Bu, URL'nin erişilebilir olduğunu gösterir."
    )

    info(
        "✗ BULUNAMADI",
        "Araç profilin bulunamadığını belirten bir cevap aldı.\n"
        "Ancak platformun davranışı değişebileceğinden kesin"
        " hüküm vermeden önce kontrol edilmelidir."
    )

    info(
        "? 403",
        "Platform isteği engellemiş olabilir.\n"
        "Profilin varlığı kesin olarak doğrulanmış sayılmaz."
    )

    info(
        "? 429",
        "Çok fazla istek nedeniyle geçici sınırlama olabilir."
    )

    info(
        "? TIMEOUT",
        "Sunucu zamanında cevap vermemiştir."
    )

    info(
        "? BAĞLANTI HATASI",
        "İstemci ile sunucu arasında bağlantı problemi vardır."
    )

    section("ÖNEMLİ")

    print(
        f"{WHITE}"
        "  Bir kullanıcı adının bir platformda bulunması,"
        " o hesabın\n"
        "  araştırılan kişiyle aynı kişiye ait olduğunu kanıtlamaz.\n\n"
        "  Kullanıcı adı benzerliği yalnızca araştırma başlangıç"
        " noktasıdır."
        f"{RESET}"
    )

    pause()


# ============================================================
# 7 - OSINT DOĞRULAMA
# ============================================================

def verification_help():
    header("OSINT DOĞRULAMA")

    section("BİLGİYİ NASIL DOĞRULARIM?")

    info(
        "1. KAYNAĞI KONTROL ET",
        "Bilginin hangi web sitesi veya profilden geldiğine bak."
    )

    info(
        "2. TARİHE BAK",
        "Eski bir bilgi güncel olmayabilir."
    )

    info(
        "3. BİRDEN FAZLA KAYNAK",
        "Önemli bir bilgiyi mümkün olduğunca bağımsız public"
        " kaynaklarla karşılaştır."
    )

    info(
        "4. KULLANICI ADINI KARŞILAŞTIR",
        "Aynı kullanıcı adı başka platformlarda bulunabilir."
    )

    info(
        "5. BAĞLANTIYI KONTROL ET",
        "Bir profilin kendi bio'sunda verdiği public bağlantılar"
        " ilişkiyi destekleyebilir."
    )

    info(
        "6. KESİN KANIT / İPUCU AYRIMI",
        "Bir bulguyu kesin gerçek olarak değil, kanıt seviyesine"
        " göre değerlendir."
    )

    section("ÖRNEK")

    print(
        f"{WHITE}"
        "  Instagram'da 'example123' bulundu.\n"
        "  GitHub'da da 'example123' bulundu.\n\n"
        "  Bu iki hesabın aynı kişiye ait olduğu otomatik olarak"
        " kanıtlanmaz.\n"
        "  Ancak daha fazla public doğrulama için araştırma"
        " başlangıcı olabilir."
        f"{RESET}"
    )

    pause()


# ============================================================
# 8 - GÜVENLİ KULLANIM
# ============================================================

def safety_help():
    header("GÜVENLİ KULLANIM")

    section("OSINT SINIRLARI")

    info(
        "SADECE PUBLIC BİLGİ",
        "Araç, herkesin erişebildiği public kaynakların"
        " araştırılması için kullanılmalıdır."
    )

    info(
        "PRIVATE HESAPLAR",
        "Private hesapların içeriklerine erişmeye çalışılmaz."
    )

    info(
        "ŞİFRELER",
        "Şifre, token, cookie veya oturum bilgisi aranmaz."
    )

    info(
        "ERİŞİM KONTROLLERİ",
        "Giriş veya erişim kısıtlamaları aşılmaz."
    )

    info(
        "KİŞİSEL VERİ",
        "Gereksiz kişisel bilgiler toplanmamalı veya"
        " yayılmamalıdır."
    )

    info(
        "DOĞRULAMA",
        "Yanlış eşleşmelerden kaçınmak için bulgular"
        " doğrulanmalıdır."
    )

    warning(
        "OSINT aracı kullanmak, bir kişinin private bilgilerine"
        " erişim hakkı vermez."
    )

    pause()


# ============================================================
# 9 - KOMUTLAR
# ============================================================

def command_help():
    header("OSINT KOMUTLARI")

    section("TERMUX")

    info(
        "PROGRAMI AÇ",
        "osint"
    )

    info(
        "HELP'İ DOĞRUDAN AÇ",
        "osint help"
    )

    section("ANA MENÜ")

    option("1", "Yeni arama")
    option("3", "Help")
    option("0", "Çıkış")

    section("YENİ ARAMA")

    print(
        f"{WHITE}"
        "  Kullanıcı adı araştırması seçildiğinde araç,"
        " desteklenen\n"
        "  platformlarda public profil adreslerini kontrol eder."
        f"{RESET}"
    )

    info(
        "İSİM ARAMASI",
        "İsim araması için arama motorlarında public sonuçlar"
        " oluşturulabilir."
    )

    warning(
        "Sonuçları otomatik olarak kesin kimlik eşleşmesi"
        " olarak değerlendirme."
    )

    pause()


# ============================================================
# PROGRAM BAŞLANGICI
# ============================================================

def main():
    try:
        help_menu()

    except KeyboardInterrupt:
        print(
            f"\n\n{YELLOW}"
            "Yardım menüsünden çıkıldı."
            f"{RESET}"
        )

    except EOFError:
        print(
            f"\n\n{YELLOW}"
            "Girdi sonlandırıldı."
            f"{RESET}"
        )


if __name__ == "__main__":
    main()

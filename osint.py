import concurrent.futures
import sys
import time
import os
from urllib.parse import quote, urlparse

import requests


TIMEOUT = 10
MAX_WORKERS = 12

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Linux; Android 13; "
        "Mobile) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/140.0 "
        "Mobile Safari/537.36"
    ),
    "Accept-Language": "tr-TR,tr;q=0.9,en;q=0.8",
}


RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
GRAY = "\033[90m"
WHITE = "\033[97m"


FOUND = "found"
NOT_FOUND = "not_found"
UNKNOWN = "unknown"


PLATFORMS = [

    # SOSYAL

    {
        "name": "Instagram",
        "url": "https://www.instagram.com/{username}/",
        "not_found": [
            "page isn't available",
            "sorry, this page isn't available",
            "sayfa kullanılamıyor",
        ],
    },

    {
        "name": "X",
        "url": "https://x.com/{username}",
        "not_found": [
            "this account doesn’t exist",
            "this account doesn't exist",
            "hesap mevcut değil",
        ],
    },

    {
        "name": "TikTok",
        "url": "https://www.tiktok.com/@{username}",
        "not_found": [
            "couldn't find this account",
            "account not found",
            "couldn't find this user",
        ],
    },

    {
        "name": "Threads",
        "url": "https://www.threads.net/@{username}",
        "not_found": [
            "page isn't available",
            "page not found",
        ],
    },

    {
        "name": "Pinterest",
        "url": "https://www.pinterest.com/{username}/",
        "not_found": [
            "page not found",
            "this page isn't available",
        ],
    },

    {
        "name": "Facebook",
        "url": "https://www.facebook.com/{username}",
        "not_found": [
            "this page isn't available",
            "content isn't available",
        ],
    },

    {
        "name": "Snapchat",
        "url": "https://www.snapchat.com/add/{username}",
        "not_found": [
            "page not found",
            "couldn't find",
        ],
    },

    {
        "name": "Tumblr",
        "url": "https://{username}.tumblr.com/",
        "not_found": [
            "there's nothing here",
            "page not found",
        ],
    },

    {
        "name": "Bluesky",
        "url": "https://bsky.app/profile/{username}.bsky.social",
        "not_found": [
            "profile not found",
            "not found",
        ],
    },


    # VIDEO / YAYIN

    {
        "name": "YouTube",
        "url": "https://www.youtube.com/@{username}",
        "not_found": [
            "this page isn't available",
            "page not found",
        ],
    },

    {
        "name": "Twitch",
        "url": "https://www.twitch.tv/{username}",
        "not_found": [
            "content unavailable",
            "page not found",
        ],
    },

    {
        "name": "Kick",
        "url": "https://kick.com/{username}",
        "not_found": [
            "page not found",
            "user not found",
        ],
    },

    {
        "name": "Vimeo",
        "url": "https://vimeo.com/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Rumble",
        "url": "https://rumble.com/user/{username}",
        "not_found": [
            "page not found",
        ],
    },


    # GELİŞTİRİCİ / TEKNOLOJİ

    {
        "name": "GitHub",
        "url": "https://github.com/{username}",
        "not_found": [
            "this is not the page you're looking for",
            "this is not the page you’re looking for",
        ],
    },

    {
        "name": "GitLab",
        "url": "https://gitlab.com/{username}",
        "not_found": [
            "the page you're looking for doesn't exist",
        ],
    },

    {
        "name": "Codeberg",
        "url": "https://codeberg.org/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Dev.to",
        "url": "https://dev.to/{username}",
        "not_found": [
            "page not found",
            "the page you were looking for doesn't exist",
        ],
    },

    {
        "name": "Medium",
        "url": "https://medium.com/@{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Hashnode",
        "url": "https://hashnode.com/@{username}",
        "not_found": [
            "page not found",
            "user not found",
        ],
    },

    {
        "name": "Replit",
        "url": "https://replit.com/@{username}",
        "not_found": [
            "page not found",
            "user not found",
        ],
    },

    {
        "name": "Hugging Face",
        "url": "https://huggingface.co/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Kaggle",
        "url": "https://www.kaggle.com/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "LeetCode",
        "url": "https://leetcode.com/u/{username}/",
        "not_found": [
            "user not found",
            "page not found",
        ],
    },

    {
        "name": "HackerRank",
        "url": "https://www.hackerrank.com/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "CodePen",
        "url": "https://codepen.io/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Docker Hub",
        "url": "https://hub.docker.com/u/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "PyPI",
        "url": "https://pypi.org/user/{username}/",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "npm",
        "url": "https://www.npmjs.com/~{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Product Hunt",
        "url": "https://www.producthunt.com/@{username}",
        "not_found": [
            "page not found",
        ],
    },
]
# EK PLATFORMLAR

PLATFORMS += [

    # TOPLULUK / FORUM

    {
        "name": "Reddit",
        "url": "https://www.reddit.com/user/{username}/",
        "not_found": [
            "nobody on reddit goes by that name",
            "this account has been suspended",
            "page not found",
        ],
    },

    {
        "name": "Quora",
        "url": "https://www.quora.com/profile/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Hacker News",
        "url": "https://news.ycombinator.com/user?id={username}",
        "not_found": [
            "no such user",
        ],
    },


    # OYUN

    {
        "name": "Steam",
        "url": "https://steamcommunity.com/id/{username}",
        "not_found": [
            "the specified profile could not be found",
        ],
    },

    {
        "name": "Roblox",
        "url": "https://www.roblox.com/users/profile?username={username}",
        "not_found": [
            "user not found",
        ],
    },


    # MÜZİK / YARATICI

    {
        "name": "SoundCloud",
        "url": "https://soundcloud.com/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Bandcamp",
        "url": "https://{username}.bandcamp.com/",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Behance",
        "url": "https://www.behance.net/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Dribbble",
        "url": "https://dribbble.com/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "DeviantArt",
        "url": "https://www.deviantart.com/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Letterboxd",
        "url": "https://letterboxd.com/{username}/",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Patreon",
        "url": "https://www.patreon.com/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Ko-fi",
        "url": "https://ko-fi.com/{username}",
        "not_found": [
            "page not found",
        ],
    },


    # EK PLATFORM

    {
        "name": "Telegram",
        "url": "https://t.me/{username}",
        "not_found": [
            "if you have telegram",
            "username not found",
        ],
    },

    {
        "name": "Gitee",
        "url": "https://gitee.com/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "SourceForge",
        "url": "https://sourceforge.net/u/{username}/",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Codewars",
        "url": "https://www.codewars.com/users/{username}",
        "not_found": [
            "user not found",
        ],
    },

    {
        "name": "Exercism",
        "url": "https://exercism.org/profiles/{username}",
        "not_found": [
            "profile not found",
        ],
    },

    {
        "name": "Chess.com",
        "url": "https://www.chess.com/member/{username}",
        "not_found": [
            "member not found",
            "page not found",
        ],
    },

    {
        "name": "Lichess",
        "url": "https://lichess.org/@/{username}",
        "not_found": [
            "user not found",
        ],
    },

    {
        "name": "MyAnimeList",
        "url": "https://myanimelist.net/profile/{username}",
        "not_found": [
            "profile not found",
        ],
    },

    {
        "name": "AniList",
        "url": "https://anilist.co/user/{username}/",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "ArtStation",
        "url": "https://www.artstation.com/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Flickr",
        "url": "https://www.flickr.com/people/{username}/",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Mixcloud",
        "url": "https://www.mixcloud.com/{username}/",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Last.fm",
        "url": "https://www.last.fm/user/{username}",
        "not_found": [
            "page not found",
            "user not found",
        ],
    },

    {
        "name": "BandLab",
        "url": "https://www.bandlab.com/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Audiomack",
        "url": "https://audiomack.com/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "itch.io",
        "url": "https://{username}.itch.io/",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Game Jolt",
        "url": "https://gamejolt.com/@{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Modrinth",
        "url": "https://modrinth.com/user/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Keybase",
        "url": "https://keybase.io/{username}",
        "not_found": [
            "user not found",
        ],
    },

    {
        "name": "Linktree",
        "url": "https://linktr.ee/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "About.me",
        "url": "https://about.me/{username}",
        "not_found": [
            "page not found",
        ],
    },

    {
        "name": "Buy Me a Coffee",
        "url": "https://www.buymeacoffee.com/{username}",
        "not_found": [
            "page not found",
        ],
    },
]


# ============================================================
# YARDIMCI FONKSİYONLAR
# ============================================================

def clear():
    print("\033[2J\033[H", end="")


def pause():
    input("\nDevam etmek için ENTER...")


def clean_username(value):
    value = value.strip()

    if value.startswith("@"):
        value = value[1:]

    return value.strip()


def valid_url(url):
    try:
        p = urlparse(url)

        return (
            p.scheme in ("http", "https")
            and bool(p.netloc)
        )

    except Exception:
        return False


def page_says_not_found(response, platform):
    text = response.text.lower()

    for phrase in platform.get("not_found", []):
        if phrase.lower() in text:
            return True

    return False


# ============================================================
# PLATFORM KONTROLÜ
# ============================================================

def check_platform(platform, username):

    url = platform["url"].format(
        username=username
    )

    result = {
        "name": platform["name"],
        "url": url,
        "status": UNKNOWN,
        "http": None,
        "error": "",
    }

    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=TIMEOUT,
            allow_redirects=True,
        )

        code = response.status_code
        result["http"] = code

        # 404
        if code == 404:
            result["status"] = NOT_FOUND
            result["error"] = "404"
            return result

        # 403
        if code == 403:
            result["error"] = "403"
            return result

        # 429
        if code == 429:
            result["error"] = "429"
            return result

        # Diğer istemci hataları
        if 400 <= code < 500:
            result["error"] = str(code)
            return result

        # Sunucu hataları
        if 500 <= code < 600:
            result["error"] = str(code)
            return result

        # 200/3xx sayfa içeriği
        if page_says_not_found(
            response,
            platform
        ):
            result["status"] = NOT_FOUND
            result["error"] = str(code)
            return result

        if 200 <= code < 400:
            result["status"] = FOUND
            result["error"] = str(code)
            return result

        result["error"] = str(code)

    except requests.Timeout:
        result["error"] = "TIMEOUT"

    except requests.ConnectionError:
        result["error"] = "BAĞLANTI HATASI"

    except requests.RequestException as e:
        result["error"] = "HTTP HATASI"

    except Exception:
        result["error"] = "HATA"

    return result
# ============================================================
# SONUCU YAZDIR
# ============================================================

def print_result(result):

    name = result["name"]
    url = result["url"]
    status = result["status"]
    error = result["error"]

    if status == FOUND:
        text = f"{GREEN}✓ Bulundu{RESET}"

    elif status == NOT_FOUND:
        text = f"{RED}✗ Bulunamadı{RESET}"

    else:
        text = f"{YELLOW}? {error}{RESET}"

    print(
        f"{text:<25} "
        f"{name:<22}"
    )

    print(
        f"    {BLUE}{url}{RESET}"
    )


# ============================================================
# KULLANICI ADI TARAMASI
# ============================================================

def scan_username(username):

    print()
    print(
        f"{BOLD}{CYAN}"
        "Kullanıcı adı aranıyor..."
        f"{RESET}"
    )

    print(
        f"{GRAY}"
        f"{len(PLATFORMS)} platform kontrol edilecek."
        f"{RESET}"
    )

    print()

    results = []

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=MAX_WORKERS
    ) as executor:

        jobs = [
            executor.submit(
                check_platform,
                platform,
                username
            )
            for platform in PLATFORMS
        ]

        for job in concurrent.futures.as_completed(
            jobs
        ):

            try:
                result = job.result()

            except Exception:
                result = {
                    "name": "Bilinmeyen",
                    "url": "",
                    "status": UNKNOWN,
                    "http": None,
                    "error": "HATA",
                }

            results.append(result)
            print_result(result)

    print()

    found = sum(
        r["status"] == FOUND
        for r in results
    )

    not_found = sum(
        r["status"] == NOT_FOUND
        for r in results
    )

    errors = len(results) - found - not_found

    print(
        f"{BOLD}"
        "============== ÖZET =============="
        f"{RESET}"
    )

    print(
        f"{GREEN}Bulundu     : {found}{RESET}"
    )

    print(
        f"{RED}Bulunamadı  : {not_found}{RESET}"
    )

    print(
        f"{YELLOW}Hata/Bilinmiyor: {errors}{RESET}"
    )


# ============================================================
# İSİM ARAMA LİNKLERİ
# ============================================================

def create_name_searches(name):

    q = quote(
        name.strip(),
        safe=""
    )

    return [

        {
            "name": "Google",
            "url":
                "https://www.google.com/search?q="
                + q,
        },

        {
            "name": "Bing",
            "url":
                "https://www.bing.com/search?q="
                + q,
        },

        {
            "name": "DuckDuckGo",
            "url":
                "https://duckduckgo.com/?q="
                + q,
        },

        {
            "name": "Brave Search",
            "url":
                "https://search.brave.com/search?q="
                + q,
        },

        {
            "name": "Google - Instagram",
            "url":
                "https://www.google.com/search?q="
                + quote(
                    "site:instagram.com " + name,
                    safe=""
                ),
        },

        {
            "name": "Google - X",
            "url":
                "https://www.google.com/search?q="
                + quote(
                    "site:x.com " + name,
                    safe=""
                ),
        },

        {
            "name": "Google - YouTube",
            "url":
                "https://www.google.com/search?q="
                + quote(
                    "site:youtube.com " + name,
                    safe=""
                ),
        },

        {
            "name": "Google - TikTok",
            "url":
                "https://www.google.com/search?q="
                + quote(
                    "site:tiktok.com " + name,
                    safe=""
                ),
        },

        {
            "name": "Google - GitHub",
            "url":
                "https://www.google.com/search?q="
                + quote(
                    "site:github.com " + name,
                    safe=""
                ),
        },

        {
            "name": "Google - Reddit",
            "url":
                "https://www.google.com/search?q="
                + quote(
                    "site:reddit.com/user " + name,
                    safe=""
                ),
        },

        {
            "name": "Google - LinkedIn",
            "url":
                "https://www.google.com/search?q="
                + quote(
                    "site:linkedin.com/in " + name,
                    safe=""
                ),
        },

        {
            "name": "Google - Genel Profil",
            "url":
                "https://www.google.com/search?q="
                + quote(
                    '"' + name + '" profile',
                    safe=""
                ),
        },
    ]


# ============================================================
# İSİM ARAMASI
# ============================================================

def scan_name(name):

    print()
    print(
        f"{BOLD}{CYAN}"
        "İsim arama bağlantıları"
        f"{RESET}"
    )

    print()

    for item in create_name_searches(name):

        print(
            f"{WHITE}{item['name']}{RESET}"
        )

        print(
            f"    {BLUE}"
            f"{item['url']}"
            f"{RESET}"
        )

        print()
# ============================================================
# YENİ ARAMA
# ============================================================

def new_search():

    clear()

    print(
        f"{BOLD}{CYAN}"
        "========================================"
        f"{RESET}"
    )

    print(
        f"{BOLD}{WHITE}"
        "              YENİ ARAMA"
        f"{RESET}"
    )

    print(
        f"{BOLD}{CYAN}"
        "========================================"
        f"{RESET}"
    )

    print()

    username = input(
        "Kullanıcı adı (@nick): "
    ).strip()

    username = clean_username(
        username
    )

    name = input(
        "İsim: "
    ).strip()

    if not username and not name:

        print()
        print(
            f"{RED}"
            "Kullanıcı adı veya isim gir."
            f"{RESET}"
        )

        pause()
        return

    if username:
        scan_username(username)

    if name:
        scan_name(name)

    print()
    pause()


# ============================================================
# ANA MENÜ
# ============================================================

def main():

    while True:

        clear()

        print(
            f"{BOLD}{CYAN}"
            "========================================"
            f"{RESET}"
        )

        print(
            f"{BOLD}{WHITE}"
            "              OSINT ARAMA"
            f"{RESET}"
        )

        print(
            f"{BOLD}{CYAN}"
            "========================================"
            f"{RESET}"
        )

        print()

        print("1) Yeni arama")
        print("2) Help")
        print("0) Çıkış")

        print()

        choice = input(
            "Seçim: "
        ).strip()

        if choice == "1":
            new_search()

        elif choice == "2":
            import subprocess
            subprocess.run(
                ["python", os.path.expanduser("~/osint/osint_help.py")]
            )
            input("\nDevam etmek için ENTER...")

        elif choice == "0":
            clear()
            print(f"{CYAN}Program kapatıldı.{RESET}")
            sys.exit(0)
        else:

            print()

            print(
                f"{RED}"
                "Geçersiz seçim."
                f"{RESET}"
            )

            time.sleep(1)


# ============================================================
# BAŞLAT
# ============================================================

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:

        print()

        print(
            f"{YELLOW}"
            "Program durduruldu."
            f"{RESET}"
        )

        sys.exit(0)

    except Exception as error:

        print()

        print(
            f"{RED}"
            "Hata:"
            f"{RESET}"
        )

        print(
            f"{GRAY}{error}{RESET}"
        )

        sys.exit(1)

import requests
from bs4 import BeautifulSoup
import csv

# Wikipedia sayfasının URL'si
start_url = "https://en.wikipedia.org/wiki/Special:AllPages?from=electron&to=&namespace=0"

# Linklerin çekilmesi
response = requests.get(start_url)
if response.status_code != 200:
    print(f"Başlangıç URL'sine ulaşılamadı. HTTP Hatası: {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, "html.parser")
allpages_div = soup.find("div", class_="mw-allpages-body")
if allpages_div is None:
    print("Hata: 'mw-allpages-body' sınıfı bulunamadı!")
    exit()

links = allpages_div.find_all("a", href=True)

# CSV dosyası oluştur
csv_filename = "electron1.csv" 
with open(csv_filename, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Makale Adı", "İçerik"])  # Sütun başlıkları

    # Ana işlemleri yürütecek fonksiyon
    def process_article(link_text, link_href):
        full_url = f"https://en.wikipedia.org{link_href}"
        print(f"\nİşleniyor: {link_text} -> {full_url}")
        
        # Makaleyi indir
        response = requests.get(full_url)
        if response.status_code != 200:
            print(f"Hata: {link_text} sayfası indirilemedi! HTTP Hatası: {response.status_code}")
            return

        soup = BeautifulSoup(response.content, "html.parser")
        content_div = soup.find("div", class_="mw-content-ltr mw-parser-output")
        if content_div is None:
            print(f"Hata: {link_text} için içerik bulunamadı!")
            return

        # İçeriği ayrıştır
        article_data = []
        for element in content_div.find_all(["h2", "h3", "p"]):
            if element.name in ["h2", "h3"]:
                article_data.append(f"\n== {element.get_text(strip=True)} ==")
            elif element.name == "p":
                text = element.get_text(strip=True)
                if text:
                    article_data.append(text)

        # İçeriği birleştir
        full_article = "\n".join(article_data)

        # CSV'ye yaz
        writer.writerow([link_text, full_article])
        print(f"{link_text} makalesi CSV dosyasına kaydedildi.")

    # Tüm linkleri işle
    for i, link in enumerate(links, start=1):
        link_text = link.get_text(strip=True)
        link_href = link['href']
        print(f"\n#{i} Makale İşleniyor:")
        process_article(link_text, link_href)

print(f"Tüm makaleler '{csv_filename}' dosyasına kaydedildi!")

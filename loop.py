import requests
from bs4 import BeautifulSoup

# Wikipedia sayfasının URL'si
url = "https://en.wikipedia.org/wiki/Special:AllPages?from=Technology&to=&namespace=0"

# HTTP isteği gönder
response = requests.get(url)

# HTTP isteğinin başarılı olup olmadığını kontrol et
if response.status_code == 200:
    print("Sayfa başarıyla indirildi!")
else:
    print(f"HTTP Hatası: {response.status_code}")
    exit()

# HTML içeriğini ayrıştır
soup = BeautifulSoup(response.content, "html.parser")

# İlgili div'i bul
allpages_div = soup.find("div", class_="mw-allpages-body")

# Div bulunamadıysa hata ver
if allpages_div is None:
    print("Hata: 'mw-allpages-body' sınıfı bulunamadı!")
    exit()

# Linkleri çek ve bastır
links = allpages_div.find_all("a", href=True)  # href'e sahip <a> etiketlerini al
if links:
    for link in links:
        link_text = link.get_text(strip=True)  # Link metni
        link_href = link['href']  # Linkin href değeri
        print(f"{link_text}: https://en.wikipedia.org{link_href}")
else:
    print("Hata: Bu div içinde hiç link bulunamadı!")

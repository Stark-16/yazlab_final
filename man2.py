import requests
from bs4 import BeautifulSoup

# Wikipedia sayfasının URL'si
url = "https://en.wikipedia.org/wiki/Object-oriented_programming"

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

# Ana makale gövdesi: mw-parser-output sınıfını bul
content_div = soup.find("div", class_="mw-parser-output")

# Ana gövde bulunamadıysa hata ver
if content_div is None:
    print("Hata: Ana makale gövdesi bulunamadı!")
    exit()

# Başlık ve paragraf yapısını düzenli çekmek için veri saklama
article_data = []

# Başlık ve içerikleri ayrıştır
current_section = None
current_content = []
for element in content_div.find_all(["h2", "h3", "p"]):
    if element.name in ["h2", "h3"]:
        # Eğer önceki başlıkta içerik varsa, kaydet
        if current_section and current_content:
            article_data.append({"section": current_section, "content": current_content})
        # Yeni başlığı başlat
        current_section = element.get_text(strip=True)
        current_content = []  # İçeriği sıfırla
    elif element.name == "p" and current_section:
        # Paragraf ise, mevcut başlığa ekle
        text = element.get_text(strip=True)
        if text:
            current_content.append(text)

# Döngü bittikten sonra son başlık ve içeriği kaydet
if current_section and current_content:
    article_data.append({"section": current_section, "content": current_content})

# Veriyi derli toplu şekilde yazdır veya kaydet
output_lines = []
for section in article_data:
    output_lines.append(f"== {section['section']} ==")
    output_lines.extend(section["content"])
    output_lines.append("")  # Bölümler arasında boşluk

# Tüm metni birleştir
full_article = "\n".join(output_lines)

# Sonucu yazdır
print(full_article[:1000])  # İlk 1000 karakteri yazdır

# Alternatif: Metni bir dosyaya kaydet
with open("oop_filtered.txt", "w", encoding="utf-8") as file:
    file.write(full_article)
    print("Makale başarıyla 'oop_filtered.txt' dosyasına kaydedildi!")

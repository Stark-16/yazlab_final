import re
import pandas as pd

# Örnek bir veri yükleyelim (CSV dosyasını okuyarak DataFrame oluşturuyoruz)
file_path = "dataset_filtered2.csv"  # CSV dosyanızın yolu
df = pd.read_csv(file_path)

def clean_text(text):
    """
    Metni temizlemek için bir fonksiyon.
    - Fazla boşlukları kaldırır.
    - HTML etiketlerini temizler.
    - Özel karakterleri ve sembolleri kaldırır.
    - \n ve \t gibi kontrol karakterlerini temizler.
    """
    # 1. HTML etiketlerini temizle
    text = re.sub(r"<.*?>", "", text)
    
    # 2. Özel karakterler ve sembolleri kaldır
    text = re.sub(r"[^\w\s]", "", text)  # Harf, rakam ve boşluk dışındaki her şeyi kaldırır
    
    # 3. Satır sonları ve tab karakterlerini kaldır (\n, \t)
    text = re.sub(r"[\n\t\r]", " ", text)
    
    # 4. Fazla boşlukları tek bir boşluğa indir
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

# "İçerik" sütunundaki metinleri temizleme
df["İçerik"] = df["İçerik"].apply(clean_text)

# "Makale Adı" sütunundaki metinleri de temizlemek isterseniz:
df["Makale Adı"] = df["Makale Adı"].apply(clean_text)

# Temizlenmiş veri setini bir dosyaya kaydetmek için:
output_file = "dataset_filtered2.csv"
df.to_csv(output_file, index=False)
print(f"Temizlenmiş veri {output_file} olarak kaydedildi.")

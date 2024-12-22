import pandas as pd
import re

# Örnek CSV dosyasını yükleme
input_file = "all3.csv"  # Dataset dosya adı
output_file = "all4.csv"  # Temizlenmiş datasetin kaydedileceği dosya adı

# CSV dosyasını yükleme
df = pd.read_csv(input_file)

# Fonksiyon: Altı boş olan başlıkları ve bu başlıkları kaldırma
def clean_empty_sections(content):
    if pd.isna(content):  # Eğer içerik boşsa, olduğu gibi döndür
        return content
    
    # Tüm başlıkları regex ile bul
    # Başlık formatı: '== Başlık adı =='
    pattern = r"(== .*? ==)(?:\n\s*\n|\n?$)"  # Altında metin olmayan başlıkları bul
    
    # Başlıkları altı boşsa kaldır
    cleaned_content = re.sub(pattern, "", content, flags=re.MULTILINE)
    return cleaned_content.strip()

# Fonksiyon: Kelime sayısını kontrol etme ve kısa içerikleri kaldırma
def filter_short_content(content):
    if pd.isna(content):  # İçerik boşsa None döndür
        return None
    word_count = len(content.split())  # Kelime sayısını hesapla
    return content if word_count >= 20 else None  # 20'den azsa None döndür

# DataFrame'in 'İçerik' sütununu temizle
df['İçerik'] = df['İçerik'].apply(clean_empty_sections)
df['İçerik'] = df['İçerik'].apply(filter_short_content)

# Kelime sayısı az olan satırları tamamen kaldır
df = df.dropna(subset=['İçerik'])

# Temizlenmiş dataset yeni bir dosyaya kaydedilir
df.to_csv(output_file, index=False)

print(f"Temizleme işlemi tamamlandı. Sonuç {output_file} dosyasına kaydedildi.")

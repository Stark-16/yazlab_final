import pandas as pd

# CSV dosyasını yükleme
input_file = "dataset_filtered.csv"  # Veri dosyanızın adı
output_file = "dataset_filtered2.csv"  # Temizlenmiş verilerin kaydedileceği dosya adı

# CSV dosyasını pandas DataFrame olarak yükleme
df = pd.read_csv(input_file)

# Fonksiyon: İçerikteki kelime sayısını kontrol et
def has_minimum_words(content):
    if pd.isna(content):  # Eğer içerik boşsa (NaN), False döndür
        return False
    # Kelime sayısını hesapla
    word_count = len(content.split())
    return word_count >= 100  # 20 veya daha fazla kelime varsa True, değilse False

# Kelime sayısı 20'den az olan satırları filtrele
df = df[df['İçerik'].apply(has_minimum_words)]

# Temizlenmiş verileri yeni bir CSV dosyasına kaydet
df.to_csv(output_file, index=False)

print(f"Kelime sayısı 20'den az olan satırlar silindi. Sonuç {output_file} dosyasına kaydedildi.")

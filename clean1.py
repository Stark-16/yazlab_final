import pandas as pd
import re

# CSV dosyasını yükleme
input_file = "databackup/all.csv"  # Veri dosyanızın adı
output_file = "all2.csv"  # Temizlenmiş verilerin kaydedileceği dosya adı

# CSV dosyasını pandas DataFrame olarak yükleme
df = pd.read_csv(input_file)

# Temizlenmesi gereken başlıklar
remove_headers = [
    "== See also ==",
    "== Notes ==",
    "== References ==",
    "== Sources ==",
    "== External links =="
]

# Fonksiyon: İlgili başlıkları ve varsa altındaki metni sil
def remove_unwanted_sections(content):
    if pd.isna(content):  # Eğer içerik boşsa olduğu gibi dön
        return content

    # Her bir başlığı regex ile sil
    for header in remove_headers:
        # Başlığı ve altındaki metni (bir sonraki başlığa kadar olan kısmı) temizle
        content = re.sub(rf"{re.escape(header)}.*?(?=(==|$))", "", content, flags=re.DOTALL)

    # Fazla boşlukları temizle
    content = content.strip()
    return content

# 'İçerik' sütununu güncelle
df['İçerik'] = df['İçerik'].apply(remove_unwanted_sections)

# Temizlenmiş verileri yeni bir CSV dosyasına kaydet
df.to_csv(output_file, index=False)

print(f"Belirtilen başlıklar ve altındaki içerikler temizlendi. Sonuç {output_file} dosyasına kaydedildi.")

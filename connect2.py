import os
import pandas as pd

# Ana klasörün yolu
folder_path = "/Users/muratertik/Desktop/data/databackup"  # Kendi yolunuzu buraya girin

# Tüm CSV dosyalarını saklamak için bir liste
csv_files = []

# Klasörün ve alt klasörlerin içinde döngü oluşturmak için os.walk kullanıyoruz
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        # Eğer dosyanın uzantısı .csv ise
        if file_name.endswith(".csv"):
            # Dosyanın tam yolunu al
            file_path = os.path.join(root, file_name)
            # Dosyayı bir pandas DataFrame olarak oku ve listeye ekle
            csv_files.append(pd.read_csv(file_path))

# Tüm CSV dosyalarını birleştir
merged_csv = pd.concat(csv_files, ignore_index=True)

# Birleştirilmiş dosyayı kaydetmek için hedef dosya yolu
output_file = os.path.join(folder_path, "all.csv")

# Birleştirilmiş CSV dosyasını kaydet
merged_csv.to_csv(output_file, index=False)

print(f"CSV dosyaları birleştirildi ve {output_file} olarak kaydedildi.")

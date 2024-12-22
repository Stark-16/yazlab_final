import pandas as pd

# CSV dosyasının yolunu belirtin
file_path = "dataset.csv"  # Örneğin: "C:/data/your_file.csv"

# CSV dosyasını oku
df = pd.read_csv(file_path)

# "Others" olmayan satırları filtrele
filtered_df = df[df["Kategori"] != "Other"]

# Düzenlenmiş veri kümesini aynı dosyaya veya farklı bir dosyaya kaydedin
output_file = "dataset_filtered.csv"  # Kaydedilecek dosyanın yolu
filtered_df.to_csv(output_file, index=False)

print(f"'Others' satırları çıkarıldı ve düzenlenmiş veri kümesi {output_file} olarak kaydedildi.")

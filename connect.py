import pandas as pd

# CSV dosyalarının adlarını belirtin
csv_dosyalar = ["all1.csv","all2.csv"]

# Dosyaları birleştirmek için bir liste oluşturun
dataframes = [pd.read_csv(dosya) for dosya in csv_dosyalar]

# DataFrame'leri birleştirin
birlesmis_df = pd.concat(dataframes, ignore_index=True)

# Birleştirilmiş CSV dosyasını kaydedin
birlesmis_df.to_csv("mydataset.csv", index=False)

print("Dosyalar başarıyla birleştirildi ve 'allreligion.csv' olarak kaydedildi.")

import pandas as pd
import matplotlib.pyplot as pylot
import seaborn as sns

dataPath = 'D:\my-code\learn-python\data-science\latihan-ds\mobil.csv'

data = pd.read_csv(dataPath)

# print(data)

mobilTerbanyak = data['Merek Mobil'].value_counts().idxmax()
mobilTersedikit = data['Merek Mobil'].value_counts().idxmin()

print('Mobil dengan penjualan terbanyak adalah :', mobilTerbanyak)
print('Mobil dengan penjualan paling sedikit adalah :', mobilTersedikit)
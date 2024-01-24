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

hondaTerbanyak = data[data['Merek Mobil'] == 'Honda'].value_counts().idxmax()
hondaTerbanyak = data[data['Merek Mobil'] == 'Toyota'].value_counts().idxmax()

print(hondaTerbanyak)

bulanTerbanyak = data['Bulan'].value_counts().nlargest(10).index.tolist()

print(bulanTerbanyak)

data['Harga'] = data['Harga'].str.replace('[Rp.]', '', regex=True).str.replace('[.]', '', regex=True).astype(int)
data['Pendapatan'] = data['Mobil Terjual'] * data['Harga']

bulanPendapatanTerbanyak = data.groupby('Bulan')['Pendapatan'].sum().idxmax()

print(bulanPendapatanTerbanyak)
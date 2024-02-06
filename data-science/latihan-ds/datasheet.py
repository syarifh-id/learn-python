import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

dataPath = 'D:\my-code\learn-python\data-science\latihan-ds\csv\mobil.csv'
data = pd.read_csv(dataPath)

# print(data)

# mobilTerbanyak = data['Merek Mobil'].value_counts().idxmax()
# print('Mobil dengan penjualan terbanyak adalah :', mobilTerbanyak)
# mobilTersedikit = data['Merek Mobil'].value_counts().idxmin()
# print('Mobil dengan penjualan paling sedikit adalah :', mobilTersedikit)

# hondaTerbanyak = data[data['Merek Mobil'] == 'Honda'].value_counts().idxmax()
# print(hondaTerbanyak)
# toyotaTerbanyak = data[data['Merek Mobil'] == 'Toyota'].value_counts().idxmin()
# print(toyotaTerbanyak)

# bulanTerbanyak = data['Bulan'].value_counts().nlargest(12).index.tolist()
# print(bulanTerbanyak)

###### membersihkan data dari string yang tidak terpakai [Rp. .] ########
data['Harga'] = data['Harga'].str.replace('[Rp.]', '', regex=True).str.replace('[.]', '', regex=True).astype(int)
print(data['Harga'])

# data['Pendapatan'] = data['Mobil Terjual'] * data['Harga']

# bulanPendapatanTerbanyak = data.groupby('Bulan')['Pendapatan'].sum().idxmax()

# print(bulanPendapatanTerbanyak)
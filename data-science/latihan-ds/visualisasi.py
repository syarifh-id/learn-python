import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

dataPath = "D:\my-code\learn-python\data-science\latihan-ds\csv\penjualan_mobil.csv"

#read data 
data = pd.read_csv(dataPath)

data['Bulan'] = pd.to_datetime(data['Bulan'])

plt.plot(data['Bulan'], data['Penjualan'])
plt.xlabel('Bulan')
plt.ylabel('Penjualan')
plt.xticks(rotation=90)
plt.title("Trend Penjualan")
plt.show()







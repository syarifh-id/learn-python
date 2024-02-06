import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

dataPath = "D:\my-code\learn-python\data-science\latihan-ds\csv\penjualan_mobil.csv"

#read data 
data = pd.read_csv(dataPath)

#penjualan terbanyak 
mostSales = data['Penjualan'].value_counts().idxmax()
print(mostSales)
#penjualan tersedikit
lowestSales = data['Penjualan'].value_counts().idxmin()
print(lowestSales)
#perbulan
mostSalesByMoon = data['Bulan'].value_counts().nlargest().index.tolist()
print(mostSalesByMoon)

x = data.groupby('Bulan')['Penjualan'].sum().idxmax()
print(x)
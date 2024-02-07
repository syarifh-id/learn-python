import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

dataPath = "D:\my-code\learn-python\data-science\latihan-ds\csv\kemiskinan.csv"

data = pd.read_csv(dataPath)

plt.bar(data['Provinsi'], data['Penduduk'])
plt.xlabel('Provinsi')
plt.ylabel('Penduduk')
plt.xticks(rotation=90)
plt.show()

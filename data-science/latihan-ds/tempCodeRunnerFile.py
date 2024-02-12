import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sb

dataPath = "D:\my-code\learn-python\data-science\latihan-ds\csv\kemiskinan.csv"

df = pd.read_csv(dataPath)
#print(df.columns)
# print(df)

plot.bar(df['Provinsi'], df['Kemiskinan'])
plot.xlabel('Provinsi')
plot.ylabel('Penduduk')
plot.xticks(rotation=45)
plot.show()
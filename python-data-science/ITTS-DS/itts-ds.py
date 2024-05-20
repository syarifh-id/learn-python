import pandas as pd
import matplotlib.pyplot as plt

dataPath = "D:\my-code\learn-python\data-science\ITTS-DS\tujuan-wisata.csv"


data = pd.read_csv(dataPath)
print(data)
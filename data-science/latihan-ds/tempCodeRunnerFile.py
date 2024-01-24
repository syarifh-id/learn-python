data['Harga'] = data['Harga'].str.replace('[Rp.]', '', regex=True).str.replace('[.]', '', regex=True).astype(int)
data['Pendapatan'] = data['Mobil Terjual'] * data['Harga']

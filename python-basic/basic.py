#string
nama = "syarifh"
namaBelakang = 'hidayat'
print("nama saya adalah",nama,namaBelakang)
#interger
usia = 24
print("umur saya",usia)
#float
tinggi = 1.8
print("tinggi saya adalah",tinggi,"meter")




# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.




#list *mutable
hobby = ["membaca", "koding", "olahraga" ]
print("Hobby saya yang saya sedang tekuni adalah",hobby[1])
hobby[1] = "programming"
print("Hobby saya yang saya sedang tekuni adalah",hobby[1])
#list
nilai = [9,8,7,9,7,6,7,6]
print("nilai tertinggi saya", nilai[0])
print("Jumlah mapel", len(nilai))
print("data nilai ber-type", type(nilai))
#tuple *immutable
favColor = ("biru", "ungu", "jingga")
print("warna kesukaan saya", favColor[0])
# favColor[1] = "hitam" error
#dictonary
students = {"nama":"syarifh", "umur":23, "asal":"karanganyar"}
print("nama saya", students["nama"],'saya berasal dari', students["asal"],"saya berumur",students["umur"])

#set * mengacak data
days = {"senin", "selasa", "rabu", "kamis", "jum'at", "sabtu", "ahad"}
print("nama nama hari", days)

#booelan
mymind = True

i = 1

while i <= 5 :
	print("pengulangan ke :", i)
	i += 1
 
 
#to stops looping use break

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
  
#loop use for

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)
  
  
#and also can use a break keyword


fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)
	if x == "banana":
		break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
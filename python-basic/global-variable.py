#we can globalize variable inside function with global keyword

def myVar():
	global i 
	i = "syarif"
	print("this is my name ", i)

myVar()

print("this is also my name ", i)
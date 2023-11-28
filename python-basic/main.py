print("hellow")
#this is a comment

if 5 > 1 :
	print("its true") #python use indentation to indicate a block of code
if 5 > 1 :
	print("Remember python use indentation")

i = 1

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
print("i")

#If you want to specify the data type of a variable, this can be done with casting.
#Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

print("type of this variable is ",type(i)) # to show the type of data

name, age, gender = "syarif", 22, "male" #multiple assign variable

print("my name is ",name," and my age ",age)
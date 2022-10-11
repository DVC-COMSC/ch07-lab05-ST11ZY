
# ******************************
# Make your Code
# ******************************
strval = input("numbers?").split()
numbers = []
for v in strval:
	numbers.append(int(v))
comp=input("Number?")
x=numbers.count(int(comp))
print(x)
# the below llin 11 are same as the lines from 5 to 8
# numbers = list(map(int, strval))
# print (numbers)

#!usr/bin/python3

stra="Mr John Smith    "
letterCount=0
j=len(stra)
count=0
for letter in stra:
	letterCount+=1
	if (letter==" " and letterCount<=j):
		stra = stra[:letterCount-1]+ "%20" + stra[letterCount:]
		letterCount+=2

print(stra)
		

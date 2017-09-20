#!usr/bin/python3


strA="ramesh"
strB="kufakbflafbakuajagfkameasdjaarnjfahs"
#strB="shmear"
if len(strA)>len(strB):
	temp=strA
	strA=strB
	strB=temp

for letter in strA:
	if letter in strB:
		continue
	else:
		print("Not a permutation. Exiting program!!")
		exit(0)
print("Seems like it was a permutation string")

#!usr/bin/python3

A1 = [1,3,5,7,11,13,21,31]
A2 = [2,4,6,8,10,20,30]
A3 = A1
A1= A3 + A2
i = 0
j = 0
count = 0
count1 = count2 = 1
while(count<len(A1)):
	if count1 and count2:
		if A3[i]<A2[j]:
			A1[count] = A3[i]
			i+=1

	
		else :
			A1[count] = A2[j]
			j+=1

	elif count1:
		A1[count] = A3[i]
		i+=1
	elif count2:
		A1[count] = A2[j]
		j+=1
	
		
	if i==len(A3):
		count1=0

	if j==len(A2):
		count2=0

	count+=1

print A1
		

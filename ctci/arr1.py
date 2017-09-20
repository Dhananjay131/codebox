#!usr/bin/python3

string = "pattern"
print("the entered string is:" + string)

i=0
while(i<len(string)):
	j=i+1
	while j< len(string):
#		print (string[i] + " vs "+ string[j])
		if string[i]==string[j]:
			print ("Oops! Characters aren't unique.")
			exit(0)
		j+=1
	i+=1
print("Hurray!! All the characters are unique.")

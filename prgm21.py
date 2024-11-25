string=input("enter a string:")
count=0
for i in range(0,len(string)):
	if(string[i]!=' '):
		count+=1
print("the number of characters in the string is"+str(count));

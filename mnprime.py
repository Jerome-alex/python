def isprime(n):
	if n<=1:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
	return True
n=int(input("enter a number"))
for i in range(1,n):
	if isprime(i):
		print(i)


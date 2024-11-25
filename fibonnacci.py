def fibonacci(n):
	if n==0 or n==1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter the number to generate fibonacci series"))
for i in range(n):
	print(fibonacci(i),end=" ")
print("\n the",n,"fibonacci numbers are:",fibonacci(n-1))

def is_palindrome(n):
	n_str=str(n)
	n_rev=n_str[::-1]
	if n_str==n_rev:
		return True
	else:
		return False
n=input("enter a number")
result=is_palindrome(n)
if result:
	print("the number is palindrome")
		
else:
	print("the number is not a palindrome")

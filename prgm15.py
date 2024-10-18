def add(n1,n2):
	return n1+n2
def subtract(n1,n2):
	return n1-n2
def multiply(n1,n2):
	return n1*n2
def divide(n1,n2):
	return n1/n2
def power(n1,n2):
	return n1**n2
def calculator(n1,operator,n2):
	if operator=="+":
		return add(n1,n2)
	elif operator=="-":
		return subtract(n1,n2)
	elif operator=="*":
		return multiply(n1,n2)
	elif operator=="/":
		return divide(n1,n2)
	elif operator=="**":
		return power(n1,n2)
	else:
		print("invalid option")
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
operator=input("\n enter the operator:+,-,*,/,**\n")
result=calculator(n1,operator,n2)
print("result=",result)
 

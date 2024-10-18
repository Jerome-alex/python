a=int(input("enter the first number"))
b=int(input("enter the second number"))
print("operations")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.exponentiation")
print("6.floor division")
print("7.modulo")
choice=int(input("select the choice"))
if choice==1:
	r=a+b
	print("the sum is",r)
elif choice==2:
	result=a-b
	print("the result is",result)
elif choice==3:
	result=a*b
	print("the product is",result)
elif choice==4:
	result=a/b
	print("the result is",result)
elif choice==5:
	result=a**b
	print("the result is",result)
elif choice==6:
	result=a//b
	print("the result is",result)
elif choice==7:
	result=a%b
	print("the result is",result)
else:
	print("invalid choice")

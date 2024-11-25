a=int(input("enter the first side"))
b=int(input("enter the second side"))
c=int(input("enter the third side"))
s=(a+b+c)/2
print('the semi perimeter is',s)
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('the area of the triangle is',area)

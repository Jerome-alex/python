string=input("enter a string ")
first_char=string[0]
new_string=first_char+string[1: ].replace(first_char,'$')
print("the modified string is",new_string)

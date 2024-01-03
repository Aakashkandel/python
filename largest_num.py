a=int(input("Enter the first number here: "))
b=int(input("Enter the second number here: "))
c=int(input("Enter the third number here: "))

if a>b:
    if a>c:
        print(f"{a} is largest among three number")
        
    else:
        print(f"{c} is largest among three number")
        
else:
    if b>c:
        print(f"{b} is largest among three number")
    else:
        print(f"{c} is largest among three number")

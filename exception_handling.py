try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    
    r=a/b
    print("Result is:",r)
except:
    print("Divide by zero is exception")
finally:
    print("This is rest of the code ")
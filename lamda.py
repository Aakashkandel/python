# Write a program to find odd or even number 

# num=int(input('Enter the number which you want to check?'))
# if num%2==0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# Now,Using lamda function to perform above operation

calc=lambda num:"Even number" if num%2==0 else "Odd number"
n=int(input("Enter the number for check?"))
print(calc(n))
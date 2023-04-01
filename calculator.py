num_1 = float(input("Enter a Number:"))
num_2= float(input("Enter another Number:"))
choice = input("Enter the operations + - * / ")
if choice == "+":
    sum = num_1 + num_2
    print("The sum is",sum)

if choice=="-":
    diff = num_1 - num_2
    print("The dif is",diff)
    
if choice=="*":
        mul = num_1 * num_2
        print("The Mul is", mul)
        
        
if choice=="/":
    div = num_1 / num_2
    print("the div is ", div)
    
else:
    print("Invalid Choice")
        
    










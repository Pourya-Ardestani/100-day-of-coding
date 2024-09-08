def add (n1,n2):
    """add the to arguments"""
    return n1+n2

def sub(n1,n2):
    """subtract the firs argument by the second one"""
    return n1-n2

def multiply(n1,n2):
    """multiply the 2 numbers by each others"""
    return n1*n2

def divid(n1,n2):
    """divid the first argument by second argument"""
    return n1/n2

def calculator(op , num1 , num2):
    """takes Operator and 2 numbers and calculate the probles"""
    if op =='+':
        return add(num1,num2)
    elif op =='-':
        return sub(num1,num2)
    elif op =='*':
        return multiply(num1,num2)
    elif op =='/':
        return divid(num1,num2)
    else :
        print("ERROR !! \n INVALID OPERATOR")

number_1 = int(input("what is your firrst number :"))
number_2 = int(input("what is the second number : "))
print("*\n/\n+\n-")
operator = input("give the operator from list above : ")

print(f"{number_1} {operator} {number_2} = {calculator(operator,number_1,number_2) }")


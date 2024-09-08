def calculator(Num1 , Num2 , operator):
    """calculat with 2 number and the one operator that given in argumets """
    if operator == '*':
        result = Num1 * Num2 
    elif operator =='/':
        result = Num1 / Num2
    elif operator=='+':
        result = Num1 + Num2 
    elif operator =='-':
        result == Num1- Num2
    return result


F_number = float(input("what is your first number : "))
print("*\n+\n-\n/")
Op = input("what do you want todo with these numbers :")
S_number = float(input("what is your second number : "))
Result = calculator(F_number , S_number , Op)
print(f"{F_number} {Op} {S_number} = {Result}")
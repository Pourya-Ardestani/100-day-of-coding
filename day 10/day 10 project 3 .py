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

def calculat():
    number_1 = float(input("what is your firrst number :"))
    should_continue = True
    while should_continue :
        print("*\n+\n-\n/")
        op = input("what operator do you want to do (from list above):")
        number_2 = float(input("what is the second number : "))

        dict_calculator ={
            '+': add,
            '-':sub,
            '*':multiply,
            '/':divid ,
        }
        function = dict_calculator[op]
        answer= function(number_1,number_2)
        print(f"{number_1} {op} {number_2} = {answer}")
        continu = input(f"do you want to do somthing with {answer} (yes) or do you want to start a new calculation (no) : ")
        if continu =="yes" :
            should_continue = False
        elif continu == "no" :    
            number_1 = answer
            calculat()

calculat()            
def prime_check(n):

    prime = True 
    if number is 1 :
        prime = False
    for i in range(2,int(n/2)+1):
        if n%i == 0 :
            prime = False
    if prime == True :
        print("the number is PRIME")
    else :
        print("the number is NOT PRIME")




number = int(input("number :"))
prime_check(number)



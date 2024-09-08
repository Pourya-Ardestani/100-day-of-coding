for number in range(1,101):
    if number %3 ==0 :
        if number %5 ==0 :
           print("fizzbuzz")
        else :
            print("fizz")
    else :
        if number %5 ==0 :
           print("buzz")
        else :
            print(number)   
            
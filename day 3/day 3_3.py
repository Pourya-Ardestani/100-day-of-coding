Year = int(input("Enter a year : "))
if Year% 4 == 0 :
    if Year %100 == 0:
        if Year%400 == 0:
            print("it is a leap year ")
        else:
            print("it is not a leap year")   
    else:
        print("it is a leap Year")        
else:
    print("it is not a leap year")    

# Result = 0
# if Year % 4 == 0:
#     if Year % 100 == 0:
#         if Year % 400 == 0 :
#             Result = 1    
#     else:
#         result = 1        

# if Result == 1:
#     print("it is a leap year")
# else:
#     print("it is not a leap year")    
Hight = float(input("Enter your hight : "))
weight = int(input("Enter your weight : "))
BMI = round(weight/(Hight**2) , 2)
print(f"Your BMI : {BMI}")
if BMI <18.5 :
    print("You are ^UnderWeight^ ")
elif BMI < 25 :
    print("You are ^NormalWeight^")    
elif BMI < 30:
    print("you are ^OverWeight^")    
elif BMI < 35:
    print("You are obese") 
else:
    print("you are clinically obese")       
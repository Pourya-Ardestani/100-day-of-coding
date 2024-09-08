Bill = float(input("how much do you spent on food? $"))
Number = int(input("how many people were you ?"))
Percent = int(input("what percent do you want to give tip?(10,12or15)"))
Each = (Bill/Number) + (Bill/Number)*Percent*0.01
Round_Each = round(Each,2)
print(f"Each person need to pay : {Round_Each} " )

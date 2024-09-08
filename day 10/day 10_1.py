def is_leap(year):
    """takes the year and tells that the 
    year is leap or not in boolian shape"""
    if year%4 ==0 : 
        if year%100 == 0:
            if year% 400 == 0 :
                return True
            else : 
                return False
        else : 
            return True
    else:
        return False 

def day_in_month(Y,M):
    """this function get the year and month and returns
    the number of days that are in this monnth"""
    M-=1
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31] 
    if is_leap(Y)and M == 1:
        return 29
    else:
        return month_days[M]



year = int(input("Enter year :"))
month = int(input("Enter month :"))
days= day_in_month(year,month)
print(days)
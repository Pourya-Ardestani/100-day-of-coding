import random 
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','$','#','%','^','&','*','(',')','-','_','+','|','/']
numbers = [0,1,2,3,4,5,6,7,8,9]
# print(len(symbols))


print("welcome to the password generator ! ")
n_letters = int(input("how many letters do you want in your password : "))
n_symbols = int(input("how many symbols do you want : "))
n_numbers = int(input("how many numbers do you need : "))
 
#//////////////////////////////////////////////////////////////////////////
n_total = n_letters + n_symbols + n_numbers
password = []
for i in range(1,n_total):
    if i <= n_letters :
        password.append(letters[random.randint(0,25)])
    if i <= n_symbols :
        password.append(symbols[random.randint(0,14)])
    if i <= n_numbers :
        password.append(numbers[random.randint(0,9)])  

random.shuffle(password)          
s_password = ""
for i in range(0,n_total):
    s_password += str(password[i])
print(s_password)    

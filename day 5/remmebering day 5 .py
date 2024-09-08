import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','$','#','%','^','&','*','(',')','-','_','+','|','/']
numbers = ['0','1','2','3','4','5','6','7','8','9']

N_letter = int(input("how many letters do you want in your password ?"))
N_symbol = int(input("how many symbols? : "))
N_number = int(input("how many numbers do you wany ? :"))

password = []

for i in range(0,N_letter) :
    password += random.choice(letters)
for i in range(0,N_symbol) :
    password += random.choice(symbols)
for i in range(0,N_number) :
    password += random.choice(numbers)

random.shuffle(password)    
n_total = N_letter+N_number+N_symbol
string_password = ''


for  pass_key in range(0,n_total) :
    string_password += password[pass_key] 

print(string_password)    
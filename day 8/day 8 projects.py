import logo
list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encode(massage,shift):
    new_massage = ''
    for letter in massage:
        for i in range(len(list)):
            if letter == list[i]:
                if i+shift < 26:
                    new_massage += list[i+shift]
                else :
                    new_massage += list[i+shift-26]
    print(f"massage : {new_massage}")                

def decode(massage,shift):
    new_massage = ''
    for letter in massage:
        for i in range(len(list)):
            if letter == list[i]:
                if i-shift >= 0 :
                    new_massage += list[i-shift]
                else :
                    new_massage += list[i-shift+26]
    print(f"massage : {new_massage}")                
        
# start
end_program = False
print(logo)
while not end_program :
    user_wants = input('do you want to "encode" or "decode" ? ').lower()
    massage = input("Enter your sentenc : ")
    shift = int(input("shift :"))
    if user_wants == "encode" :
        encode(massage,shift) 
    elif user_wants == "decode":
        decode(massage,shift)
    else :
        print("ERROR \n you entered a wrong choice ")
    again = input("do you want to do again ? ").lower()
    if again == "no" :
        end_program = True    


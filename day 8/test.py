list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
massage = "helloz"
shift = 1
new_massage = ''
for letter in massage:
    for i in range(len(list)):
        if letter == list[i]:
            if i+shift < 26:
                new_massage += list[i+shift]
            else :
                new_massage += list[i+shift-26]




print(f"massage : {new_massage}")
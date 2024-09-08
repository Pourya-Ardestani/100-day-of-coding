import random
print("WELCOME TO CHOOSE GAME !!\nPlease enter a numbere for gussing the treasure : \n")
row1 = ['✉️','✉️','✉️']
row2 = ['✉️','✉️','✉️']
row3 = ['✉️','✉️','✉️']
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

guss = list(input())
T_row = random.randint(0,2)
T_column = random.randint(0,2)

print(f"you guss is {guss}")
print(f"the treasure is in {T_row+1},{T_column+1}")

user_row = int(guss[0])-1
user_column= int(guss[1])-1

map[user_row][user_column] = '❌'
map[T_row][T_column] = '💸'


if user_row ==T_row and user_column == T_column :
    print("You find the treasure horay !!!!!🎊 🎉")
else:
    print("GAME OVER")   

print(f"{row1}\n{row2}\n{row3}")    
students_hight = input("Enter a list of students hight :").split()
sum = 0
count =0
lenght = len(students_hight)
for i in range(0,lenght) :
    students_hight[i] = int(students_hight[i])
    sum += students_hight[i]
    count +=1

print(count)
avg =round( sum / count)
print(f"average = {avg} ")

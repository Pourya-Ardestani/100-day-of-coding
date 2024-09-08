students_score = input("Enter a list of students scores : ").split()
lenght = len(students_score)
for score in range(0,lenght):
    students_score[score] = int(students_score[score])
#list of int now
max = 0
for score in students_score :
    if max < score :
        max = score

print(f"the max score in these scores is : {max}")
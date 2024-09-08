#list1 = []
#list2 = []
with open("file1.txt") as file1:
    str_list1 = file1.read().split()
    list1 = [int(number) for number in str_list1]

with open("file2.txt") as file2:
    str_list2 = file2.read().split()
    list2 = [int(number) for number in str_list2]

result = [number for number in list1 if number in list2]

print(list1)
print(list2)
print(result)
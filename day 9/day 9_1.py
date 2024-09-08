# day 9_1
student_dictionary = {
   "Harry":81 ,
   "Ron":78,
   "Hermione":99,
   "Draaco":74,
   "Neville":62, 
}
# 
new_dic = {}
Grade_in_string = ""
for key in student_dictionary :
    Grade = student_dictionary[key]
    if Grade >=90 and Grade <=100:
        Grade_in_string = "Outstanding"
    elif Grade >=81 and Grade<=90  :
        Grade_in_string = "Exeed Expectation"
    elif  Grade >=71 and Grade<=80  :    
        Grade_in_string = "Acceptable"
    else :
        Grade_in_string = "Fail"
    new_dic[key] = Grade_in_string 


print(new_dic)
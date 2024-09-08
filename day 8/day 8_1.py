def can_need(Hight,Width,Coverage):
    result = round((Hight*Width/Coverage)+.4)
    return result

hight = int(input("hight = "))
width = int(input("width = "))
coverage = 5

print(f" you need {can_need(hight,width,coverage)} can of paint")

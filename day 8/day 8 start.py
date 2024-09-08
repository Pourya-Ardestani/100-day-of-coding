def greet():
    print(" hello!\n nice to meet you \n let's play game")
greet()    

def greet_with_2_parameter(name,location):
    print(f"hello {name}")
    print(f"what is it like in {location} ?")
n = input("name:") 
l = input("location:")
greet_with_2_parameter(location =l,name = n)
     
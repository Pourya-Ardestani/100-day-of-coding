from turtle import Turtle , Screen


jimmy = Turtle()
print(jimmy)
screen_show = Screen()
jimmy.shape("turtle")
jimmy.color("Blue")
jimmy.forward(40)
jimmy.left(100)
jimmy.forward(100)
jimmy.right(100)
jimmy.forward(200)
#print(screen_show.canvheight)
screen_show.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

table.align["Pokemon Name"] = "l"
table.align["Type"] = "r"
print(table)

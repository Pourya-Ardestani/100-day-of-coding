import tkinter


def button_clicked():
    string_from_Entry = input.get()
    label.config(text=string_from_Entry)


def button2_get_clicked():
    print("button2 got clicked")

#window
window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#lable
label = tkinter.Label(text="Salam")
label.grid(column=0, row=0)

#Button1
button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)
 
#Buttom2
button2 = tkinter.Button(text="newButton", command=button2_get_clicked)
button2.grid(column=2 , row=0)

#Entry
input = tkinter.Entry()
input.grid(column=3, row=2)

window.mainloop()

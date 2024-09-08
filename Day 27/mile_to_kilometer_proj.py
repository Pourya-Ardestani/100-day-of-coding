import tkinter


def calculate():
    distance_in_mile = float(entry_box.get())
    distance_in_km = distance_in_mile*1.609
    result_label.config(text=distance_in_km)


window = tkinter.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=200, height=100)
window.config(padx=15, pady=10)

#Entry Box for Miles input
entry_box = tkinter.Entry(width=5)
entry_box.config()
entry_box.insert(tkinter.END, string='0')
entry_box.grid(column=1, row=0)

#Label Miles
mile_label = tkinter.Label(text="Miles")
mile_label.grid(column=2, row=0)

#label is qqual:
is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

#label for number
result_label = tkinter.Label(text=0)
result_label.grid(column=1, row=1)

#label Km:
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

#Button calculate
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)



window.mainloop()
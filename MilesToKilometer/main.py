from tkinter import *

def calculate():
    num = round(int(input.get()) * 1.60934, 2)
    conversion.config(text=num)

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(250, 100)
window.config(padx=20, pady=20)

str_miles = Label(text="Miles", font=("Arial", 10))
str_miles.grid(column=2, row=0)
str_miles.config(padx=5, pady=5)

str_is_equal_to = Label(text="is equal to", font=("Arial", 10))
str_is_equal_to.grid(column=0, row=1)

str_km = Label(text="Km", font=("Arial", 10))
str_km.grid(column=2, row=1)

conversion = Label(text= 0, font=("Arial", 10))
conversion.grid(column=1, row=1)
conversion.config(padx=5, pady=5)

calc_button = Button(text="Calculate", font=("Arial", 10), command=calculate)
calc_button.grid(column=1, row=2)

input = Entry(width=10, font=("Arial", 10))
input.grid(column=1, row=0)


window.mainloop()
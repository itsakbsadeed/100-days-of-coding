from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def mile_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")


# miles_input
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Miles
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# is equal to
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

# KM_input
km_result = Label(text="0")
km_result.grid(column=1, row=1)


#KM
km = Label(text="Km")
km.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()



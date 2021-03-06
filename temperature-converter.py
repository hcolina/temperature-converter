import tkinter as tk

def fahrenheit_to_celsius():
    #this function converts F>C
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

#window set-up
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

#Fahrenheit entry frame with an Entry widget and label
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

#Use .grid() geometry manager to layout the temperature Entry and Label in frm_entry
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

#Creates the conversion Button and the result display Label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window,text="\N{DEGREE CELSIUS}")

#Layout using .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=0)
btn_convert.grid(row=0, column=1,pady=10)
lbl_result.grid(row=0, column=2, padx=10)

#Run the application
window.mainloop()

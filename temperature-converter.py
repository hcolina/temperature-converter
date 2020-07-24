import tkinter as tk

def fahrenheit_to_celcius():
    #this function converts F>C
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N {DEGREE CELSIUS}"

#window set-up
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

#Fahrenheit entry frame with an Entry widget and label
frm-entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_temperature.grid(row=0, column=0, sticky=e)


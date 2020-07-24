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

frm-entry = tk.Frame(master=window)
ent_temperature = tk.Entry()


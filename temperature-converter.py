import tkinter as tk

def fahrenheit_to_celcius():
        '''This converts the Fahrenheit value into Celcius and inputs the
        result into the lbl_result'''
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N {DEGREE CELSIUS}"

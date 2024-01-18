from cgitb import text
from queue import Full
import tkinter as tk
from turtle import width
import customtkinter

# from pkg_resources import evaluate_marker

customtkinter.set_appearance_mode("dark") # system, light, dark
customtkinter.set_default_color_theme("dark-blue") # blue, green, dark

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation(): 
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    pass

# Interface dimenssions
root = customtkinter.CTk()
root.geometry("400x500")
root.title("Python Calculator")

# add frame
#frame = customtkinter.CTkFrame(master=root)
#frame.pack(pady=20, padx=60, fill="both", expand=True)

# Text box which shows calculations
text_result = customtkinter.CTkTextbox(root, height=2, width=20, font=("Arial", 24))
text_result.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")  # Centered and expanded


# Function to create buttons
def create_button(text, command, row, column, width=5):
    btn = customtkinter.CTkButton(root, text=text, command=command, width=width, font=("Arial", 14))
    btn.grid(row=row, column=column, padx=10, pady=10, sticky="ew")


# Operation buttons
create_button("+", lambda: add_to_calculation("+"), row=2, column=4)
create_button("-", lambda: add_to_calculation("-"), row=3, column=4)
create_button("x", lambda: add_to_calculation("*"), row=4, column=4)
create_button("/", lambda: add_to_calculation("/"), row=5, column=4)

# Bracket buttons
create_button("(", lambda: add_to_calculation("("), row=2, column=2)
create_button(")", lambda: add_to_calculation(")"), row=2, column=3)

create_button(".", lambda: add_to_calculation("."), row=6, column=3)

# Numbers
create_button("0", lambda: add_to_calculation("0"), row=6, column=2)
create_button("1", lambda: add_to_calculation("1"), row=5, column=1)
create_button("2", lambda: add_to_calculation("2"), row=5, column=2)
create_button("3", lambda: add_to_calculation("3"), row=5, column=3)
create_button("4", lambda: add_to_calculation("4"), row=4, column=1)
create_button("5", lambda: add_to_calculation("5"), row=4, column=2)
create_button("6", lambda: add_to_calculation("6"), row=4, column=3)
create_button("7", lambda: add_to_calculation("7"), row=3, column=1)
create_button("8", lambda: add_to_calculation("8"), row=3, column=2)
create_button("9", lambda: add_to_calculation("9"), row=3, column=3)

# Clear buttons
create_button("C", clear_field, row=2, column=1)
create_button("=", evaluate_calculation, row=6, column=4)

# run application
root.mainloop()
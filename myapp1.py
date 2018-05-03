import ctypes
import random
import tkinter as tk
# ----------INITIALIZE-----------
user32 = ctypes.windll.user32
screensize = str(user32.GetSystemMetrics(0)) + "x" + str(user32.GetSystemMetrics(1))
window = tk.Tk()
window.title("Greetings _____")
window.geometry(screensize)
# ----------FUNCTION-----------
def phrase_generator():
	phrases = ["Hello", "Bonjour", "Hola", "Aloha"]
	name =  str(entry1.get())
	return phrases[random.randint(0, 3)] + " " + name
	
def phrase_display():
	greeting = phrase_generator()
	# This creates the text field
	greeting_display = tk.Text(master=window, height=10, width=30)
	greeting_display.grid(column=0, row=3)
	greeting_display.insert(tk.END, greeting)
# ----------LABEL-----------
lable1 = tk.Label(text="Welcome to my app")
lable1.grid(column=0, row=0)

lable2 = tk.Label(text="What is your name?")
lable2.grid(column=0, row=1)

# ----------ENTRY-----------
entry1 = tk.Entry()
entry1.grid(column=1, row=1)

# ----------BUTTON-----------
button1 = tk.Button(text="Click me!", bg="red", command=phrase_display)
button1.grid(column=0, row=2)

window.mainloop()
import tkinter as tk

def show_message():
    user_text = entry.get()
    label.config(text="You typed: " + user_text)

window = tk.Tk()
window.title("Simple Desktop App")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Submit", command=show_message)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()

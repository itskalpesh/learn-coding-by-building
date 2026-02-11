import tkinter as tk
from datetime import datetime

def process_command():
    command = entry.get().lower()
    
    if command == "hello":
        response = "Hello there!"

    elif command == "time":
        now = datetime.now()
        response = "Current time: " + now.strftime("%H:%M")

    elif command.startswith("add"):
        parts = command.split()
        if len(parts) == 3:
            try:
                num1 = float(parts[1])
                num2 = float(parts[2])
                response = "Result: " + str(num1 + num2)
            except:
                response = "Invalid numbers."
        else:
            response = "Usage: add 5 7"

    elif command == "exit":
        window.destroy()
        return

    else:
        response = "I don't understand that command."

    output_label.config(text=response)


# Create window
window = tk.Tk()
window.title("Desktop AI Assistant")

# Input field
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# Button
button = tk.Button(window, text="Submit", command=process_command)
button.pack()

# Output label
output_label = tk.Label(window, text="", font=("Arial", 12))
output_label.pack(pady=10)

window.mainloop()

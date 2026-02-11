import tkinter as tk

class VEDUI:
    def __init__(self, process_function):
        self.process_function = process_function

        self.window = tk.Tk()
        self.window.title("VED Assistant")

        self.entry = tk.Entry(self.window, width=40)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(
            self.window,
            text="Submit",
            command=self.handle_submit
        )
        self.submit_button.pack()

        self.output_label = tk.Label(
            self.window,
            text="",
            font=("Arial", 12),
            wraplength=300
        )
        self.output_label.pack(pady=10)

    def handle_submit(self):
        command = self.entry.get().lower()
        response = self.process_function(command)
        self.output_label.config(text=response)

    def run(self):
        self.window.mainloop()

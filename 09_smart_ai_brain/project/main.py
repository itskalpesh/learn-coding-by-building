from datetime import datetime

def say_hello():
    print("Hello there!")

def show_time():
    now = datetime.now()
    print("Current time is", now.strftime("%H:%M"))

def add_numbers(a, b):
    print("Result is", a + b)

while True:
    command = input("You: ").lower()

    if command == "hello":
        say_hello()

    elif command == "time":
        show_time()

    elif command.startswith("add"):
        parts = command.split()
        if len(parts) == 3:
            num1 = float(parts[1])
            num2 = float(parts[2])
            add_numbers(num1, num2)
        else:
            print("Usage: add 5 7")

    elif command == "exit":
        print("Goodbye!")
        break

    else:
        print("I don't understand that command.")

from datetime import datetime

def say_hello():
    return "Hello, I am VED."

def show_time():
    now = datetime.now()
    return "Current time is " + now.strftime("%H:%M")

def add_numbers(command):
    parts = command.split()
    if len(parts) == 3:
        try:
            num1 = float(parts[1])
            num2 = float(parts[2])
            return str(num1 + num2)
        except:
            return "Invalid numbers."
    else:
        return "Usage: add 5 7"

def show_help():
    return (
        "Available commands:\n"
        "- hello\n"
        "- time\n"
        "- add X Y\n"
        "- exit"
    )

def process_command(command):
    if command == "hello":
        return say_hello()

    elif command == "time":
        return show_time()

    elif command.startswith("add"):
        return add_numbers(command)

    elif command == "help":
        return show_help()

    elif command == "exit":
        return "exit"

    else:
        return "I don't understand that command."


def main():
    print("VED Text Brain Activated.")
    
    while True:
        command = input("You: ").lower()
        response = process_command(command)

        if response == "exit":
            print("VED: Goodbye.")
            break

        print("VED:", response)


if __name__ == "__main__":
    main()

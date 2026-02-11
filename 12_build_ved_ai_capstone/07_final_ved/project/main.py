from ui import VEDUI
from tools import get_time, get_date, add_numbers, help_menu
from memory import remember, recall
from voice import speak
from vision import detect_faces


def process_command(command):
    if command == "hello":
        return "Hello, I am VED."

    elif command == "time":
        return get_time()

    elif command == "date":
        return get_date()

    elif command.startswith("add"):
        parts = command.split()
        if len(parts) == 3:
            return add_numbers(parts[1], parts[2])
        return "Usage: add 5 7"

    elif command.startswith("remember"):
        parts = command.replace("remember ", "").split(" is ")
        if len(parts) == 2:
            remember(parts[0], parts[1])
            return "I will remember that."
        return "Usage: remember key is value"

    elif command.startswith("what is"):
        key = command.replace("what is ", "")
        value = recall(key)
        if value:
            return f"{key} is {value}"
        return "I don't remember that."

    elif command == "vision":
        detected = detect_faces()
        return "Face detected." if detected else "No face detected."

    elif command == "help":
        return help_menu()

    elif command == "exit":
        return "exit"

    else:
        return "I don't understand."


def main():
    def wrapped_process(command):
        response = process_command(command)

        if response != "exit":
            speak(response)

        return response

    ui = VEDUI(wrapped_process)
    ui.run()


if __name__ == "__main__":
    main()

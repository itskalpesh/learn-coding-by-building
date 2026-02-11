from datetime import datetime

def get_time():
    now = datetime.now()
    return "Current time is " + now.strftime("%H:%M")

def get_date():
    now = datetime.now()
    return "Today is " + now.strftime("%A, %d %B %Y")

def add_numbers(a, b):
    try:
        return str(float(a) + float(b))
    except:
        return "Invalid numbers."

def help_menu():
    return (
        "Available commands:\n"
        "- hello\n"
        "- time\n"
        "- date\n"
        "- add X Y\n"
        "- remember key is value\n"
        "- what is key\n"
        "- vision\n"
        "- exit"
    )

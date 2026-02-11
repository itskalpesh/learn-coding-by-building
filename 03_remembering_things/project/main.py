try:
    file = open("name.txt", "r")
    name = file.read()
    file.close()
    print("Welcome back,", name)

except:
    print("What is your name?")
    name = input()

    file = open("name.txt", "w")
    file.write(name)
    file.close()

    print("Nice to meet you,", name)
try:
    file = open("sample.txt", "r")
    content = file.read()
    file.close()
    print("File Content:\n", content)

except:
    print("File not found. Create 'sample.txt' first.")

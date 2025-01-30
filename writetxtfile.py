with open('file.txt', 'w') as file:
    file.write("I'm working at Bestpeers.")

with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
# Write a Python program to read a file and print its content

with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
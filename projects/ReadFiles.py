# Files in Python

secret_file = open("secret", "r")
content = secret_file.read()
secret_file.close()
print(content)

with open("secret", "r") as content:
    print(content.read()) # read all the file
    print(content.readline()) # read the first line
    print(content.readlines()) # rad the file as a list
    for fruit in content.readlines():
        print("This is a fruit: ",fruit, end="")
    print(content.read(20)) #read just 20 caracters
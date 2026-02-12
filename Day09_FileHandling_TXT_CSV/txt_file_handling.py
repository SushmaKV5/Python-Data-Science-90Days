#Reading a text file

file = open("sample.txt", "r")
content = file.read()
file.close()

print("Reading from the file:")
print(content)

with open("sample.txt","r") as file:
    lines = file.readlines()
    print("No. of lines:", len(lines))

#Writing a new text file
new_file = open("output.txt", "w")
new_file.write("This file is created using python file handling!")
print("output.txt file created successfully!")
new_file.close()
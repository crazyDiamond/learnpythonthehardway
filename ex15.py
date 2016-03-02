from sys import argv

script, file_name = argv

text = open(file_name)

print("Here's your file: %r" %(file_name))
print(text.read())
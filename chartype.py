import re
for character in range(4):
    character = input("Enter a character: ")
    if re.match(r'[a-z]+',character):
            print(character, "is a lower case letter.")
    elif re.match(r'[A-Z]',character):
            print(character, "is an upper case letter.")
    elif re.match(r'[0-9]+',character):
            print(character, "is a digit.")
    else:
            print(character, "is a non-alphanumeric character.")
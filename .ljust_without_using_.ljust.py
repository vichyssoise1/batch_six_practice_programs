#User input text and width for spaces
text = input("Enter string: ")
width = int(input("Enter the total width: "))

if len(text) < width:
    text += " " * (width - len(text))  # Add spaces to the right to fill the width

print("The string is: ", text)
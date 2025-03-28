#User input
text = input("Enter a string: ")
width = int(input("Enter the total width: "))

if len (text) < width:
    spaces = (width - len(text)) // 2
    text = " " * spaces + text + " " * (width - len(text) - spaces)

print("The centered string is: ", text)
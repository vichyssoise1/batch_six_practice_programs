#User input
text = input("Enter a string: ")

if text:
    # Capitalize the first letter of the string
    result = text[0].upper() + text[1:].lower()
else:
    result = text 

print("The string is: ", result)

#User input
text = input("Enter a string: ")

# Swap case without using swapcase() method
text = ''.join(char.lower() if char.isupper() else char.upper() for char in text)

print("The reversed string is: ", text)
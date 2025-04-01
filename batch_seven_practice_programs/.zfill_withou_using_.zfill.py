# Add user input
text = input("Enter text: ")
width = int(input("Enter total width: "))

# Function to add zero at the beginning of the string to complete the total width
padded_text = '0' * (width - len(text)) + text if len(text) < width else text 

# print the result
print("Zero-padded text:", padded_text)
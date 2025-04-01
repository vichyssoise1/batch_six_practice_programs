# Create user inpur
text = input("Enter a string: ")
width = int(input("Enter the total width: "))

# Function to right justify a string without using rjust()
# Add space characters at the beginning of the string to complete the total width
padded_text = ' ' * (width - len(text)) + text if len(text) < width else text

# Print the result
print("Right-justified string:", padded_text)

# Create user input
text = input("Enter a string with trailing spaces: ")

# Remove trailing spaces manually
while text and text[-1] == " ":
    text = text[:-1]

# Print if it works
print("You entered: ", text)
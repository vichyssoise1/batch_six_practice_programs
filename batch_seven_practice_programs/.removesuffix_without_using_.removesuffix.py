# Create user input
text = input("Enter a string: ")
suffix = input("Enter a suffix: ")

# Function to check if the string ends with the given suffix
if text.endswith(suffix):
    text = text[:-len(suffix)] # Remove the suffix from the string

# Print the result of the function
print("Your string after removing the suffix: ", text)

# Create user input
text = input("Enter text: ")
substring = input("Enter the substring to search for: ")

# Find the first occurrence of the substring in the text
position = text.find(substring)

# Print the result
print(f"The first occurrence of '{substring}' is at index {position}" if position != -1 else "Substring not found.")
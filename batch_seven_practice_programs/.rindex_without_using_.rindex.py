# Create user input 
text = input("Enter string: ")
substring = input("Enter the substring to search for: ")

# Find the last occurrence of the substring manually
position = text.rfind(substring)

# Print the result
print(f"The last occurrence of '{substring}' is at index {position}" if position != -1 else "Substring not found.")
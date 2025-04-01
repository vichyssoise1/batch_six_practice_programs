# Add user input
text = input("Enter string: ")

# Convert to uppercase without using the upper() method
uppercase_text = ''.join(chr(ord(char) - 32) if 'a' <= char <= 'z' else char for char in text)

# Print the result
print("Uppercased string: ", uppercase_text)
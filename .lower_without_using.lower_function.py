#user input
text = input("Enter a string: ")

# Convert uppercase letters (A-Z) to lowercase manually
lower_text = "".join(chr(ord(char) + 32) if 'A' <= char <= 'Z' else char for char in text)

print("Lowercase string:", lower_text)

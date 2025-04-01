# Add user input to collect the string
text = input("Enter a string: ")

# Check if the string is lowercase without using .islower()
all_lower = all('a' <= char <= 'z' for char in text if char.isalpha())

# Check if it works
print("The String is all loercase: ", all_lower)
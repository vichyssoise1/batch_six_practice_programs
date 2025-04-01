# Create user input for string
text = input("Enter a string: ")
prefix = input("Enter the beggining to check: ")

# Check if the string starts with the given prefix without using .startswith()
is_starting = text[:len(prefix)] == prefix if len(prefix) <= len(text) else False

# Print the result
print("Does the string start with the given prefix?", is_starting)
# Create user input
text = input("Enter a string: ")
subtring = input("Enter the substring to count: ")

# Count the occurrences of the substring manually
count = text.split(subtring) # Split the string by the substring
occurrences = len(count) - 1 # The number of times the substring appears

# print the result
print(f"The substring '{subtring}' appears {occurrences} times in the string.")
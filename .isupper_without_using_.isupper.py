#User input
text = input("Enter a string: ")

#Check if all the letters are uppercase
is_upper = all('A' <= char <= 'Z' for char in text if char.isalpha())

print("Is the string in uppercase?: ", is_upper)
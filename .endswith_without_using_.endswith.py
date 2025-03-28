#user input
text = input("Enter a string: ")
suffix = input("Enter the edning to check: ")

#Check if the string ends with the given suffix
ends_with = text[-len(suffix):] == suffix

print("Does the string end with the given suffix?", ends_with)
#User input and the prefix to remove
text = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")

#funtion to remove the prefix
if text.startswith(prefix):
    text = text[len(prefix):] # remove the prefix

#check if it works
print("Starting without the prefix: ", text)
#User input
text = input("Enter a string: ")

words = text.split()  # Split the string into words
capitalized_words = [word[0].upper() + word[1:].lower() if word else "" for word in words] # Capitalize each word
result = " ".join(capitalized_words)  # Join the words back into a string
print("Title cased string:", result)  # Print the result
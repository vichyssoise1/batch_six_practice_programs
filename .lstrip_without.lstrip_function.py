#User Input
full_name = input("Enter your full name: ")
full_name = " ".join(full_name.split()) #remove leading spaces without using lstrip function
print("Your name without leading spaces is: ", full_name)
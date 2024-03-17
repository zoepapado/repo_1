#request name, age, house number and street name from the user
#store these into variables called 'name', 'age', 'house_number' and 'street_name' respectively
#print a sentence which incorporates these variables, i.e. 'This is [name]. He is [age] years old and lives at house number [house_number] on [street_name]'
#make sure to change all variable types to strings (if the input types were integers) where necessary

name = input('What is your full name?')
age = input('How old are you (in years)?')
house_number = input('What is your house number?')
street_name = input('What is the name of your street?')

print(f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name}.")

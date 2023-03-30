# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

name = input('What is your name? ')
location = input('Where are you located? ')


def greet(name, location):
    print(f'Hello {name}')
    print(f'I am a machine, {name}')
    print(f'What is it like in {location}')


greet(name=name, location=location)

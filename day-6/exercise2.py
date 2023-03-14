# Exercise Source: https://holypython.com/intermediate-python-exercises/exercise-9-python-while-loop/

# Using a while loop, len function, an if statement and the str() function; iterate through the given list and if there is a 100, assign a notification message to the variable my_message with the index of 100.
# i.e.: "There is a 100 at index no: 5"

lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]

i = 0

while i < len(lst):
    if lst[i] == 100:
        my_message = f"There is a 100 at index {i}"
    i = i + 1
print(my_message)
print(lst[12])

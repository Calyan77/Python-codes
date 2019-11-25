# This program take inpute from the user and swap the value

# taking inputs from the user
first_number = input('Enter first_number: ')
second_number = input('Enter second_number: ')

# printing the number before swapping
print('Value of first_number before swapping: ', first_number)
print('Value of second_number before swapping: ', second_number)

# swapping the numbers 
third_number = first_number
first_number = second_number
second_number = third_number

# printing the value after swapping
print('Value of first_number after swapping: ', first_number)
print('Value of second_number after swapping: ', second_number)
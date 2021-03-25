
# Ask the user for two numbers and assign these numbers to variables and replace the values of these variables with each other.
first_num = str(input('Write a number: '))
second_num = str(input('Write one more please: '))
print(first_num, second_num)
b = second_num
second_num = first_num
first_num = b
print(first_num, second_num)
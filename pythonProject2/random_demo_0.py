# 作者: 大数据 浪哥
# 2025年06月12日05时26分04秒
# 1054074422@qq.com

#在Python中，要使用随机数，首先需要导入随机数的模块—— “工具包”
import random

# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)
# Print the random number
print("Random number:", random_number)

# Generate a random float between 0 and 1
random_float = random.random()
# Print the random float
print("Random float:", random_float)

# Generate a random boolean value
random_boolean = random.choice([True, False])
# Print the random boolean value
print("Random boolean:", random_boolean)

# Generate a random string of length 10
random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
# Print the random string
print("Random string:", random_string)


# Generate a random list of length 10 with random integers between 1 and 100
random_list = [random.randint(1, 100) for i in range(10)]
# Print the random list
print("Random list:", random_list)


# Generate a random tuple of length 10 with random integers between 1 and 100
random_tuple = tuple(random.randint(1, 100) for i in range(10))
# Print the random tuple
print("Random tuple:", random_tuple)


# Generate a random dictionary with 10 key-value pairs with random integers between 1 and 100 as values
random_dict = {i: random.randint(1, 100) for i in range(10)}
# Print the random dictionary
print("Random dictionary:", random_dict)


# Generate a random set of length 10 with random integers between 1 and 100
random_set = set(random.randint(1, 100) for i in range(10))
# Print the random set
print("Random set:", random_set)


# Generate a random string of length 10 with only lowercase letters
random_lowercase_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
# Print the random lowercase string
print("Random lowercase string:", random_lowercase_string)


# Generate a random string of length 10 with only uppercase letters
random_uppercase_string = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))
# Print the random uppercase string
print("Random uppercase string:", random_uppercase_string)


# Generate a random string of length 10 with only letters
random_letter_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))
# Print the random letter string
print("Random letter string:", random_letter_string)


# Generate a random string of length 10 with only digits
random_digit_string = ''.join(random.choices('0123456789', k=10))
# Print the random digit string
print("Random digit string:", random_digit_string)


# Generate a random string of length 10 with only special characters
random_special_string = ''.join(random.choices('!@#$%^&*()_+-=[]{}|;:,.<>?', k=10))
# Print the random special string
print("Random special string:", random_special_string)

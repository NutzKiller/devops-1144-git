import random
#if-then statments:
#1
# age = int(input("what is your age? "))
# if age == 16 or age == 17:
#   print('you are almost old enough')
# elif age < 18:
#   print('you are not old enough')
# else:
#   print('you are old enough')

# #2
# number = int(input('Enter a number: '))
# if number % 2 == 0:
#   print('number is even')
# else:
#   print('number is odd')

# #3
# score = int(95)
# if score < 100 and score > 90:
#   print('A')
# elif score < 89 and score > 80:
#   print('B')
# elif score < 79 and score > 70:
#   print('C')
# elif score < 69 and score > 60:
#   print('D')
# elif score > 100 or score < 0:
#   print('Invalid score')
# else:
#   print('F')

#4
# input_number = int(input('Provide number: '))

# if input_number < 0:
#   print(f'{input_number} is a negative number')
# elif input_number == 0:
#   print(f'{input_number} is 0')
# else:
#   print(f'{input_number} is a positive number')


#5
# c_age = int(input("what is your age? "))
# is_student = str(input("are you a student? "))

# if c_age < 18 or is_student == "yes":
#   print('you get a discount')
# else:
#   print('you are paying full price')

  
#for and while loops
#6
# for i in range(1,11):
#   if i % 2 == 0:
#     print(i)

#7
# numbers = []
# for i in range(1, 101):
#   numbers.append(i)
# total = sum(numbers)
# print(total)

#chatgpt way:
#total = sum(range(1, 101))
#print(total)

# #8
# number = int(input("Enter a number: "))
# for i in range(1,11):
#   print(f'{number} x {i} = {number * i}')

# #9
# color_list = ['red', 'green', 'blue', 'yellow']
# for i in color_list:
#   print(i)

# #10
# i = 10
# while i > 0:
#   print(i)
#   i -= 1
#   if i == 0:
#     print('Liftoff!')

# #11
# generated_number = random.randint(1, 10)
# while True:
#   chosen_number = int(input('Choose a number between 1-10: '))
#   if chosen_number == generated_number:
#     print("its right!")
#     break
#   elif chosen_number > generated_number:
#     print('its too high')
#   else:
#     print('number too low')

# print(f'correct number was {generated_number}')

# #12
# guesses = []
# while True:
#   given_number = int(input('give me a number: '))
  
#   if given_number > 0:
#     guesses.append(given_number)
#     print('guess again')
#   else:
#     print('you are right!')
#     break
# guess_sum = sum(guesses)
# print('All your guesses:', guess_sum)

# #13
# def greet():
#   print("hello, world!")
# greet()

# #14
# def greet(name):
#   print(f'hello {name}')

# greet("yuval")

# #15
# def square(number):
#   return number ** 2
# result = square(5)
# print(result)

# #16
# def factorial(n):
#   result = 1
#   for i in range(1, n + 1):
#     result *= i
#   return result
# answer = factorial(5)
# print(answer)

# #17 sasha's work!
# numbers = [1, 2, 3222, 4, 5, 6, 7]
# def find_max(lst):
#   max_number = numbers[0]
#   for i in lst:
#     if max_number < i:
#       max_number = i
#   return max_number

# result = find_max(numbers)
# print(result)

# #18
# def celsius_to_fahrenheit(c):
#   c = (c * 9/5) + 32
#   return c
# result = celsius_to_fahrenheit(10)
# print(result)

# #19
# def is_palindrome(word):
#   if word == word[::-1]:
#     return True
#   else:
#     return False
# result = is_palindrome("dennis")
# print(result)

# #20
# numbers = [10, 20, 30, 40]
# def sum_list(lst):
#   sum_lst = sum(lst)
#   return sum_lst
# sasha = sum_list(numbers)
# print(sasha)

# #21
# def is_prime(number):
#   for i in range(2, int(number ** 0.5) + 1):
#     if number % i == 0:
#       return False
#   return True
    
# check = is_prime(7)
# print(check)


# #22
# def calculator(a, b, operation):
#   if operation == "+":
#      print(a + b)
#   elif operation == "-":
#      print(a - b)
#   elif operation == "*":
#      print(a * b)
#   else:
#     if b == 0:
#       print('you cant dived by zero')
#     else:
#      print(a / b)

# calc = calculator(10, 0, "/")
import random
#chat gpt exercises:
#1 Write a program that asks the user to enter two numbers, then adds, subtracts, multiplies, and divides them. Print each result.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# argument = input("Enter an argument: ")
# def calculate(num1, num2, argument):
#   if argument == "+":
#     return num1 + num2
#   elif argument == "-":
#     return num1 - num2
#   elif argument == "*":
#     return num1 * num2
#   elif argument == "/":
#     if num2 == 0:
#       return "cant divide by 0"
#     else:
#       return num1 / num2
#   else:
#     return "Not a valid argument"
  
# result = calculate(num1, num2, argument)
# print(result)

#2 Ask the user for a number and check if it is even or odd. Print a message indicating the result.

# input_number = int(input("Enter a number: "))
# if input_number % 2 == 0:
#   print("Number is even")
# else:
#   print("Number is odd")

#3 Write a program to convert temperatures between Celsius and Fahrenheit. Prompt the user to choose the conversion type and enter a temperature, then display the converted temperature.

# convert_temp = input("Choose Celsius or Fahrenheit: ")
# degrees = int(input("How many degrees to convert? "))
# def calculate_temp(convert_temp):
#   if convert_temp == "Celsius":
#     new_temperature = (degrees * 9/5) + 32
#     return f'New temperature is: {new_temperature}'
#   elif convert_temp == "Fahrenheit":
#     new_temperature = (degrees -32) * 5/9
#     return f'New temperature is: {new_temperature}'
# answer = calculate_temp(convert_temp)
# print(answer)

#4 Create a program that takes principal, rate of interest, and time in years as input and calculates simple interest.

# interest_rate = float(input("Enter interest rate: "))
# year_number = int(input("Enter number of years: "))
# amount = int(input("Enter amount of investment: "))
# def calculate_interest(interest_rate, year_number, amount):
#   return (interest_rate * amount) * year_number
# answer = calculate_interest(interest_rate, year_number, amount)
# print(answer)

# #5 Ask the user to enter a word, then print the word reversed.
# new_word = str(input("Enter a word: "))
# def reversing_word(new_word):
#   return new_word[::-1]
# answer = reversing_word(new_word)
# print(answer)

#6 Write a program where the computer randomly selects a number between 1 and 10. Ask the user to guess the number and print if they’re correct or not.

# guess = None
# generated_number = random.randint(1, 10)

# while guess != generated_number:
#     guess = int(input("Please enter a number between 1 and 10: "))
    
#     if guess == generated_number:
#         print("Spot on! You guessed it right!")
#     elif guess > generated_number:
#         print("Too high! Try again.")
#     else:
#         print("Too low! Try again.")

#  #8 Ask the user to input a number, then print the multiplication table for that number up to 10.
# entered = int(input("Please enter a number: "))
# def multiplier(entered):
#   for i in range(1,11):
#     result = i * entered
#     print(result)
# multiplier(entered)

#9 Write a program that takes a string as input and counts the number of vowels (a, e, i, o, u) in it.
# string = str(input("Provide a string: "))
# number_of_vowels = 0
# vowels = ("a", "e", "i", "o", "u")
# for i in string:
#     if i in vowels:
#       number_of_vowels += 1
# print(number_of_vowels)

#10 Create a list of random numbers. Write a program to find and print the sum of numbers in the list.

# new_list = [1, 5, 8, 2, 5, 1]
# total_value = 0
# for i in new_list:
#   total_value += i
# print(total_value)  
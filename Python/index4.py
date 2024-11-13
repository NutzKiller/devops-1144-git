# #1
# for i in range(1, 10): #loop over the numbers 1-9
#     if i % 2 == 0: #checks if i is even
#         print(i * i) #prints the square of i if i is even
# #output:
# #4, 16, 36, 64

# #2
# word = "hello" #gives word the value "hello"
# new_word = word[1:] + word[0] # this will copy all the values except the first index and will add the first index (word[0]) at the start of the line
# print(new_word) #output: "elloh"

# #3
# numbers = [1, 2, 3, 4, 5] #define the list
# squared_numbers = [n ** 2 for n in numbers if n % 2 == 1] #if the number is not even, it will square the number
# print(squared_numbers)
# #output: 1*1 = 1, 3*3 = 9 5*5 = 25
# #result: numbers =[1,9,25]

# #4
# fruits = {"apple": 3, "banana": 5, "cherry": 2} #define the dict
# total = 0 #define a variable
# for fruit in fruits:
#   total += fruits[fruit] #loop threw the dict and add the value of each index into the total of total
# print(total) #prints the values of all keys in the fruits dict
# #output: 10

# #5
# text = "Python" #define text value to be "Python"
# result = "" #define result as empty value.
# for char in text:  #iterates all characters inside text(going threw each character in "python")
#   result = char + result #print result for each iteration one after the other in result.
# print(result) #output: result = "nohtyp"

# #6
# set_a = {1, 2, 3} #define a set
# set_b = {2, 3, 4} #define b set
# result = set_a.symmetric_difference(set_b) #define the result as a symmetric difference between set_a and set_b (combine both sets and output only the one timers in each set)
# print(result) #output: {1,4}

# #7
# def greet(name="stranger"): #define a function named greet with the default value for name= "stranger"
#   print(f"Hello, {name}!") #prints a sentence with the variable defined in the function
# greet() #output "Hello, stranger!"
# greet("Alice") #output "Hello, Alice!"

# #8
# sentence = "This is a simple sentence." #define sentence with a value(the sentence)
# count = sentence.count("s") #define variable named count that counts the number of time there is an "s" in the sentence
# print(count) #output 4

# #9
# x = 10 #define x with the value 10
# y = 5 #define y with the value 5
# z = x > y and y < 0 or x < 0 #checks if 10(x) is bigger than 5(y) and 5(y) is smaller than 0 or 10 is smaller than 0.
# #that returns False, because both return False
# print(z) #output False

# #10
# n = 1 #define n the value 1
# while n < 10: #start while loop while 10 is bigger than n
#  print(n) #prints the value of n
#  n += 3 #adds 3 after every iteration to the value of n
#  # output: 1, 4, 7

# #11
# values = (1, 2, 3) #define a list named values with 1, 2, 3
# a, b, c = values #define a, b, c to the values in values(a = 1, b = 2, c = 3)
# print(a + b + c) #output (1 + 2 + 3) = 6

# #12
# data = [10, 20, 30, 40, 50] #define a list named data with values
# print(data[-3]) #print the 3 value from the end of the data list
# #output = 30

# #13
# info = {"name": "Alice", "age": 25} #define a dictionary with 2 key:value
# info["age"] = 26 #redefine age as 26 instead of 25
# print(info) #print the dictionary
# #output: {"name": "Alice", "age": 26}

# #14
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #define a list with 3 lists inside
# result = [row[1] for row in matrix] #define result as the [1] index and for loop each row in the second index
# print(result) #output: [2,5,8]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
fruits = ["apple", "orange", "kiwi"]
for i in range(len(numbers)):
  print(i)
               
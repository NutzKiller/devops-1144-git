# #dict
# new_dict = {
#   "name": "Alice",
#   "age": 25,
#   "city": "New York"
# }

# new_dict["job"] = "Engineer"

# for key, value in new_dict.items():
#   print(f"{key}: {value}")

# def new_function(dict):
#   for key, value in dict.items():
#     print(f"{key}: {value}")

# print(new_function(new_dict))

# new_dict.pop("job")
# print(new_dict)

# #functions
# def greet(name = "Guest"):
#   return "Hello, " + name + "!"

# print(greet("Yuval"))
# print(greet())

# def add_function(x, y):
#   return x + y

# print(add_function(2, 3))

# def factorial(x):
#   return 1 if x == 0 else x * factorial(x - 1)

# print(factorial(5))

# def double(list):
#   return [x * 2 for x in list]

# print(double([1, 2, 3, 4]))


# #global local scope
# x = 10
# def global_scope():
#   global x
#   y = 15
#   x += 20
#   print(x)
#   print(y)

# global_scope()
# print(x)

# a = 100
# b = 200
# def another_scope():
#   global a
#   global b
#   a = 2000
#   return a + b
# print(another_scope())
# print(a)

# def local_scope():
#   z = 5
#   if z == 5:
#     z += 10
#     print(z)

# local_scope()

# numbers = [1, 2, 3, 4, 5]
# for i in numbers:
#   print(i)

# count = 0
# while count <= 4:
#   print(count)
#   count += 1

# sum = 0
# num_list = [10, 20, 30, 40, 50]
# for i in num_list:
#   sum = sum + i
# print(sum)

# Outer loop for rows
for i in range(1, 4):
    # Inner loop for columns
    for j in range(1, 4):
        product = i * j
        print(f"{i} * {j} = {product}")
    print()  # Print a new line after each row

while True:
    user_input = input("Enter a number: ")
    if user_input == "stop":
        break
    else:
        print(f"You entered: {user_input}")
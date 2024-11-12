
age = 24
name = "Yuval"
print(f'Your name is: {name}. Your age is: {age}') # Your name is: Yuval. Your age is: 24

x = 10
y = 5
add_sum = x + y
minus_sum = x - y
divide_sum = x / y
multiply_sum = x * y
print(add_sum, minus_sum, divide_sum, multiply_sum) # 15 5 2.0 50

a = 3
b = 7
temp = a
a = b
b = temp
print(a, b) # 7 3


length = input("what is the length?: ")

width = y
area = length * width
print(area)

greeting = "Hello, World!"
print(len(greeting)) 
print(greeting[0])
print(greeting[-1])

first_name = "Yuval"
Last_name = "Shmuely"
full_name = first_name + " " + Last_name
print(full_name)

print(f'Hey my name is {first_name} {Last_name} and im {age} years old')

quote = "To be or not to be, that is the question"
print(quote.upper())

word = "Python"
print(word[0:3])
print(word[3:6])
print(word[::-1])

sentence = "I love programming in Python"
print(sentence.replace("Python", "JavaScript"))

text = "The quick brown fox jumps over the lazy dog"
if "fox" in text:
  print("True")
else: print("False")
if "cat" in text:
  print("True")
else : print("False")

animals = ["cat", "dog", "rabbit", "hamster"]
(first_animal, second_animal, third_animal, fourth_animal) = animals
print(first_animal, second_animal, third_animal, fourth_animal)
print(len(animals))

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(fruits.count('apple'))

colors = ['red', 'blue', 'green', 'yellow', 'blue']
color_index = colors.index("blue")
print(color_index)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
for x in list2:
  list1.append(x)
print(list1)

def remove_all(lst, value):
  return [item for item in lst if item != value]
numbers = [1, 2, 2, 3, 4, 2]
numbers = remove_all(numbers, 2)
print(numbers)


def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        # Flag to detect any swap, if no swap is made, the list is sorted
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if numbers[j] > numbers[j + 1]:
                # Swap if elements are out of order
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        # If no swaps were made in the inner loop, the list is sorted
        if not swapped:
            break
    return numbers

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print("Sorted list:", sorted_numbers)


#tuple_1
my_tuple = (1, 2, 3)
print(type(my_tuple), my_tuple)
print(my_tuple[1])
my_tuple = (1, 2, 3, 4)
print(my_tuple)
#tuple_2
person = ("yuval", 24, "kiryat ono")
(name, age, city) = person
print(name)
print(age)
print(city)
#tuple_3
nested_tuple = ((1,2,3), (4,5,6))
second_tuple = nested_tuple[1]
print(second_tuple[1])

#tuple_4
numbers = (1, 2, 3, 2, 4, 2)
countedNum = numbers.count(2)
print(countedNum)
hamburger = numbers.index(3)
print(hamburger)

#dict_1
student = {"name": "yuval", "age": "24", "grade": "c"}
print(student["name"])
student["school"] = "ben-zvi"
print(student)

#dict_2
student["age"] = "25"
student["grade"] = "amazing"
print(student)
if "grade" in student:
  print('Grade exist')
else:
  print('Does not exist')

#dict_3
capitals = {'France': 'Paris', 'Spain': 'Madrid', 'Japan': 'Tokyo'}
for i in capitals.values():
  print(i)



#dict_4
print(student.values())
print(student.keys())
grade = student.get("grade")
print(grade)
school = student.get("school")
print(school)

#dict_5
def count_number(text):
  number_count = {}
  for char in text:
    if char in number_count:
      number_count[char] += 1
    else:
      number_count[char] = 1
  return number_count
text = "hello"
result = count_number(text)
print(result)

#sets_1
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
# my_set.add(3)
my_set.remove(2) #return 
print(my_set)

#sets_2
set_a = {1, 2, 3, 4}
set_b = {1, 5, 6, 7, 8}
union_set = set_a.union(set_b)
print(union_set) #return a union set 

intersection_set = set_a.intersection(set_b)
print(intersection_set) #returns a new set with elements common to both sets.
difference_set = set_a.difference(set_b)
print(difference_set) #returns the numbers that arent match
symmetric_diff = set_a.symmetric_difference(set_b)
print(symmetric_diff) #return a new set with elements that are in either of the sets, but not in both

#sets_3
numbers = [1, 2, 2, 3, 4, 4, 5]
new_numbers = set(numbers)
print(new_numbers)

#sets_4
if 3 in set_a:
  print('3 is in set_a')
else:
  print("3 is not in set_a")  

if 6 not in set_b:
    print('6 is not in set_b')
else:
    print('6 is in set_b')
print("lololololololololo")
#sets_5
last_set = {1, 2, 3, 4, 5}
last_set.add(6)
print(last_set)
last_set.remove(6)
print(last_set)
last_set.discard(2)
print(last_set) #discard won’t cause an error if the element isn’t present, whereas remove will
# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

students = ['darnell', 'derek', 'devin', 'denise', 'drew']
print(students[1:2])
print(students[4:])

# Exercise 2
# Create a tuple named foodscontaining the same number of foods (strings) as there are names in the studentslist.
# Use a forloop to print out the string "food goes here is a good food".

foods = ('carrot', 'cabbage', 'crab', 'chicken', 'cheese', 'cracker')
for food in foods:
    print(f'{food} is a good food 😘👌')

# Exercise 3
# Using a forloop, print just the last two food strings from foods.
  
for idx, food in enumerate(foods):
    if idx > 3:
    	print(f"{idx}: {food}")

# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"

home_town = {
	'city': 'Carnation',
	'state': 'WA',
	'pop': 2167
}
print(f"I grew up in {home_town['city']}, {home_town['state']} - population: {home_town['pop']}")

# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
"city = Arcadia"
"state = California"
"population = 58000"

for key, value in home_town.items():
    print(f'{key} = {value}')

 
# Exercise 6
# Create an empty list named cohort.
# Using a forloop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:

# {
# 	'student': 'Tina',
# 	'fav_food': 'Cheeseburger'
# }

cohort = []
for idx, student in enumerate(students):
    cohort.extend([{'student': student, 'fav_food': foods[idx]}])
    
print(cohort)

# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.

awesome_students = [student + ' is awesome!' for student in students]
print(awesome_students)

# Exercise 8
# Using the tuple foods and list comprehension within a forloop, print each food string that contains the letter a.

foods_a = [f for f in foods if 'a' in f]
print(foods_a)
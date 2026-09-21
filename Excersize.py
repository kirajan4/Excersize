print("this is my first sample code")

# Excercise1
# Create and Access : Create a dictionary with the following keys: name, age, city. Print each value.
person = {"name": "Ravi", "age": 25, "city": "Chennai"}
print(person)

# Excercise2
# Add new key : Add a key grade with value "A".
student = {"name": "Anu", "marks": 85}
student.update({"grade":"A"})
print(student)

# Excercise3
# update value : Change the marks in the dictionary below to 90.
student = {"name": "Anu", "marks": 85}
student.update({"marks":"90"})
print(student)

# Excercise4
# Delete key : Remove the key age from the dictionary:
person = {"name": "Ravi", "age": 25, "city": "Chennai"}
person.pop("age")
print(person)

# Excercise5
# Loop through dictionary : Print each fruit and its price in this format:
fruits = {"apple": 100, "banana": 40, "orange": 60}
for x,y in fruits.items():
    print(x,"costs",y)

# Excercise6
# Count Frequency : Write a program to count the frequency of each character in a string.
frequency = {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}

# Excercise7
# Check key exists : Write a program to check if a key "math" exists in:
subjects = {"science": 80, "english": 75}

if "math" in subjects:
    print("yes")
else:
    print("No")

# Excercise8
# Merge Two dictionaries : Merge them into one dictionary.
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d1.update(d2)
d2.update(d1)
d3 = d1 | d2
print(d1)
print(d2)
print(d3)

# Excercise9
# Find Max Value : Find the name of the student with the highest score.
scores = {"Arun": 78, "Bala": 92, "Charan": 85}
if x in scores.values():
    


# Excercise10
# Create a dictionary with numbers from 1 to 5 as keys and their squares as values.
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



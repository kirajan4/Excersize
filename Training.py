#Variables
a = "5"
b = "1.5"
c = "Testing"

#Printing Variables
print("{} {} {}".format( "value is ", a, "today"))
print(type(a))

#Printing List
value1 = [1, 2, "Raja", 4, 5]
print(value1[0])
print(value1[-1])
print(value1[1:3])

#Insert
value1.insert(2, "Ravi")
print(value1[2])

#Append
value1.append("end")
print(value1[-1])

#Delete index
value1.pop(0)
print(value1[0])

#Tuples (unchange values, it will be locked once it is created)
value2 = (1, 2, "Raja", 4, 5)
#value2[2] = "Ravi"
print(value2[2])

#Dictionary (changeable values and it has key and pair)
dictionary = {"name": "Ravi", "age": 25, "city": "Chennai"}
print(dictionary["name"])
print(dictionary["age"])
print(dictionary["city"])
print(dictionary.get("name"))
dictionary["age"] = 26
print(dictionary["age"])

# If condition
Day = "Sunday"
Year = 2026

if Day == "Sunday":
    print("Today is Sunday")
else:
    print("Today is not Sunday")

if Year == 2025:
    print("Year is 2025")
else:
    print("Year is:" + str(Year))



numbers = [1, 2, 3, 4, 5]
for x in numbers:
    print(x + 1)

for x in range(5):
    print(x)

# Create first 5digit natural numbers and print them in reverse order.)

Total = 0
for x in range(1, 6, 2):
#    Total += x
    Total = Total + x
print(Total)

#while loop
i = 0
while i <= 5:
    print(i)
    i += 1

Password = ""

while Password != "Ravi":
    Password = input("Enter the password:")
print("Password is correct")    
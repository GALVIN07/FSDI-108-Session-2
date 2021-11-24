

# dictionary

about_me = {
    "name": "Gary",
    "last": "Galvin",
    "age": 33,
    "hobbies": [],
    "address": {
        "street": "2717 thisway",
        "city": "Springfield"
    }
}

print(f"{about_me['name']} {about_me['last']}")


address = about_me["address"]
print(address["street"])
print(address["city"])


#  modify
about_me["age"] = 34

about_me["phone"] = "123 123 1234"

print(about_me)




#  List
print("-" * 40)

names = []
names.append("Gary")
names.append("Oscar")
names.append("Angel")
names.append("Kvon")
names.append("Sergio")

print(names)

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])


#  for loop to travel a list
print("using loops " * 4)
for name in names:
    print(name)


nums = [1,2,3,4,5,6,7,5,4,4,7,2,54,6,2,768,89,345,5467,908,2,4,78,678,123,435]


#  exe 1: print all numbers

for numbers in nums:
    if nums != 4:
        print(numbers)


count=0
for num in nums:
    if num == 4:
        count = count +1
print(count)
    
Sum = sum(nums)
print(Sum)

sum = 0

for num in nums:
    sum = sum + num

print(sum)

students = [ 
    {
        "name": "Kvon",
        "age": 36
    },
   {
        "name": "Gary",
        "age": 37
    },
    {
        "name": "Oscar",
        "age": 33
    },
    {
        "name": "Angel",
        "age": 35
    },
]

ages=0

for student in students:
    age = student["age"]
    ages += age

print(ages)






    
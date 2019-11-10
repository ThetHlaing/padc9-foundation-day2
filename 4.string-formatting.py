## % formating

name = "Aung Aung"
age = 28

# print("Hello, %s." % name)

# print("Hello, %s. You are %s." % (name, age))

## str.format()

# print("Hello, {}. You are {}.".format(name, age))

# print("Hello, {0}. You are {1}.".format(age, name))

# print("Hello, {name}. You are {age}.".format(name='Aye Aye', age=age))

person = { 'name' : name , 'age' : age, 'job' : 'cleaner'}

# print("Hello, {name}. You are {age}".format(**person))


# Formatted String Literal

print(f"Hello, {name}. You are {age}")

print(F"Hello, {name}. You are {age}")

print(F"Hello, {person.get('name')}. You are {age-5}")

print(
    f"Hello, {name}."
    f"You are {age}"
)

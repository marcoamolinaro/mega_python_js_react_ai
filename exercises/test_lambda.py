def greet_person(name):
    return "Hello, " + name

greet = lambda name: "Hi, " + name

print(greet_person("John"))
print(greet("Bob"))

is_adult = lambda age: age >= 18

print(is_adult(17))
print(is_adult(36))
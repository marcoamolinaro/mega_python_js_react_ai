from functions import is_adult

age = int(input("Please enter your age: "))

while not is_adult(age):
    print("Sorry, you are not old enough! Next person please!")
    age = int(input("Please enter your age: "))
    
print("Welcome to the club!")

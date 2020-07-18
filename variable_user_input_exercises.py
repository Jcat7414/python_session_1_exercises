print("Q1")

first_number = input("Enter number 3: ")
second_number = input("Enter number 9: ")

result = int(first_number) + int(second_number)
print(result)

print("")

first_int = input("Enter number -3: ")
second_int = input("Enter number 9: ")

result = int(first_int) + int(second_int)
print(result)

print("")

first_float = input("Enter number 3.0: ")
second_float = input("Enter number -9: ")

result = float(first_float) + float(second_float)
print(result)

print("")

print("Q2")

first_number = input("Enter number 3: ")
second_number = input("Enter number 9: ")

result = int(first_number) * int(second_number)
print(f"{first_number} * {second_number} = {result}")

print("")

first_int = input("Enter number -3: ")
second_int = input("Enter number 9: ")

result = int(first_int) * int(second_int)
print(f"{first_int} * {second_int} = {result}")

print("")

first_float = input("Enter number 3.0: ")
second_float = input("Enter number -9: ")

result = float(first_float) * float(second_float)
print(f"{first_float} * {second_float} = {result}")

print("")

print("Q3")

print("Convert kilometers to meters and centimeters")
distance_km = input("Enter kilometers number 10: ")

result_m = int(distance_km) * 1000
result_cm = int(distance_km) * 100000
print(f"{distance_km}km = {result_m}m")
print(f"{distance_km}km = {result_cm}cm")

print("")

distance_km = input("Enter kilometers number 5.4: ")

result_m = float(distance_km) * 1000
result_cm = int(result_m) * 100

print(f"{distance_km}km = {int(result_m)}m")
print(f"{distance_km}km = {result_cm}cm")

print("")

print("Q4")

name = input("What is your name? ")
height_cm = input("How tall are you in centimeters? ")

print(f"{name} is {height_cm}cms tall.")

print("")

dogs_name = input("What is your dog's name? ")
dog_height_cm = input("How tall is your dog in centimeters? ")

print(f"{dogs_name} is {dog_height_cm}cms tall.")
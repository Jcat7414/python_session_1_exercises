print("Q1")

print("Is it time for Roary to catch moths?")

moths_in_house = input("Are there any moths in the house? (Y/N) ")

if moths_in_house == "Y":
    print("Get the moths!")

if moths_in_house == "N":
    print("No threats detected.")

print("")

print("Q2")

print("Is it time for Roary to go moth hunting?")

moths_in_house = input("Are there any moths in the house? (Y/N) ")
# print(moths_in_house)

mitch_is_home = input("Is Mitch at home? (Y/N) ")
# print(mitch_is_home)

if moths_in_house == "Y" and mitch_is_home == "Y":
    print("Hooman! Help me get the moths!")

if moths_in_house == "N" and mitch_is_home == "N":
    print("No threats detected.")

if moths_in_house == "Y" and mitch_is_home == "N":
    print("Meooooooow! Hissssss!")

if moths_in_house == "N" and mitch_is_home == "Y":
    print("Climb on Mitch.")

print("")

print("Q3")

print("What action, if any, will the Red Light Camera take?")

light_colour = input("What colour is the light? Enter Red (R), Amber (A) or Green (G): ")
# print(light_colour)
car_detected = input("Is there a vehicle detected? Enter Yes (Y) or No (N): ")
# print(car_detected)

if light_colour == "R" and car_detected == "N":
    print("Do nothing.")

if light_colour == "R" and car_detected == "Y":
    print("Flash!")

if light_colour == "G" and car_detected == "N":
    print("Do nothing.")

if light_colour == "G" and car_detected == "Y":
    print("Do nothing.")

if light_colour == "A" and car_detected == "N":
    print("Do nothing.")

if light_colour == "A" and car_detected == "Y":
    print("Do nothing.")

print("")

print("Q4")

print("Find out if you are tall enough to ride the rollercoaster!")

height_cm = input("Enter your height in centimeters: ")

result = int(height_cm)

if result >= 120:
    print("Hop on!")
elif result<120:
    print("Sorry, not today :(")
else:
    print("Hop on!")
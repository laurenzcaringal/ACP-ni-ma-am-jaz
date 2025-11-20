# 1. Food list
food = ["Carbonara", "Caldereta", "Spaghetti", "Pansit", "Beef Steak"]

addFood = input("Enter food to add: ")
food.append(addFood)
print(food)

removeFood = input("Enter food to remove: ")
food.remove(removeFood)
print(food)

# 2. Tuple of cars
cars = ("Honda", "Mitsubishi", "Nissan", "Ford", "Suzuki")
print(cars)
print("2nd car:", cars[1])
print("last car:", cars[-1])
print(cars)

# 3. Sets of hobbies
physicalHobbies = {"Walking", "Weight Lifting", "Running", "Playing Basketball", "Playing Badminton"}
mentalHobbies = {"Reading books", "Singing", "Listening to Music", "Playing Online Games", "Watching Documentary"}

print("\nSet A:", physicalHobbies)
print("Set B:", mentalHobbies, "\n")

print("Union:", physicalHobbies | mentalHobbies)
print("Difference:", physicalHobbies - mentalHobbies)
print("Intersection:", physicalHobbies & mentalHobbies)

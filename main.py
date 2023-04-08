from GymnastInfo import GymnastInfo,Trainer_Info
from Gymnasium import Gymnasium
from Exercise import Exercise,Meal,Running,Cycling,Pushups,Yoga,Lunges,BMI



breakfast = Meal('Protein powders and egg whites', 300)
print(breakfast)

my_bmi=BMI(40,5.6)
print(my_bmi.calculate_bmi())
print(my_bmi.get_bmi())
print(my_bmi.get_bmi_category())

"""
# create some exercises
running_exercise = Running("Morning run", 30, 5)
cycling_exercise = Cycling("Indoor cycling", 45, 8)
pushups_exercise = Pushups("Pushups", 20, 3)
yoga_exercise = Yoga("Yoga", 30, 5)
lunges_exercise = Lunges("Lunges", 20, 3)



# create some meals
breakfast = Meal('Protein powders and egg whites', 300)
lunch = Meal("Brown rice, quinoa, yams, potatoes, oats", 450)
dinner = Meal("Tropical fruits, berries, green/fibrous vegetables, beans", 600)



# create a gymnasium
gym = Gymnasium("Gold Standard Gym", "University Town",running_exercise)

# create a trainer
trainer = Trainer_Info("Usama Naeem", 28, 70, 1.75, "male", "ACE")
trainer.add_exercise(running_exercise)
trainer.add_exercise(cycling_exercise)
trainer.add_exercise(pushups_exercise)
trainer.add_exercise(yoga_exercise)
trainer.add_exercise(lunges_exercise)
for exercise in trainer.exercise:
    print(exercise)

print(trainer.Display())

# create a gymnast


gymnast = GymnastInfo("Hamza Ejaz", 25, 60, 1.65, "Male")
gymnast.set_name("Hamza Ejaz")
gymnast.set_age(26)
gymnast.set_weight(62)
gymnast.set_height(5.8)
gymnast.set_gender('Male')
print(len(gymnast.total_gymnasts))


# print some information

print(gym.Display())
print(f'{gymnast.get_name()} eat {breakfast} in breakfast')
print(f'{gymnast.get_name()} goes to {gym.get_name_of_gymnasium()} and his trainer is {trainer.get_name()}')
print(f'{trainer.get_name()}is certified of {trainer.get_certification()}')
print(trainer.Display())
print(gymnast.Display())
print(f"{gymnast.get_name()} has burned {running_exercise.calories_burned()} calories with {running_exercise.get_name_of_exercise()}")

"""


"""
# Create an exercise
running = Exercise("Morning run", 30)

# Create a gymnasium
gym = Gymnasium("Gold Standard Gym", "University Town", running)

# Display information about the gymnasium
print(gym.Display())
"""


"""
# Create some exercises
running = Running("Morning run", 30, 5)
cycling = Cycling("Afternoon bike ride", 45, 8)

# Print information about the exercises
print(running)
print(cycling)

# Calculate and print calories burned during the exercises
print(f"{running.get_name_of_exercise()} burned {running.calories_burned()} calories.")
print(f"{cycling.get_name_of_exercise()} burned {cycling.calories_burned()} calories.")

# Create some meals
breakfast = Meal("Oatmeal", 350)
lunch = Meal("Grilled chicken salad", 450)

# Print information about the meals
print(breakfast)
print(lunch)

# Calculate and print total calories consumed during the meals
total_calories = breakfast.calories + lunch.calories
print(f"Total calories consumed: {total_calories}")

"""
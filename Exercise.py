class Exercise:
    exercise=[]
    def __init__(self,name_of_exercise: str,time_duration_of_exercise:float,):
        assert time_duration_of_exercise >= 0, "Time duration cannot be negative!"
        self.name_of_exercise=name_of_exercise
        self.time_duration_of_exercise=time_duration_of_exercise
    def set_name_of_exercise(self,name_of_exercise):
        self.name_of_exercise=name_of_exercise
    def set_time_duration_of_exercise(self,time_duration_of_exercise):
        self.time_duration_of_exercise=time_duration_of_exercise
    def get_name_of_exercise(self):
        return self.name_of_exercise
    def get_time_duration_of_exercise(self):
        return self._time_duration_of_exercise
    def Display(self):
        return f"{self.name_of_exercise} takes {self.time_duration_of_exercise} minutes to complete"

class Pushups(Exercise):
    def __init__(self, name_of_exercise, time_duration_of_exercise, sets):
        super().__init__(name_of_exercise, time_duration_of_exercise)
        self.sets = sets

    def __str__(self):
        return f'{self.name_of_exercise} takes {self.time_duration_of_exercise} minutes to complete - {self.sets} sets'

    def calories_burned(self):
        return int(self.time_duration_of_exercise * (self.sets / 5) * 5)

class Running(Exercise):
    def __init__(self, name_of_exercise, time_duration_of_exercise, distance):
        super().__init__(name_of_exercise, time_duration_of_exercise,)
        self.distance = distance

    def __str__(self):
        return f'{self.name_of_exercise} takes {self.time_duration_of_exercise} minutes to complete - {self.distance} Kilometer'

    def calories_burned(self):
        return int(self.time_duration_of_exercise* (self.distance / 10) * 8)

class Cycling(Exercise):
    def __init__(self, name_of_exercise, time_duration_of_exercise, resistance):
        super().__init__(name_of_exercise, time_duration_of_exercise)
        self.resistance = resistance

    def __str__(self):
        return f'{self.name_of_exercise} takes {self.time_duration_of_exercise} minutes to complete - Resistance: {self.resistance}'

    def calories_burned(self):
        return int(self.time_duration_of_exercise * (self.resistance / 5) * 10)
class Yoga(Exercise):
    def __init__(self, name_of_exercise, time_duration_of_exercise, difficulty):
        super().__init__(name_of_exercise, time_duration_of_exercise)
        self.difficulty = difficulty

    def __str__(self):
        return f'{self.name_of_exercise} takes {self.time_duration_of_exercise} minutes to complete - Difficulty: {self.difficulty}'

    def calories_burned(self):
        return int(self.time_duration_of_exercise * (self.difficulty / 5) * 5)
class Lunges(Exercise):
    def __init__(self, name_of_exercise, time_duration_of_exercise, sets):
        super().__init__(name_of_exercise, time_duration_of_exercise)
        self.sets = sets

    def __str__(self):
        return f'{self.name_of_exercise} takes {self.time_duration_of_exercise} minutes to complete - {self.sets} sets'

    def calories_burned(self):
        return int(self.time_duration_of_exercise * (self.sets / 5) * 5)


class Meal:
    meal=[]
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __str__(self):
        return f'{self.name} - {self.calories} calories'
class BMI:
    def __init__(self,weight: float,height: float):
        self.weight=weight
        self.height=height
    def calculate_bmi(self):
        return (self.weight / self.height**2)
    def get_bmi(self):
        return self.calculate_bmi()
    def get_bmi_category(self):
        if self.get_bmi() < 18.5:
            return "Underweight"
        elif self.get_bmi() >= 18.5 and self.get_bmi() < 25:
            return "Normal"
        elif self.get_bmi() >= 25 and self.get_bmi() < 30:
            return "Overweight"
        elif self.get_bmi() >= 30:
            return "Obese"
    def __str__(self):
        return f"{self.get_bmi_category()}"
from Exercise import Exercise,Meal
class GymnastInfo:
    total_gymnasts = []
    exercise=[]
    meal=[]
    def __init__(self, name: str,age: int, weight: float, height: float,gender: str):
        assert age >= 0, "Age cannot be negative!"
        assert weight >= 0, "Weight cannot be negative!"
        assert height >= 0, "Height cannot be negative!"
        self.name = name
        self.age=age
        self.weight=weight
        self.height=height
        self.gender=gender
        GymnastInfo.total_gymnasts.append(self)
        Exercise.exercise.append(self)
        Meal.meal.append(self)
    def set_name(self,name):
        self._name =name   #private variable
    def set_age(self,age):
        self._age=age    #private variable
    def set_weight(self,weight):
        self._weight=weight    #private variable
    def set_height(self,height):
        self._height=height    #private variable
    def set_gender(self,gender):
        self._gender=gender
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_weight(self):
        return self._weight
    def get_height(self):
        return self._height
    def get_gender(self):
        return self._gender
    def Display (self):
        return f"{self.name} weight is {self.weight} kg,his age is {self.age} years,his height is {self.height} cm and gender of {self.name} is {self.gender}"
    def add_exercise(self,exercise):
        self.exercise.append(exercise)
    def add_meal(self,meal):
        self.meal.append(meal)

class Trainer_Info(GymnastInfo):
    exercise=[]
    def __init__(self,name: str,age: int,weight: float,height: float,gender: str,certification: str):
        super().__init__(name,age,weight,height,gender)
        self.certification=certification
        Exercise.exercise.append(self)
    def get_name(self):
        return self.name
    def get_certification(self):
        return self.certification
    def Display(self):
        return f"{self.name} is a {self.certification} certified trainer"

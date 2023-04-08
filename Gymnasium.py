from Exercise import Exercise
class Gymnasium:

    def __init__(self,name_of_gymnasium: str,location_of_gymnasium: str,exercise: Exercise):
        self.name_of_gymnasium=name_of_gymnasium
        self.location_of_gymnasium=location_of_gymnasium
        self.exercise=exercise
    def set_name_of_gymnasium(self,name_of_gymnasium):
        self.name_of_gymnasium=name_of_gymnasium
    def set_location_of_gymnasium(self,location_of_gymnasium):
        self.location_of_gymnasium=location_of_gymnasium
    def get_name_of_gymnasium(self):
        return self.name_of_gymnasium
    def get_location_of_gymnasium(self):
        return self.location_of_gymnasium
    def Display (self):
        return f"{self.name_of_gymnasium} is located in {self.location_of_gymnasium} and it offers {self.exercise}"
    def add_exercise(self,exercise):
        self.exercise.append(exercise)

# Path: project\GymnastInfo.py


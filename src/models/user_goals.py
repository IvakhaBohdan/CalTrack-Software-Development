class User:
    def __init__(self, name, age, gender, height, weight, activityLevel, goal="maintain"):
        self.name = name
        self.age = age          # вік
        self.gender = gender    # стать
        self.height = height    # зріст у см
        self.weight = weight    # вага у кг
        self.activityLevel = activityLevel # рівень активності 
        self.goal = goal        # ціль 
        self.daily_calories_target = 0 
        self.meal_history = []
        self.activity_history = []

if __name__ == '__main__':
    user1 = User("Богдан", 25, "Male", 178, 80, "moderate", "loss")
    print(f"Користувач {user1.name}, вага: {user1.weight} кг")
class Product:
    def __init__(self, name: str, calories: float, proteins: float, fats: float, carbs: float):
        self.name = name
        self.calories = calories
        self.proteins = proteins
        self.fats = fats
        self.carbs = carbs

    def get_nutrients(self):
        return {
            'calories': self.calories,
            'proteins': self.proteins,
            'fats': self.fats,
            'carbs': self.carbs
        }
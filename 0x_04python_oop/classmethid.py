
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def veg(cls):
        return cls(["tomato", "onion", "cheese"])

    @classmethod
    def margherita(cls):
        return cls(["tomato", "basil", "cheese"])

# Create instances of the Pizza class
pizza_1 = Pizza.veg()
pizza_2 = Pizza.margherita()

print(pizza_1.ingredients) 
print(pizza_2.ingredients) 





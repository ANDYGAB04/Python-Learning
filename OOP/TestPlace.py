# OOP
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    # Constructor
    def __init__(self, name="anonymous", age=0):
        self.name = name
        self.age = age

    # Methods
    def shout(self):
        print(f"My name is {self.name}")

    # Class Method
    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    # Static Method
    @staticmethod
    def add(num1, num2):
        return num1 + num2


player1 = PlayerCharacter.adding_things(2, 3)


print(player1.age)

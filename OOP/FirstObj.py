# OOP
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    # Constructor
    def __init__(self, name="anonymous", age=0):
        if age > 18:
            self.name = name
            self.age = age

    # Methods
    def shout(self):
        print(f"My name is {self.name}")


player1 = PlayerCharacter("John", 20)
player2 = PlayerCharacter("Tom", 21)

print(player1.shout())
print(player2.shout())

class User:
    def sign_in(self):
        print("login-in")

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def attack(self):
        print(f"attacking with power of {self._power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self._num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows {self._num_arrows}")


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)

for char in [wizard1, archer1]:
    char.attack()

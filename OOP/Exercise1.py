# Given the below class:
class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Luna", 5)
cat2 = Cat("Milo", 6)
cat3 = Cat("Oliver", 7)


# 2 Create a function that finds the oldest cat
def oldest_cat(cat1, cat2, cat3):
    if cat1.age > cat2.age and cat1.age > cat3.age:
        return cat1
    elif cat2.age > cat3.age and cat2.age > cat1.age:
        return cat2
    else:
        return cat3


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldcat = oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldcat.age} years old.")

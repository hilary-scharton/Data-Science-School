# using the lion class template, expand the class to have features specific to a lion
# add a field for lion type
# add a method in this class which sets the lion type based on its weight (derived from superclass)
# if weight < 80kg, type should be cub.  if < 120 kg, should be female.  if > 120 kg, is male
# print out the type of lion
# compile, save, run


class Animal(object):
    """animal class docstring"""

    def __init__(self, numteeth, spots, weight):
        self.numteeth = numteeth
        self.spots = spots
        self.weight = weight


class Lion(Animal):
    def __init__(self, numteeth, spots, weight):
        super().__init__(numteeth, spots, weight)

    def lion_type(self):
        if self.weight < 80:
            lion_type = 'cub'
        elif self.weight < 120:
            lion_type = 'female'
        elif self.weight >= 120:
            lion_type = 'male'
        return lion_type


this_animal = Lion(2, 4, 10)
print(this_animal.lion_type())

# create a class called cheetah that inherits from the animal class, contains a constructor, has an array as a field
# create a cheetah object and print it out


class Cheetah(Animal):
    """cheetah docstring explaining what it does"""
    def __init__(self, numteeth, spots, weight, name, age):
        super().__init__(numteeth, spots, weight)
        self.name = name
        self.age = age
        self.spots = True

list = []

list.append(Cheetah(24, True, 100, 'Sally', 5))
list.append(Cheetah(24, True, 75, 'Peter', 4))
list.append(Cheetah(24, True, 150, 'Tigger', 3))
list.append(Cheetah(24, True, 100, 'Daisy', 2))

for obj in list:
    print(obj.name, "is", obj.age, "years old")

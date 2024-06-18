class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "woof!"
    
class Cat(Animal):
    def speak(self):
        return "meow!"
git 
# Function to make any animal speak    
def animal_sound(animal):
    print(animal.speak())

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Using polymorphismto call the speak method
animal_sound(dog)
animal_sound(cat)
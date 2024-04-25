class Dog:
    def __init__(self, breed, age, color):
        self.breed = breed
        self.age = age
        self.color = color
def introduce(self):
        print ("Hi")
        print("I am a " + self.breed + " dog.")
        print ("I am "  + str(self.age) + " years old") 
        print ("I am "  + self.color + " in color")
dog = Dog('bhutanese', 20, 'black')
petdog = Dog('pug', 10, 'white')
my_friend_dog = Dog('german shephard', 15, 'brown')
dog.introduce()
petdog.introduce()

dog.say_age()
petdog.say_age()
my_friend_dog.say_age()
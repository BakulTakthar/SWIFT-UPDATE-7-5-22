class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"{self.name}i am talking")


person = Person("JOSHUA")
print(person.name)
print(person.talk)
bob = Person("BOBDE")
bob.talk()

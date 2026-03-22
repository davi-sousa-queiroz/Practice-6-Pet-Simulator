class Pet:
    def __init__(self, name="Clarisse", age=2, hunger=5):
        self.name = name
        self.age = age
        self.hunger = hunger

    def eat(self):
        print(f"\n{self.name} ate!")
        print("-2 hunger!")
        self.hunger -= 2

    def play(self):
        print(f"\n{self.name} played!")
        print("+2 hunger..")
        self.hunger += 2

    def info(self):
        print(f"\nPet name: {self.name}\nPet age: {self.age}\nPet hunger: {self.hunger}")

def menu():
    print("\n1.\tPlay\n2.\tEat\n3.\tShow Stats\n4.\tQuit")

mypet = Pet("Clarisse", 2, 5)
while True:
    menu()
    selection = int(input("\n>>"))
    if selection == 1:
        mypet.play()
    elif selection == 2:
        mypet.eat()
    elif selection == 3:
        mypet.info()
    elif selection == 4:
        print("\nThank you for playing pet sim! 🐶❤️")
        break
    else:
        print("\nEnter a valid input.")




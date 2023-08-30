class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} makes a {self.sound} sound.")


class Dog(Animal):
    def __init__(self, name):
        super().__init__("dog", "bark")
        self.name = name

    def wag_tail(self):
        print(f"{self.name} wags its tail.")


class Cat(Animal):
    def __init__(self, name):
        super().__init__("cat", "meow")
        self.name = name

    def purr(self):
        print(f"{self.name} purrs softly.")


def main():
    fido = Dog("Fido")
    whiskers = Cat("Whiskers")

    fido.make_sound()
    fido.wag_tail()

    whiskers.make_sound()
    whiskers.purr()


if __name__ == "__main__":
    main()

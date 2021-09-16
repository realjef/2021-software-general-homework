class Fish:
    def __init__(self, name, color, species):
        self.name = name
        self.color = color
        self.species = species
        self.alive = True

    def death(self):
        self.alive = False

    def __repr__(self):
        if self.alive:
            eye = "o"
        else:
            eye = "*"
        return f"><((({eye}>"

    def eat(self, fish):
        print(f"yum, I ate {fish.name}!")
        fish.death()
class HulkFish(Fish):
    def __init__(self, name, color, species):
        super().__init__(name, color, species)
        self.lives = 10

    def death(self):
        self.lives -= 1
        if self.lives == 0:
            self.alive = False

if __name__ == "__main__":
    pet = Fish("Jonny", "Rainbow", "Double Stuf Oreo")
    print(pet)
    print(pet)

    print()

    mega_fish = HulkFish("Hulkman", "rainbow", "swordfish")
    print(mega_fish.name)
    print(mega_fish)

    mega_fish.eat(pet)
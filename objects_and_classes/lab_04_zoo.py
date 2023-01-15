class Zoo:
    __animals__ = 0

    def __init__(self, name):
        self.name = name
        self.mammals = list()
        self.fish = list()
        self.birds = list()

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        needed_list = list()
        animal_type = ""
        if species == "mammal":
            needed_list = self.mammals
            animal_type = species[0].upper() + species[1:] + "s"
        elif species == "fish":
            needed_list = self.fish
            animal_type = species[0].upper() + species[1:] + "es"
        elif species == "bird":
            needed_list = self.birds
            animal_type = species[0].upper() + species[1:] + "s"

        print(f"{animal_type} in {self.name}: {', '.join(needed_list)}")
        print(f"Total animals: {Zoo.__animals__}")


zoo_name = Zoo(input())
Zoo.__animals__ = int(input())


for animal in range(Zoo.__animals__):
    data = input().split()
    zoo_name.add_animal(data[0], data[1])

desired_group = input()

zoo_name.get_info(desired_group)

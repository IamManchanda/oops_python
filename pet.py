class Pet:
    allowed_species = ["cat", "dog", "fish", "rat"]
    def __init__(self, name, species):
        if species.lower() not in Pet.allowed_species:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species
    def set_species(self, species):
        if species.lower() not in Pet.allowed_species:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species

cat = Pet("Blue", "Cat")
cat = Pet("Wyatt", "Dog")

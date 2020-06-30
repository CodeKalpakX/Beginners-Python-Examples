class Animal:
    def __init__(self, species, name, legs, color, voices):
        self.species = species
        self.name = name
        self.legs = legs
        self.color = color
        self.voices = voices

cat = Animal("Cat" , "Pussy-Cat" ,  4 ,  "white" , "meow")
dog = Animal("Dog" , "Cloudy",  4 , "brownie" , "bark")

print("Species of animal : ",dog.species)
print("name of animal : ",dog.name)
print("no. of legs       : ",dog.legs)
print("color of animal : ",dog.color)
print("voice of animal : ",dog.voices)
print("  ")
print("Species of animal : ",cat.species)
print("name of animal : ",cat.name)
print("no. of legs        : ",cat.legs)
print("color of animal : ",cat.color)
print("voice of animal : ",cat.voices)

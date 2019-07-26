from modules.Animals import Dog, Cat, Lion

keegLion = Lion('Keegan','Silver','Extra Large',33)
darDog = Dog('Daryn','Milky White','Scrawny',34)
randCat = Cat()

randCat.setRandom()

print(keegLion.getDescription())
print(darDog.getDescription())
print(randCat.getDescription())

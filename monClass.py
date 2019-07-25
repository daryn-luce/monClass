from modules.Animals import Dog, Cat, Lion

keegLion = Lion('Keegan','Silver','Extra Large',33)
darLion = Lion('Daryn','Milky White','Scrawny',34)
randLion = Lion()

randLion.setRandom()

print(keegLion.getDescription())
print(darLion.getDescription())
print(randLion.getDescription())
from random import randint

class Dog:
    def __init__(self,name=None,color=None,size=None,age=None):
        self.__name = name
        self.__color = color
        self.__speak = 'Bark'
        self.__size = size
        self.__age = age
        
    def setName(self,name):
        self.__name = name
        
    def getName(self):
        return self.__name

    def setColor(self,color):
        self.__color = color
        
    def getColor(self):
        return self.__color
    
    def setSize(self,size):
        self.__size = size
        
    def getSize(self):
        return self.__size
        
    def setAge(self,age):
        self.__age = age
        
    def getAge(self):
        return self.__age
        
    def setRandom(self):
        name = ['Bella','Lucy','Daisy','Sadie','Molly','Bailey']
        color = ['Black','Brown','White','Golen','Grey','Spotted',]
        size = ['Tiny','Small','Medium','Big','Very Big']
        self.__name = name[randint(0,len(name)-1)]
        self.__color = color[randint(0,len(color)-1)]
        self.__size = size[randint(0,len(size)-1)]
        self.__age = randint(1,13)
        
    def getAgeGroup(self):
        if self.__age > 2:
            return 'Adult'
        else:
            return 'Puppy'
    
    def getDescription(self):
        return '{} is a {} {} year old {} dog who says {}'.format(self.__name,self.__size,self.__age,self.__color,self.__speak)
    
class Cat:
    def __init__(self,name=None,color=None,size=None,age=None):
        self.__name = name
        self.__color = color
        self.__speak = 'Meow'
        self.__size = size
        self.__age = age
        
    def setName(self,name):
        self.__name = name
        
    def getName(self):
        return self.__name

    def setColor(self,color):
        self.__color = color
        
    def getColor(self):
        return self.__color
    
    def setSize(self,size):
        self.__size = size
        
    def getSize(self):
        return self.__size
        
    def setAge(self,age):
        self.__age = age
        
    def getAge(self):
        return self.__age
        
    def setRandom(self):
        name = ['Teddy','Zeus','Louie','Murphy','Hope','Jasper']
        color = ['Black','Brown','White','Golden','Grey','Calico',]
        size = ['Tiny','Small','Medium','Big','Very Big']
        self.__name = name[randint(0,len(name)-1)]
        self.__color = color[randint(0,len(color)-1)]
        self.__size = size[randint(0,len(size)-1)]
        self.__age = randint(1,18)
        
    def getAgeGroup(self):
        if self.__age > 2:
            return 'Adult'
        else:
            return 'Kitty'
            
    def getDescription(self):
        return '{} is a {} {} year old {} cat who says {}'.format(self.__name,self.__size,self.__age,self.__color,self.__speak)


class Lion:
    def __init__(self,name=None,color=None,size=None,age=None):
        self.__name = name
        self.__color = color
        self.__speak = 'Roar'
        self.__size = size
        self.__age = age
        
    def setName(self,name):
        self.__name = name
        
    def getName(self):
        return self.__name

    def setColor(self,color):
        self.__color = color
        
    def getColor(self):
        return self.__color
    
    def setSize(self,size):
        self.__size = size
        
    def getSize(self):
        return self.__size
        
    def setAge(self,age):
        self.__age = age
        
    def getAge(self):
        return self.__age
        
    def setRandom(self):
        name = ['Mufasa','Scar','Simba','Sarabi','Nala','Sarafina']
        color = ['Brown','Light Brown','Golden','Light Gold','Dark Brown','Dark Gold',]
        size = ['Tiny','Small','Medium','Big','Very Big']
        self.__name = name[randint(0,len(name)-1)]
        self.__color = color[randint(0,len(color)-1)]
        self.__size = size[randint(0,len(size)-1)]
        self.__age = randint(1,8)
        
    def getAgeGroup(self):
        if self.__age > 2:
            return 'Adult'
        else:
            return 'Cub'
            
    def getDescription(self):
        return '{} is a {} {} year old {} lion who says {}'.format(self.__name,self.__size,self.__age,self.__color,self.__speak)

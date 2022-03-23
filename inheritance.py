# parent
from urllib.parse import MAX_CACHE_SIZE


class Animal:
    def __init__(self):
        print("animal is created")

    def toString(self):
        print("animal")

    def walk(self):
        print("animal walk")

# child


class Monkey(Animal):
    def __init__(self):
        super().__init__()  # use init of parent(animal) class
        print("monkey is created")

    def toString(self):
        print("monkey")

    def climb(self):
        print("monkey can climb")


class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("bird is created")

    def fly(self):
        print("fly")
#


class Kuzu(Animal):
    def __init__(self):
        print("Kuzu olusturuldu")

    def toString(self):
        print("Kuzu mee")

    def walk(self):
        print("Kuzu yuruyor")


class Inek(Animal):
    __inek_sayisi = 0  # private
    MAX_OT = 2000

    def __init__(self, name):
        super().__init__()
        self.name = name
        print(f"{self.name} olusturuldu")
        #Inek.inek_sayisi += 1
        Inek.inek_sayisi_arttir()

    def otlan(self):
        print(f"{self.name} otlaniyor")

    def dinlen(self):
        print(f"{self.name} dinleniyor")

    def toString(self):
        print(f"Benim adim {self.name}")

    def sutVer(self, kg):
        print(f"Sut verildi {kg} kg")

    @classmethod
    def inekSayisi(cls):
        print(f"Inek sayisi : {Inek.__inek_sayisi}")

    @classmethod
    def inek_sayisi_arttir(cls):
        Inek.__inek_sayisi += 1


ku1 = Kuzu()
ku1.toString()
ku1.walk()


m1 = Monkey()
m1.toString()
m1.walk()
m1.climb()
print("----")
b1 = Bird()
b1.walk()
# b1.climb()
b1.fly()
print("--------")
i1 = Inek("Sarikiz")
i1.otlan()
i1.dinlen()
i1.walk()  # Animal sinifinin uyesi
i1.sutVer(3)
i1.toString()
Inek.inekSayisi()
print("----------")
i2 = Inek("Holshtein")
i2.otlan()
i2.dinlen()
i2.walk()  # Animal sinifinin uyesi
i2.sutVer(10)
i2.toString()

#Inek.inek_sayisi = 10

Inek.inekSayisi()
#print(f"Inek sayisi {i1.inek_sayisi}")
#print(f"Inek sayisi {i2.inek_sayisi}")
Inek.inek_sayisi_arttir()
Inek.inekSayisi()

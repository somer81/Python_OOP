# integer = 10
# string = "messi" "barcelona football team"
# %%
integer1 = 33
string1 = "messi"

# %% classes

employee1_name = "messi"
employee1_age = 33
employee1_address = "asdasdas"


class Employee:
    # attribute = age, address, name
    # behaviour = pass
    pass


employee1 = Employee()
employee2 = Employee()


# %% attribute

class Footballer:
    football_club = "barcelona"
    age = 30
    name = "Player"


f1 = Footballer()
f2 = Footballer()


print(f1)
print(f1.age)
print(f1.name)
print(f1.football_club)

f1.football_club = "real madrid"

print(f1.football_club)

print(f2.age)
print(f2.football_club)

# %% methods


class Square():
    edge = 5  # meter
    area = 0
    circum = 0

    def area1(self):
        self.area = self.edge * self.edge  # 5*5
        print("Area: ", self.area)

    def circum1(self):
        return 4 * self.edge


###############
s1 = Square()

print(s1)
print(s1.edge)

print(s1.area1())
print("Cevre : ", s1.circum1())

s1.edge = 7
s1.area1()

# %% methods vs funtions


class Emp(object):

    age = 25
    salary = 1000  # $

    def ageSalaryRatio(self):
        a = self.age / self.salary
        print("method: ", a)


e1 = Emp()
e1.ageSalaryRatio()
# ╦ ------------------------------------------------------
# function


def ageSalaryRatio(age, salary):
    a = age / salary
    print("function: ", a)


ageSalaryRatio(30, 3000)

#


def findArea(a, b):  # a = pi,  b = r
    area = a*b**2
    # print(area)
    return area


pi = 3.14
r = 5

result1 = findArea(pi, r)
print(result1)
result2 = findArea(pi, 10)

print(result1 + result2)

# %% initializer or contructor


class Animal():

    def __init__(self, a, b):  # ( name, age) = ("dog", 2) = (a, b)
        self.name = a
        self.age = b

    def getAge(self):
        # print("")
        return str(self.age)

    def getName(self):
        return self.name


a1 = Animal("dog", 2)
a2 = Animal("cat", 4)
a3 = Animal("bird", 6)

print(a1.getName(), " ", a1.getAge())
print(a2.getName(), " ", a2.getAge())
print(a3.getName(), " ", a3.getAge())

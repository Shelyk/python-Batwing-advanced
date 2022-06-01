from random import *
from abc import abstractmethod

class Person:
    def __init__(self, name, age, availability_of_money, having_your_own_home):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.having_your_own_home = having_your_own_home

    @abstractmethod
    def info(self): 
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def make_money(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def buy_house(self, house):    
        raise NotImplementedError('This method was not implemented')

class Human(Person):
    def __init__(self, name, age, availability_of_money, having_your_own_home):
        super().__init__(name, age, availability_of_money, having_your_own_home)

    def info_about_human(self):
        print(f'My name is {self.name}, I am {self.age} years old.')

    def make_money(self):
        make_money = randint(5000, 20000)
        self.availability_of_money += make_money
        print(f'I have {make_money} money on my balance now {self.availability_of_money}')

    def buy_house(self, house):
        if self.availability_of_money >= house.cost:
            print('I can buy this house')
        else:
            print("I don't have enough money for this house")

class House:
    def __init__(self,house_name, area, cost):
        self.house_name = house_name
        self.area = area
        self.cost = cost


    def house_info(self):
        if self.area < 40:
            print('This house is small :(')
        else:
            print(f'{self.house_name} area is {self.area}, price is {self.cost}')

    def discount(self):
        if self.cost >= 10000:
            print('\n', f"Interested house's price is {self.cost}")
            print('\n', 'Applying discount...', '\n')
            self.cost = self.cost - 5999
            print(f"Now house's price is {self.cost}")
        else:
            print('There is no discount at this house')
            pass


class Small_House(House):
    def __init__(self,house_name, area, cost):
        super().__init__(house_name, area, cost)
        if self.area >= 40:
            self.__class__ = House

class Realtor_Meta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

                
class Realtor(metaclass=Realtor_Meta):    
    def __init__(self, name, houses):
        self.name = name
        self.houses = houses

    def info(self):
        for i in self.houses:
            i.house_info()

    def steal_money(self, human):
        if randint(1, 10) == 10:
            human.availability_of_money = 0
            print(f'Realtor {self.name} steal my money!')

        else:
            pass
    
    def sell_house(self, name, house):
        if self.discount is True:
            house.discount()
            if name.money >= house.cost:
                print(f'Now i have {name.money} piastres', '\n')
                name.home = True
                self.houses.remove(house)
            else:
                while name.money < house.cost:
                    print('I need to work more')
                    name.make_money()
                print(f'Now i have {name.money} piastres')
                name.home = True
                print(f'Finally i can buy a {house.name}', '\n')
                self.houses.remove(house)


human = Human('Yurii', 28, 100, False)
human.info_about_human()
human.make_money()
house_1 = Small_House('house №1',randint(20, 150), randint(5000, 20000))
house_2 = Small_House('house №2',randint(20, 150), randint(5000, 20000))
house_3 = Small_House('house №3',randint(20, 150), randint(5000, 20000))
human.buy_house(house_1)
human.buy_house(house_2)
human.buy_house(house_3)
realtor = Realtor('Robin', [house_1, house_2, house_3])
realtor.info()
realtor.steal_money(human)
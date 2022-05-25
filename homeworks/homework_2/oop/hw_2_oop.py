'''
1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class
'''
from abc import abstractclassmethod, ABC


class Animal:
    def __init__(self, name, eat, sleep):
        self.name= name
        self.eat = eat
        self.sleep = sleep

    def name_of_animal(self):
        print("I'm", self.name)
    def type_of_eat(self):
        print("My food is", self.eat)
    def hours_sleep(self):
        print(f"I sleep {self.sleep} hours a day")


class Lion(Animal):
    def __init__(self, name, eat, sleep):
        super().__init__(name, eat, sleep)
    def for_the_enemy_a_command_voice(self):
        print('AAAAAAARRRRRR')
    def for_the_friend_a_command_voice(self):
        print("meow-meow")

alex = Lion("Alex", "meat", "10")
alex.name_of_animal()
alex.type_of_eat()
alex.hours_sleep()
alex.for_the_enemy_a_command_voice()
alex.for_the_friend_a_command_voice()
print(issubclass(Lion, Animal), "\n")


class Zebra(Animal):
    def __init__(self, name, eat, sleep):
        super().__init__(name, eat, sleep)
    def command_to_escape(self):
        print('RUN VASIA RUN')
    def command_to_defend_bro(self):
        print('Get out of here I know karate')

marty = Zebra("Marty", "grass", "6")
marty.name_of_animal()
marty.type_of_eat()
marty.hours_sleep()
marty.command_to_escape()
marty.command_to_defend_bro()
print(issubclass(Zebra, Animal), "\n")


class Lemur(Animal):
    def __init__(self, name, eat, sleep):
        super().__init__(name, eat, sleep)
    def command_to_look_enemy(self):
        print("I see you")
    def command_to_have_fun(self):
        print("We dance and move our holes")

julien = Lemur("Julien", "fruits", "14")
julien.name_of_animal()
julien.type_of_eat()
julien.hours_sleep()
julien.command_to_look_enemy()
julien.command_to_have_fun()
print(issubclass(Lemur, Animal), "\n")


class Giraffe(Animal):
    def __init__(self, name, eat, sleep):
        super().__init__(name, eat, sleep)
    def command_to_be_afraid(self):
        print("I'm afraid I need to hide")
    def command_I_am_a_hero(self):
        print("Сome here I will show you who is the tallest animal in the world")

melman = Giraffe('Melman', "leaf", "7")
melman.name_of_animal()
melman.type_of_eat()
melman.hours_sleep()
melman.command_to_be_afraid()
melman.command_I_am_a_hero()
print(issubclass(Giraffe, Animal), "\n")

class Hippo(Animal):
    def __init__(self, name, eat, sleep):
        super().__init__(name, eat, sleep)
    def command_to_keep_everything_under_control(self):
        print("No panic everyone obey me")
    def command_sing(self):
        print('''Chunky, chunky, chunky, chunky, chunky, chunky
And plumpy
Plumpy, plumpy, plumpy, plumpy, plumpy,
Chunky, chunky, chunky, chunky, chunky, chunky,
And plumpy,
Plumpy, plumpy, plumpy, plumpy, plumpy''')

gloria = Hippo("Gloria", "all food", "6")
gloria.name_of_animal()
gloria.type_of_eat()
gloria.hours_sleep()
gloria.command_to_keep_everything_under_control()
gloria.command_sing()
print(issubclass(Hippo, Animal))

# ===========================================================

'''1.a. Create a new class Human and use multiple inheritance to create Centaur class,
 create an instance of Centaur class and call the common method of these classes and unique.'''

class Human():
    def __init__(self, nickname, age, nationality, profession):
        self.nickname = nickname
        self.age = age
        self.nationality = nationality
        self.profession = profession

    def get_info_about_Human(self):
        print(f"Nickname {self.nickname}\n"
        f'Human age {self.age}\n'
        f'Nationality of the person {self.nationality}\n'
        f'My profession {self.profession}')


class Centaur(Animal, Human):
    def __init__(self, name, nickname, eat, sleep, age, nationality, profession, religion):
        Animal.__init__(self, name, eat, sleep)
        Human.__init__(self, nickname, age, nationality, profession)
        self.religion = religion

    def get_info_about_Centaur(self):
        print(f'Name: {self.name}\n'
        f'Nickname: {self.nickname}\n'
        f'Age: {self.age}\n'
        f'Nationality: {self.nationality}\n'
        f'Profession: {self.profession}\n'
        f'Religion: {self.religion}')

hiron = Centaur('Hiron', 'Thessalian centaur', 'all eat', '6', '3000', 'Greek', 'half god','pagan')
hiron.get_info_about_Centaur()
hiron.name_of_animal()
hiron.get_info_about_Human()
hiron.hours_sleep()
hiron.type_of_eat()

#========================================================================================

'''2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.'''



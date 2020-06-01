from __future__ import print_function

class Employee:
    def __init__ (self, name, salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)
    def work(self):
        print(self.name, "does stuff") # делает что-то
    def __repr__ (self) :
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)

class Chef(Employee):
    def __init__ (self, name):
        Employee.__init__ (self, name, 50000)
    def work(self):
        print(self.name, "makes food") # готовит еду

class Server(Employee):
    def __init__ (self, name):
        Employee.__init__ (self, name, 40000)
    def work(self):
        print(self.name, "interfaces with customer") # взаимодействует
    # с клиентом

class PizzaRobot(Chef):
    def __init__ (self, name):
        Chef.__init__ (self, name)
    def work(self):
        print(self.name, "makes pizza") # готовит пиццу

if __name__ == "__main__" :
    bob = PizzaRobot('bob') # Создать робота по имени bob
    print (bob) # Выполняется унаследованный метод__ repr__
    bob.work () # Выполняется действие, специфичное для типа
    bob.giveRaise (0.20) # Повысить зарплату роботу bob на 20%
    print(bob); print()
    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__ )
        obj.work()
______________________________________________________________
from __future__ import print_function
from employees import PizzaRobot, Server
class Customer:
    def __init__ (self, name):
        self.name = name
    def order(self, server):
        print(self.name, "orders from",
    def pay(self, server):
        print(self.name,
    class Oven:
        def bake(self):
            print("oven bakes")
class PizzaShop:
    def __init__ (self) :
        self.server = Server('Pat’)
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()
    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)
if __name__ == "__main__":
    scene = PizzaShop ()
    scene.order(’Homer')
    print(’...’)
    scene.order('Shaggy')

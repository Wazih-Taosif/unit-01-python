"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
print()
print("------------Task1-----------")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduction(self): #introduces the person with their name and age.
        print(f"Hello my name is {self.name} and I am {self.age} years old")

wazih = Person("Wazih Taosif", 18)
wazih.introduction()


"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
print()
print("----------Task2----------")
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak():
        return "bark"
class Cat(Animal):
    def speak():
        return "meow"

golden_retriever = Dog
print(golden_retriever.speak()) #prints the speaking method of the object

persian = Cat
print(persian.speak()) #prints the speaking method of the object




"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
print()
print("-----------Task3-----------")

class BankAccount:
    balance = 1000 #placeholder balance
    owner = "Wazih"
    def __init__(self, deposite, withdraw):
        self.deposite = deposite
        self.withdraw = withdraw
        self.balance = self.balance + deposite #adds the deposited amount to the total balance
        self.balance = self.balance - withdraw #Subtracting the withdrawn amount from the total balance

bank = BankAccount(200, 100) #object bank, depositing 200, and withdrawing 100
print(f"Current balance: {bank.balance}.")
from abc import ABC, abstractmethod


# - ABSTRACT BASE CLASS (PARENT) 
# Animal inherits from ABC - this makes it an abstract class (Abstraction)
class Animal (ABC):

    # Parent constructor - stores attributes shared by ALL animals
    def __init__ (self, name, habitat):
        self.name = name
        self.habitat = habitat

    # concrete method - all child classes inherit this for free
    def display(self):
        print(f"Name: {self.name} | Habitat {self.habitat}")

    # Abstract method - every child MUST implement this
    @abstractmethod
    def speak(self):
        pass

# CHILD CLASS 1
class Dog(Animal):

    def __init__ (self, name, habitat, bread):
        super().__init__(name, habitat)  # calls Animals' constructer
        self.breed = self.breed
    
    def speak (self):
        print(f"{self.name} ({self.breed}) says: Woof! Woof!")

#  CHILD CLASS 2
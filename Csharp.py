import copy
from Coding_Language import Language

# ConcretePrototype2
class Csharp(Language):
    def __init__(self, name: str, pun_name: str):
        super().__init__(name)
        self.pun_name = pun_name
    
    def clone(self):
        return copy.copy(self)
    
    def display(self):
        print('Csharp was cloned:')
        print('-------------------')
        print(f'Name: {self.language_name}')
        print(f"Did You Know My Name Is A Pun Because {self.pun_name}\n")
    
    def get_course(self):
        return self.pun_name
    
    def set_course(self, pun_name: str):
        self.pun_name = pun_name


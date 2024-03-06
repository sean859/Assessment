import copy
from Coding_Language import Language

# ConcretePrototype3
class Java(Language):
    def __init__(self, name: str, syntax: str):
        super().__init__(name)
        self.syntax = syntax
    
    def clone(self):
        return copy.copy(self)
    
    def display(self):
        print('Java was cloned:')
        print('-------------------')
        print(f'Name: {self.language_name}')
        print(f"I Use Different Syntax's Like: {self.syntax}\n")
    
    def get_course(self):
        return self.syntax
    
    def set_course(self, syntax: str):
        self.syntax = syntax


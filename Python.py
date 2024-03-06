import copy
from Coding_Language import Language

# ConcretePrototype1
class Python(Language):
    def __init__(self, name: str, logo: str):
        super().__init__(name)
        self.logo = logo
    
    def clone(self):
        return copy.copy(self)
    
    def display(self):
        print('Python was cloned:')
        print('-------------------')
        print(f'Name: {self.language_name}')
        print(f"Who's Logo Looks Like A {self.logo}\n")
    
    def get_course(self):
        return self.logo
    
    def set_course(self, logo: str):
        self.logo = logo

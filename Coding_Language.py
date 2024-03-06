from abc import ABC, abstractmethod

# Prototype
class Language(ABC):
    def __init__(self, name: str):
        self.language_name = name
        
    @abstractmethod
    def clone(self):
        pass
    
    @abstractmethod
    def display(self):
        pass

    def get_name(self):
        return self.language_name
    
    def set_name(self, name: str):
        self.language_name = name


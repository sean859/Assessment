from Python import Python
from Csharp import Csharp
from Java import Java

# This function is called 'main' and used to call called objects from other classes in different files to be displayed, because all the subclass (Python, Csharp, Java)
# are all inheriting from a parent class called 'Language' then adding their own details to that class then creating an object out of those details, then copying
# then those copyed objects are sent here and displayed with their correct subclass
def main():
    python = Python("Python", "Plus Sign")            
    pythonclone = python.clone()
    pythonclone.display()

    csharp = Csharp("Csharp", "Because The # Looks Like Two Pluses Which Is Why My Other Language is C++, GET IT!")
    Csharpclone = csharp.clone()
    Csharpclone.display()

    java = Java("Java", "*Inset Java Syntax's Here*")            
    javaclone = java.clone()
    javaclone.display()  
if __name__ == "__main__":
    main()


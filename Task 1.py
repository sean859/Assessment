# Creating a new dictionary that will be labeled as 'Contact_Book' to function as the Contact book
Contact_Book = {'Random Person': 'Random Value', 'Random Person': 'Random Value', 'Random Person': 'Random Value'}

# This class will be called in the 'Add_New_Vendor' function to request the company name, email, and phone number of the vendor called 'Vendor' 
class Vendor:
        def __init__(self, company_name, phone, email):
            self.company_name = company_name
            self.phone = phone
            self.email = email
        def print_vender(self):
            print("Are These details correct?")
            print("Name: " + self.company_name)
            print("Phone: " + self.phone)
            print("Email: " + self.email)
            print("If correct type 'Yes', otherwise type nothing")
            if input() == "Yes":
                  Contact_Book[self.company_name] = "Phone: " + self.phone, "Email: " + self.email
                  print("Your record has been added")
                  print(Contact_Book)
            else:
                 print("New Record Addition Cancelled")

# This function will be called 'Contact_Book_Display', and will be used to view all the different options of the contact book
# allowing the user to input a number to pick the specific option, was typed it will called the correct function and execute it
# then once the action is complete it will return the user to the contact book display again
def Contact_Book_Display():
    print("-----Contact Book-----")
    print("To select an option press the corrosponding number")
    print("1. Add New Vendor")
    print("2. View A Vendor's Information")
    print("3. Remove A Current Vendor")
    print("4. View All Vendor Information")
    contactbookinput = input("Option Selected: ")
    if contactbookinput == "1":
        Add_New_Vendor()
    elif contactbookinput == "2":
        View_Vendor_Info()
    elif contactbookinput == "3":
        Remove_Vendor()
    elif contactbookinput == "4":
        Show_Vendors()
    else:
        print("Please enter a valid number")
        Contact_Book_Display()

# This functin will be called when the user wants to add a new vendor called 'Add_New_Vendor', this function 
# will ask for their company name, phone number, and email address, via input then add those inputs
# to the Contact Book
def Add_New_Vendor():
    print("Please enter your full company name")
    company_name = input()
    print("Please enter your phone number")
    phone = input()
    print("Please enter your email address")
    email = input()
    NewVender = Vendor(company_name, phone, email)
    NewVender.print_vender() 
    Contact_Book_Display() 

# This function will be called 'View_Vendor_Info', and will be used to view a specific vendors information by typing
# in the full company name of the vendor
def View_Vendor_Info():
    print("Search by full name")
    search = input()
    if search in Contact_Book:
         print(Contact_Book.get(search))
         Contact_Book_Display()
    else:
         print("No Record Found")
         Contact_Book_Display()


# This function will be called 'Remove_Vendor', and will be used to remove a vendor and their information from the
# contact book by typing the full company name of the vendor
def Remove_Vendor():
    removethisperson = input("Type the full company name of the record you want to delete: ")
    if removethisperson in Contact_Book:
        Contact_Book.pop(removethisperson)
        print(removethisperson + " was removed from record")
        Contact_Book_Display()
    else:
         print("Record Not Found")
         Contact_Book_Display()


# This function will be called 'Show_Vendors', and will be used to print the our contact book display all the vendors as 
# the keywords, then their information (phone and email), as the values
def Show_Vendors():
     print(Contact_Book)
     Contact_Book_Display()

Contact_Book_Display()

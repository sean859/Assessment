# This function is called 'check_stock' and is used to count the amount of values in a list then print the amount 
# this is done by taking a list, and adding 1 to a variable called 'stock_amount' for every str (word) in the list
# then prints it after via the print function
stock_list = ["smartphone", "laptop", "tablet", "smartphone case", "laptop charger", "tablet cover"]
def check_stock(food_list):
    stock_amount = 0
    for str in food_list:
        stock_amount = stock_amount + 1
    return stock_amount
print('The Stock Amount Is:', check_stock(stock_list))

# This will create a new tuple with three values (17, 28, 30), then print the value in the third position, then 
# after that print if the word 'Stick Notes' is present in the tuple if not then it prints 0
office_supply = (17, 28, 30)
print(office_supply[2])
print(office_supply.count("Sticky Notes"))



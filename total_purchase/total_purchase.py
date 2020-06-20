
# A customer in a store is purchasing five items. Write a program that asks for the price of
# each item, and then displays the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.

# assuming the items are oranges, mango, rice, milk, chocolat
orange = input('How much is the orange ? ')
mango = input('How much is the mango ? ')
rice = input('How much does the rice cost ? ')
milk = input('How much does the milk cost ? ')
chocolate = input('How much is the chocolate ? ')
subtotal = int(orange + mango + rice + milk + chocolate)
amount_of_sale_tax = int(subtotal * 0.007)
total = int( subtotal + amount_of_sale_tax)
print(total)


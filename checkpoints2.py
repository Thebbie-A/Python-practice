# Let’s step through the process of writing a program that calculates a percentage.
# Suppose a retail business is planning to have a storewide sale where the prices of all items
# will be 20 percent off. We have been asked to write a program to calculate the sale price of an item
# after the discount is subtracted. Here is the algorithm:
# 1. Get the original price of the item.
# 2. Calculate 20 percent of the original price. This is the amount of the discount.
# 3. Subtract the discount from the original price. This is the sale price.
# 4. Display the sale price.

#input the original price
original_price = int(input("Enter the original price : "))

#convert the percentage into decimals
#thus divide 20 by 100
percent_off = 0.2

#finding the discount
Discount = original_price * 0.2

#finding the sale price
sale_price = original_price - int(Discount)

print("The sale price is ", sale_price)


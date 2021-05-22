# # Let us say your expense for every month are listed below,
# #
# # January -  2200 ,
# # February - 2350 ,
# # March - 2600 ,
# # April -  2130
# # May - 2190,
# # Create a list to store these monthly expenses
# # and using that find out,
# # a. In Feb, how many dollars you spent extra compare to January?
# # b. Find out your total expense in first quarter (first three months) of the year.
# # c. Find out if you spent exactly 2000 dollars in any month
# # d. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# # e.You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to
# # your monthly expense list based on this.
#
# # Dollars spent extra compared to January
list1 = ['January', 'February', 'March', 'April', 'May']
list2 = [2200, 2350, 2600,  2130, 2190]
total_expenses = 11470
extra_amount_spent = list2[1] - list2[0]
print(extra_amount_spent,"$")

# total expenses in first quarter
first_quarter_expense = list2[0] + list2[1] + list2[3]
print(first_quarter_expense)

# likely spent 2000 dollars in a month
amount1 = list2[0] / int(total_expenses) * 2000
print(amount1)
amount1 = list2[1] / int(total_expenses) * 2000
print(amount1)
amount1 = list2[2] / int(total_expenses) * 2000
print(amount1)
amount1 = list2[3] / int(total_expenses) * 2000
print(amount1)
amount1 = list2[4] / int(total_expenses) * 2000
print(amount1)
#
# amount_spent = 2000 in list2
# print(amount_spent)
#
# # current total list in June
list1.append("June")
print(list1)

# list2.append(1980)
# print(list2)
#
# # total amount in April after returning item
list2[3]= 200
print(list2)

fruit = ['mango', 'apple', 'orange', 'strawberry']
for x in 'mango':
    print(x)
fruit_2 = ['banana', 'guava' , 'coconut', 'pear', 'pawpaw']
for x in fruit_2 :
    print(x)
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
   print(num)
   if num == 5:
    break

num= 2 / 2
print(num)
#
#




























for i in range(2 , 51):
    print(i)


# After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out count for “heads”

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for lists in result:
    if lists == 'heads':
        count += 1
        print('heads count',count)


# Your monthly expense list (from Jan to May) looks like this, expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in
# which month that expense occurred.
# If expense is not found then convey that as well

monthly_expense_lists = ['january: 2340, februray:2500 ,march: 2100, april:3100, may:2980']
# expense_list = [2340, 2500, 2100, 3100, 2980]
expense = int(input('Enter an expense amount: '))
amount_outcome = expense  == monthly_expense_lists
for expense in monthly_expense_lists:
    if expense == 'january':
        print('amount')
        continue

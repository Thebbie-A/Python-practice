# Chris owns an auto repair business and has several employees. If any employee works over
# 40 hours in a week, he pays them 1.5 times their regular hourly pay rate for all hours over
# 40. He has asked you to design a simple payroll program that calculates an employee’s
# gross pay, including any overtime wages. You design the following algorithm:
# Get the number of hours worked.
# Get the hourly pay rate.
# If the employee worked more than 40 hours:
# Calculate and display the gross pay with overtime.
# Else:
# Calculate and display the gross pay as usual.

hours = float(input('Enter number of hours worked '))
pay_rate = input( 'Enter hourly pay rate ')
multiplier = 1.5
overtime = 40

if  hours > 40:
    overtime_hours = hours - overtime
    overtime_pay = overtime_hours * int(pay_rate) * multiplier
    gross_pay = int(hours) * int(multiplier) + int(overtime)
    print(gross_pay)
    print('Display the Gross pay with overtime')

else:
    gross_pay2 = hours * int(pay_rate)
    print(gross_pay2)
    print('The usual gross pay')
   

# Hi Williano how do I print the else statememt if i want it to be printed out?

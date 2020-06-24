# Kathryn teaches a science class and her students are required to take three tests. She wants
# to write a program that her students can use to calculate their average test score. She also
# wants the program to congratulate the student enthusiastically if the average is greater
# than 95. Here is the algorithm in pseudocode:
# Get the first test score
# Get the second test score
# Get the third test score
# Calculate the average
# Display the average
# If the average is greater than 95:
# Congratulate the user

high_score = 95
test1 = int(input('Enter your test score '))
test2 = int(input('Enter your test score '))
test3 = int(input('Enter your test score '))
average = int(test1) + int(test2) + int(test3) / 3
print(average)

if average >= high_score :
    print('Congratulate the student')
    print('Well, done, this is a great average')

# Write an if statement that assigns 0 to x if y is equal to  20.

x = 0
y = 20
if y > x:
    x = 0
    print(x)



# Write an if statement that assigns 0.2 to commissionRate if sales is greater  than or equal  to 10000.
#
# commisiionRate = 0.2
sales = 10000
if sales >= 10000:
    commisionRate = 0.2
    print(commisionRate)




# Let’s step through the process of writing a program that calculates an average. Suppose you
# have taken three tests in your computer science class, and you want to write a program that
# will display the average of the test scores. Here is the algorithm:
# 1. Get the first test score.
# 2. Get the second test score.
# 3. Get the third test score.
# 4. Calculate the average by adding the three test scores and dividing the sum by 3.
# 5. Display the average.


test_1 = int(input(" Enter your first test score: "))
test_2 = int(input(" Enter your second test score: "))
test_3 = int(input(" Enter your third test score: "))

#divide the scores by 3
average = (test_1 + test_2 + test_3) / 3

print("The average scores is ", average)
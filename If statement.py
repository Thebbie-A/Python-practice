# # # write a program that ask a user to enter a number. Program should then tell if the number is odd or even.
# #
# num = input('Enter a number : ')
# num = int(num)
# if num % 2 == 0:
#     print('Number is even')
# else:
#     print('number is odd')
# #
# # # # write a program that ask a user to enter the name of a dish  and then it should print the name of the cuisine
# Ghanaian = ['fufu''banku''yaw with kontobire stew']
# cote_devoire = ['acheke''rice with pepper' 'danke']
# nigeria =['moimoi', 'eba', 'yam with oil']
# dish = input(' Enter the name of a dish :')
#
# if dish in Ghanaian:
#     print('Ghanaian dish')
# elif dish in cote_devoire:
#     print('ivorian dish')
# elif dish in nigeria:
#     print('naija food')
# else:
#     print('I do not know the the name of this dish and its origin')
#
# #
# # # # Write a program that uses following list of cities per country,
# # # # usa = [ “atlanta”, “new york”, “chicago”, “baltimore”]
# # # # uk = [“london”, “bristol”, “cambridge”]
# # # # india = [“mumbai”,”delhi”, “banglore”]
# # # # (a) Write a program that asks user to enter a city name and it should tell you which country it belongs to
# # #
# # #
# usa = ['atlanta', 'new york', 'chicago', 'baltimore']
# uk = ['london', 'bristol', 'cambridge']
# india = ['mumbai','delhi', 'banglore']
#
# city = input(' Enter the name of a city: ')
# if city in usa:
#     print('The city is in the state')
# elif city in uk:
#     print('This city is located in UK')
# elif city in india:
#     print('City in india')
# else:
#     print('i do not know where this city is located, thank you')
#
# # # (b) Write a program that asks user to enter two cities and tell you if they both are in same country or not
# # usa = ['atlanta', 'new york', 'chicago', 'baltimore']
# # uk = ['london', 'bristol', 'cambridge']
# # india = ['mumbai','delhi', 'banglore']
# #
# city_1 = input('Enter the name of the 1st  city: ')
# city_2 = input('Enter the name of the 2nd city: ')
# if city_1 in usa and city_2 in usa:
#     print('Both cities are in the state.')
# elif city_1 in uk and city_2 in uk:
#     print('Both cities are in the uk')
# elif city_1 in india and city_2 in india:
#     print('Both cities are in india')
# else:
#     print('Both are not in the same country')


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


test_score1 = input('First test score: ')
test_score2 = input('Second test score: ')
test_score3 = input('Third test score: ')
high_score = 95
average = int(test_score1 + test_score2 + test_score3) / 3
 # print(total)
if average >= high_score:
    print('Congratulations for your success')
else:
    print('Well done, better luck next time')





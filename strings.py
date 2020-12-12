# 1. Create a string variable to store this text "Earth revolves around the sun,"
# a. Print substring “revolves”
# b. Print substring “sun” using negative index
# c. print  Earth revolves around the sun

#name varialbe
message = "Earth revolves around the sun"

# print results
print(message[5:15])
print(message[25:29])
print(message)


# 2. Create three string variables with values “I love eating“, “veggies”, “fruits”
# a. Print “I love eating veggies and fruits” (Hint: Use + operator)
# b. Create fourth variable to store number of fruits you eat everyday. Say for example you eat 2 fruits everyday,
# in that case print “I love eating 2 fruits everyday”


# three variables
message_1 = "I love eating"
item = " veggies"
type_ = "fruits"
print(message_1 +"" +item +" and  " + type_)

#

mango = 2
banana = 3
apple = 2
message_2 = " I love eating "
message_3 = "fruit everyday"
print(message_2 +"" + "" + str(banana)+" "+ message_3)
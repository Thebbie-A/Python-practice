# str = 'debora is my sweetheart'
# #1 Capitalize - Capitalizes first letter of string
# print(str.capitalize()); # Debora
# #2 center(width, fillchar) - Returns a space-padded string with the original string centered to a total of width columns.
# print(str.center(100, ' '));
#
# #3 Count - Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.
# print(str.count('e')); # 4

#4 encode - Returns encoded string version of string;
import codecs
string = b'deborah is my sweetheart'
for b in string:
    print(b, end=' ')
print('\n')
e_bytes = codecs.encode(string, 'hex')
print(e_bytes.decode())
d_bytes = codecs.decode(e_bytes, 'hex')
print(d_bytes.decode())

#5 endswith - endswith(suffix, beg=0, end=len(string))
#Determines if string or a substring of string (if starting index beg and ending
# index end are given) ends with suffix; returns true if so and false otherwise.
#
# name = 'deborah';
# print(name.endswith('a'));
# print(name.endswith('a', 2, 5));
# print(name.endswith('a', 2, 6));
#
# #6 Find -  	find(str, beg=0 end=len(string))
# # Determine if str occurs in string or in a substring of string if starting index
# # beg and ending index end are given returns index if found and -1 otherwise.
#
# suffix = 'or'
# print(name.find(suffix)); #3
# print(name.find(suffix,5,7)); #-1
#
# find more at https://www.tutorialspoint.com/python/python_strings.htm
#

ab = 'lino'
print(dir(ab))




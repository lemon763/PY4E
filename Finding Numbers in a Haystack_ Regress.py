#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
#Data Files
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_1823602.txt (There are 87 values and the sum ends with 889)
import re

filename = input('Input filename:')
if len(filename) < 1:
    filename = 'regex_sum_1823602.txt'

res = 0
fh = open(filename)
for line in fh:
    tmp = re.findall('[0-9]+', line)

    
    for x in tmp:
        res = res + int(x)

print(res)

#Problem 1

#Introduction

#Say Hello, World! With Python

print("Hello, World!")

#Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if n%2 != 0:
        print("Weird")
    
    if (n%2 == 0) and (2 <= n <= 5):
        print("Not Weird")
        
    if (n%2 == 0) and (6 <= n <= 20):
        print("Weird")
        
    if (n%2 == 0) and (n > 20):
        print("Not Weird")

#Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)

#Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)

#Loops

if __name__ == '__main__':
    n = int(input())
    
    for x in range(0, n):
        print(x*x)

#Write a function

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
        else:
            leap = True
        
    return leap

year = int(input())
print(is_leap(year))

#Print Function

if __name__ == '__main__':
    n = int(input())
    
    for x in range(1, n+1):
        print(x)+print(x+1)

#Data Types

#List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list_ = [[i, j, k] 
            for i in range(x+1)
                for j in range(y+1)
                    for k in range(z+1)
                        if i+j+k != n]
    
    print(list_)

#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    list_ = list(arr)
    list_ = sorted(list_)
    
    res = set(list_)
    res.remove(max(res))
    
    print(max(res))

#Nested Lists

if __name__ == '__main__':
    
    list_ = []
    scores_ = []
    names_ = []
    
    
    for n in range(int(input())):
        name = input()
        score = float(input())
        list_.append([name, score])
        
    
    scores_ = [item[1] for item in list_]

    score_set = set(scores_)
    score_set.remove(min(list(score_set)))
    
    a = min(score_set)
    
    names_ = [item[0] for item in list_ if item[1] == a]
    
    names_.sort()
    
    for x in names_:
        print(x)

#Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for student in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for name_, scores_ in student_marks.items():
        if name_ == query_name:
            print("{:.2f}".format(sum(scores_)/len(scores_)))

#Lists

if __name__ == '__main__':
    N = int(input())
    
    res = []
    
    for n in range(N):
        cmd = input().split()
        
        if cmd[0] == "insert":
            res.insert(int(cmd[1]), int(cmd[2]))
            
        if cmd[0] == "print":
            print(res)
            
        if cmd[0] == "remove":
            res.remove(int(cmd[1]))
            
        if cmd[0] == "append":
            res.append(int(cmd[1]))
            
        if cmd[0] == "sort":
            res.sort()
            
        if cmd[0] == "pop":
            res.pop()
            
        if cmd[0] == "reverse":
            res.reverse()

#Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    res = tuple(integer_list)
    
    print(hash(res))

#Strings

#sWAP cASE

def swap_case(s):
    return s.swapcase()
  
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#String Split and Join

def split_and_join(line):
    # write your code here
    res = line.split(" ")
    return "-".join(res)

#What's Your Name?

def print_full_name(first, last):
    # Write your code here
    print('Hello ' + first + ' ' + last + '! You just delved into python.')

#Mutations

def mutate_string(string, position, character):
    res = list(string)
    res[position] = character
    res = ''.join(res)
    return res

#Find a string

def count_substring(string, sub_string):
    count = 0
    while sub_string in string:
        i = string.find(sub_string)
        string = string[i+1:]
        count += 1
    return count

#String Validators

if __name__ == '__main__':
    s = input()
    print(any(letter.isalnum() for letter in s))
    print(any(letter.isalpha() for letter in s))
    print(any(letter.isdigit() for letter in s))
    print(any(letter.islower() for letter in s))
    print(any(letter.isupper() for letter in s))

#Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

Text Wrap

def wrap(string, max_width):
    res = textwrap.wrap(string, max_width)
    return "\n".join(res)

#Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int,input().split())

#Upper Triangle
for i in range(1, N, 2): 
    print((i * ".|.").center(M, "-"))

#Welcome Line
print("WELCOME".center(M,"-"))

#Lower Triangle
for i in range(N-2, -1, -2): 
    print((i * ".|.").center(M, "-"))

#String Formatting

def print_formatted(number):
    # your code goes here
    
    width = len(str(bin(number)[2:]))
    
    for i in range(1, number+1):
        dec_ = str(i)
        oct_ = str(oct(i)[2:])
        hex_ = str(hex(i)[2:]).upper()
        bin_ = str(bin(i)[2:])
        
        print(dec_.rjust(width, ' '), oct_.rjust(width, ' '), hex_.rjust(width, ' '),
              bin_.rjust(width, ' '), sep = ' ')

#Alphabet Rangoli

import string

def print_rangoli(size):
    # your code goes here
    alpha_ = string.ascii_lowercase[0:size]
    
    #First size rows
    for i in range(size):
        str_ = "-".join(alpha_[size - 1 - i: size])
        res = str_[::-1] + str_[1:]
        print(res.center((4*size)-3, "-"))
        
    #Remaining rows    
    for i in range(1, size):
        str_ = "-".join(alpha_[i: size])
        res = str_[::-1] + str_[1:]
        print(res.center((4*size)-3, "-"))

#Capitalize!

# Complete the solve function below.
def solve(s):
     res = [i.capitalize() for i in s.split(" ")]
     return " ".join(res)

#The Minion Game

def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    score_Stuart = 0
    score_Kevin = 0
    
    for i in range(len(string)):
        if string[i] in vowels:
            score_Kevin += len(string) - i # e.g. first 'A' in BANANA forms 5 possible words. Same goes for the following vowels.
        else:
            score_Stuart += len(string) - i
    
    if score_Kevin > score_Stuart:
        print("Kevin", score_Kevin)
    
    if score_Kevin < score_Stuart:
        print("Stuart", score_Stuart)
    
    if score_Kevin == score_Stuart:
        print("Draw")

#Merge the Tools!

def merge_the_tools(string, k):
    # your code goes here
    list_ = []
    for i in range(0, len(string), k):
        list_.append("".join(dict.fromkeys(string[i:i+k])))

    for j in list_:
        print(j)

#Sets

#Introduction to Sets

def average(array):
    # your code goes here
    res = sum(set(array))/len(set(array))
    return "{:.3f}".format(res)

#No Idea!

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
array = list(map(int, input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
happiness = 0

for item in array:
    if item in A:
        happiness += 1
    if item in B:
        happiness -= 1
    else:
        happiness += 0

print(happiness)

#Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
list_a = list(input().split())
list_a = list(map(int, list_a))
a = set(list_a)
    
N = int(input())
list_b = list(input().split())
list_b = list(map(int, list_b))
b = set(list_b)


res = a.symmetric_difference(b)
res = list(res)

for ele in sorted(res):
    print(ele)

#Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
names_ = set()
for i in range(N):
    names_.add(input())

print(len(names_))

#Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    cmd = input().split()
    
    if cmd[0] == 'pop':
        s.pop()
    if cmd[0] == 'discard':
        s.discard(int(cmd[1]))
    if cmd[0] == 'remove':
        s.remove(int(cmd[1]))
        
print(sum(s))

#Set .union() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = set(input().split())

b = int(input())
french = set(input().split())

print(len(eng.union(french)))

#Set .intersection() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = set(input().split())

b = int(input())
french = set(input().split())

print(len(eng.intersection(french)))

#Set .difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = set(input().split())

b = int(input())
french = input().split()

print(len(eng.difference(french)))

#Set .symmetric_difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = set(input().split())

b = int(input())
french = input().split()

print(len(eng.symmetric_difference(french)))

#Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
A = set(map(int, input().split()))

N = int(input())

for i in range(N):
    cmd = input().split()
    set_ = set(map(int, input().split()))
    
    if cmd[0] == "update":
        A.update(set_)
    if cmd[0] == "intersection_update":
        A.intersection_update(set_)
    if cmd[0] == "difference_update":
        A.difference_update(set_)
    if cmd[0] == "symmetric_difference_update":
        A.symmetric_difference_update(set_)

print(sum(A))

#The Captain's Room

# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
list_ = map(int, input().split())
a = set()
b = set()

for i in list_:
    if i not in a:
        a.add(i)
    else:
        b.add(i)

print(list(a.difference(b))[0])

#Check Subset

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for i in range(T):
    A, a = int(input()), set(map(int, input().split()))
    B, b = int(input()), set(map(int, input().split()))

    print(a.issubset(b))

#Check Strict Superset

# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())

print(all(A.issuperset(set(map(int, input().split()))) for i in range(n)))

#Collections

#collections.Counter()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
shoe_size = Counter((map(int, input().split())))
N = int(input())
earnings = 0

for i in range(N):
    size, price = map(int, input().split())
    if shoe_size[size]:
        earnings += price
        shoe_size[size] -= 1

print(earnings)

#DefaultDict Tutorial

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
words = defaultdict(list)

for i in range(1, n+1):
    words[input()].append(str(i))
    
for i in range(1, m+1):
    B = input()
    if B in words:
        print(" ".join(words[B]))
    else:
        print(-1)

#Collections.namedtuple()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
col_1, col_2, col_3, col_4 = input().split()
total_marks = 0
student_profile = namedtuple('student_profile', col_1 + ' ' + col_2 + ' ' + col_3 + ' ' + col_4)

for i in range(N):
    arg_1, arg_2, arg_3, arg_4 = input().split()
    student = student_profile(arg_1, arg_2, arg_3, arg_4)
    total_marks += int(student.MARKS)

print('{:.2f}'.format(total_marks/N))

#Collections.OrderedDict()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

N = int(input())
od = OrderedDict()

for i in range(N):
    words = list(input().split())
    item_name = " ".join(words[:-1])
    price = int(words[-1])
    
    if od.get(item_name):
        od[item_name] += price
    else:
        od[item_name] = price
    
for n, p in od.items():
    print(n, p)

#Word Order

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
list_ = []
for i in range(int(input())):
    list_.append(input())
print(len(set(list_)))
print(*Counter(list_).values())

#Collections.deque()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
N = int(input())
d = deque()
for i in range(N):
    cmd = input().split()
    if cmd[0] == "append":
        d.append(cmd[1])
    if cmd[0] == "pop":
        d.pop()
    if cmd[0] == "popleft":
        d.popleft()
    if cmd[0] == "appendleft":
        d.appendleft(cmd[1])

for x in d:
    print(x, end=" ")

#Company Logo

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    list_ = []
    for char in s:
        list_.append(char)
    list_ = sorted(list_)
    res = Counter(list_)
    res = res.most_common(3)
    
    for a, b in res:
        print(a, b)

#Piling Up!

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    flag = 'No'
    blocks = []
    n = int(input())
    blocks = list(map(int, input().split()))
    mx = max(blocks)
    if blocks[0] == mx or blocks[-1] == mx:
        flag = 'Yes'
    print(flag)

#Date and Time

#Calendar Module

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
date_ = input().split()
res_ = calendar.day_name[calendar.weekday(int(date_[-1]), int(date_[0]), int(date_[1]))]
print(res_.upper())

#Time Delta

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    time_1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    time_2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return str(int(abs(time_1-time_2).total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

#Exceptions

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

#Built-ins

#Zipped!

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
mark_sheet = []

for i in range(X):
    mark_sheet.append(map(float, input().split()))

res = zip(*mark_sheet)

for i in res:
    print(sum(i)/len(i))

#Athlete Sort

#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    res = sorted(arr, key = itemgetter(k))
    
    for i in res:
        print(*i)

#ginortS

# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
S = input().strip()
lowercase = []
uppercase = []
even_no = []
odd_no = []
odds = ['1', '3', '5', '7', '9']
evens =['0', '2', '4', '6', '8']

for char in S:
    if char in string.ascii_lowercase:
        lowercase.append(char)
    if char in string.ascii_uppercase:
        uppercase.append(char)
    else:
        if char in odds:
            odd_no.append(char)
        elif char in evens:
            even_no.append(char)
            
for i in sorted(lowercase):
    print(i, end='')
for i in sorted(uppercase):
    print(i, end='')
for i in sorted(odd_no):
    print(i, end='')
for i in sorted(even_no):
    print(i, end='')

#Python Functionals

#Map and Lambda Function

cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    list_ = [0, 1]
    break_ = []
    if n == 0:
        return break_
    else:
        x = 0
        y = 1
        for i in range(n):
            z = x + y
            x = y
            y = z
            list_.append(y)
    return list_[:n]

#Regex and Parsing

#Detect Floating Point Number

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input())
for i in range(T):
    str_ = input()
    print(bool(re.search("^[+-]?[0-9]*\.[0-9]+$" , str_)))

#Re.split()

regex_pattern = r"[.,]"	# Do not delete 'r'.

#Group(), Groups() & Groupdict()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()
x = re.search(r"([0-9A-Za-z])\1" , S)
if x:
    print(x.group(1))
else: 
    print(-1)

#Re.findall() & Re.finditer()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input().strip()

res_ = re.findall(r"[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])", S)

if res_:
    print("\n".join(res_))
else:
    print(-1)

#Re.start() & Re.end()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input().strip()
k = input().strip()

res_ = list(re.finditer(r"(?={})".format(k), S))

if res_:
    for ele in res_:
        print((ele.start(), ele.start() - 1 + len(k)))
else:
    print((-1,-1))

#Regex Substitution

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input().strip())

for i in range(N):
    code = input()
    print("".join(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda m: 'and' if m.group() == '&&' else 'or' , code)))

#Validating Roman Numerals

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

#Validating phone numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input().strip())

for i in range(N):
    if re.match("^[7-9][0-9]{9}$",input()):
        print("YES")
    else:
        print("NO")

#Validating and Parsing Email Addresses

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input().strip())
for i in range(n):
    name, email = input().strip().split()
    res_ = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', email)
    if res_:
        print(name, email)

#Hex Color Code

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input().strip())
for i in range(N):
    line = input()
    for hex_ in re.findall(r'(#[0-9a-fA-F]{3,6}){1,2}[^\n ]', line):
        print(hex_)

#HTML Parser - Part 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class myHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ("Start : " + tag)
        for att in attrs:
            print ('->' + " " + att[0] + " " + '>' + " " + str(att[1]))
            
    def handle_endtag(self, tag):
        print ("End   : " + tag)
        
    def handle_startendtag(self, tag, attrs):
        print ("Empty : " + tag)
        for att in attrs:
            print ('->' + " " + att[0] + " " '>' + " " + str(att[1]))
            
myParser = myHTMLParser()

N = int(input().strip())

for i in range(N):
    line_ = input().strip()
    myParser.feed(''.join(line_))

#HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data_):
        if '\n' in data_:
            print(">>> Multi-line Comment" + "\n" + data_)
        
        else:
            print(">>> Single-line Comment" + "\n" + data_)
            
    def handle_data(self, data_):
        if data_ != '\n':
            print(">>> Data" + "\n" + data_)
              
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Detect HTML Tags, Attributes and Attribute Values

# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class myHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for a, b in attrs:
            print("-> " + a + " > " + b)

N = int(input().strip())            
lines_ = []

for i in range(N):
    line_ = input().strip()
    lines_.append(line_)

html = '\n'.join(lines_)
parser = myHTMLParser()
parser.feed(html)

#Validating UID

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input().strip())

for i in range(T):
    code = input().strip()
    if re.match(r"(?!.*(.).*\1)(?=.*\d.*\d.*\d)(?=.*[A-Z].*[A-Z])[A-Za-z0-9]{10,}", code):
        print("Valid")
    else:
        print("Invalid")

#Validating Credit Card Numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input().strip())

for i in range(N):
    num = input().strip()
    if re.search(r"^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$" , num):
        print("Valid")
    else:
        print("Invalid")

#Validating Postal Codes

regex_integer_in_range = r"[1-9][\d]{5}$"    # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"    # Do not delete 'r'.

#Matrix Script

#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

res_ = ''
for row in range(len(matrix[0])):
    for col in range(len(matrix)):
        res_ += matrix[col][row]
        
print(re.sub(r'([a-zA-Z0-9])[!@#$%&) ]+([a-zA-Z0-9])', lambda x: f'{x.group(1)} {x.group(2)}', res_))

#XML

#XML 1 - Find the Score

def get_attr_number(node):
    # your code goes here
    len_ = len(node.attrib)
    sum_ = sum(map(get_attr_number, node))
    return len_ + sum_

#XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    maxdepth = max(level, maxdepth)
    
    for i in elem:
        depth(i, level)

#Closures and Decorators

#Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        # complete the function
        return f(map(lambda i: f"+91 {i[-10:-5]} {i[-5:]}", l))
    return fun

#Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key = lambda i: int(i[2])))
    return inner

#Numpy

#Arrays

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = list(reversed(arr))
    return numpy.array(arr, float)

#Shape and Reshape

import numpy

list_ = input().strip().split()

array_ = numpy.array(list_, int)
array_.shape = (3, 3)
print(array_)

#Transpose and Flatten

import numpy

N, M = map(int, input().split())

res_ = [input().strip().split() for i in range(N)]
    
array_ = numpy.array(res_, int)
print(array_.transpose())
print(array_.flatten())

#Concatenate

import numpy

N, M, P = map(int,input().split())

array_1 = numpy.array([input().split() for n in range(N)], dtype=int)
array_2 = numpy.array([input().split() for m in range(M)], dtype=int)

print(numpy.concatenate((array_1, array_2), axis = 0))

#Zeros and Ones

import numpy

inp_ = tuple(map(int, input().strip().split()))
print(numpy.zeros(inp_, dtype = numpy.int))
print(numpy.ones(inp_, dtype = numpy.int))

#Eye and Identity

import numpy
numpy.set_printoptions(legacy='1.13')

N, M = map(int, input().strip().split())
print(numpy.eye(N, M))

#Array Mathematics

import numpy

N, M = map(int, input().strip().split())

A = [input().strip().split() for i in range(N)]
B = [input().strip().split() for i in range(N)]

A = numpy.array(A, int)
B = numpy.array(B, int)

print(numpy.add(A, B))
print(numpy.subtract(A, B))
print(numpy.multiply(A, B))
print(numpy.floor_divide(A, B))
print(numpy.mod(A, B))
print(numpy.power(A, B))

#Floor, Ceil and Rint

import numpy
numpy.set_printoptions(legacy='1.13')

A = input().strip().split()
A = numpy.array(A, float)

print(numpy.floor(A))
print(numpy.ceil(A))

#rint
print(numpy.rint(A))

#Sum and Prod

import numpy

N, M = map(int, input().strip().split())

array_ =[input().strip().split() for i in range(N)]
array_ = numpy.array(array_, int)

print(numpy.prod(numpy.sum(array_, axis=0)))

#Min and Max

import numpy

N, M = map(int, input().strip().split())

array_ = [input().strip().split() for i in range(N)]
array_ = numpy.array(array_, int)

print(numpy.max(numpy.min(array_, axis=1)))

#Mean, Var, and Std

import numpy

N, M = map(int, input().strip().split())

array_ = [input().strip().split() for i in range(N)]
array_ = numpy.array(array_, float)

print(numpy.mean(array_, axis=1))
print(numpy.var(array_, axis=0))
print(round(numpy.std(array_, axis=None), 11))

#Dot and Cross

import numpy

N = int(input().strip())

A = [input().strip().split() for i in range(N)]
B = [input().strip().split() for i in range(N)]

A = numpy.array(A, int)
B = numpy.array(B, int)

print(numpy.matmul(A, B))

#Inner and Outer

import numpy

A = input().strip().split()
B = input().strip().split()

A = numpy.array(A, int)
B = numpy.array(B, int)

print(numpy.inner(A, B))
print(numpy.outer(A, B))

#Polynomials

import numpy

P = list(map(float, input().strip().split()))
x = float(input().strip())

print(numpy.polyval(P, x))

#Linear Algebra

import numpy
from numpy import linalg

N = int(input().strip())
A = [input().strip().split() for i in range(N)]
A = numpy.array(A, float)

print(round(linalg.det(A), 2))

#Problem 2

#Algorithms

#Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    # Write your code here
    max_ = max(candles)
    count_ = 0
    for i in range(len(candles)):
        if candles[i] == max_:
            count_ += 1
    return count_    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2): 
    if x1 < x2 and v1 < v2: 
        return "NO" 
    elif (v2 - v1) != 0 and (x2 - x1)%(v1 - v2) == 0:
        return "YES"
    else: 
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
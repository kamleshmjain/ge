# take user input using inpute function
  #!/usr/bin/python3
  x=input("enter name: ")
  print(x)
  
  
#Command line args

#!/usr/bin/python3
import sys
print(sys.argv)
print(len(sys.argv))
print(sys.argv[1])


### List ###
#list contains items separated by commas, and enclosed withing the squar bracket

list = ["abc", 786, 2.23, "john"]
print(list)
print(list[0])

#inbuilt functions in list
#len(): return the length of list
>>> list
[1, 2, 3, 4]
>>> len(list)
4  

#startswith
l = ['aa', 'ab', 'aac']
>>> for i in l:
...   if i.startswith('a'):
...     print(i)
...
aa
ab
aac

>>> for i in l:
...   if i.endswith('c'):
...    print(i)
...
aac

#concatenation
>>> list
[1, 2, 3, 4]
>>> list2=[5,6,7,8]
>>> list+list2
[1, 2, 3, 4, 5, 6, 7, 8]

#membership check
>>> 3 in list
True

#iterating over list
>>> for x in list: print(x, end=" ")
...
1 2 3 4 >>>

#append: append the new element to existing list
>>> list
[1, 2, 3, 4]
>>> list.append(5)
>>> list
[1, 2, 3, 4, 5]

#count: shows the count of element>>> list
list = [1, 2, 3, 4, 5, 5]
>>> list.count(5)
2

#index: return the lowest index
list = [1, 2, 3, 4, 5, 5]
>>> list.index(5)
4

#insert: Insert obj in the list at the offset index
>>> list
[1, 2, 3, 4, 5, 5]
>>> list.insert(0,9)
>>> list
[9, 1, 2, 3, 4, 5, 5]

#pop: remove and return the last element from list

>>> list
[9, 1, 2, 3, 4, 5, 5]
>>> list.pop()
5
>>> list
[9, 1, 2, 3, 4, 5]

#Remove: remove the element from list>>> list
[9, 1, 2, 3, 4, 5]
>>> list.remove(9)
>>> list
[1, 2, 3, 4, 5]

#Reverse: reverse the list
>>> list
[1, 2, 3, 4, 5]
>>> list.reverse()
>>> list
[5, 4, 3, 2, 1]

#sort: sort the list
>>> list
[5, 4, 3, 2, 1]
>>> list.sort()
>>> list
[1, 2, 3, 4, 5]
  
### Tuples ###
# This is another sequence data type similar to the list
# Tuple consist of number of values separated by comma and enclosed with paranthesis
# Immutable
tuple = ("abcd", "78", "john")  

### Dictionary ###
# Python dictionary are kind of Hash table, Dictionary are enclosed by curly bracket, 
# Values are accessed by [ ]
dict = {}
dict = {'name': 'John', 'code': 6734, 'dept': 'sales'}
dict['name']

print(dict.keys())   ##this will print Keys
print(dict.values()) ##this will print values

for key, value in dict.items():
    print(key, value)
    

### Python Membership function ####
# In operator - Evaluate to true if value found in sequence
# Not in  - Evaluate to true if variable is not in sequence

a = 10
b = 20
list = [1,2,3,10]

if( a in list ):
   print(f" line 1 - {a} is available in given list")
else:
   print(f" line 2 - {a} is  Not available in given list")    
   
if( b in list):
   print(f" line 3 - {b} is available in given list")
else:
   print(f" line 1 - {b} is Not available in given list") 
   


### Python Identity Operator ###
IS: Evaluate to true if the variable on either side of operator point to same object
isnote: if either side of the operator not pointing to same object


a=10
b=20
if(a is b):
   print(f"{a} & {b} are same")

### Single Statement Suite  ###
var=100
if(var == 100): print(f"value of expression is 100")


### Using else statement with loops:
#python support having an else statement associated with loogs
#if else statement is used with FOR loop, else statement will be executed when the loop exhaused the iterations
#if else statement is used with a while loop, else statement is executed when condition become false.

count = 0
while count < 5:
  print(count, "is less than 5")
  count = count + 1
else:
  print count
  
  
### For loop: the python for loop has ability to iterate over list or string
#syntax:
for statement in sequence:
   statement

  #range() function:
     #Build in function range() is the right function to iterate over the sequence of number
     # It generate an Iterator
     range(5) same as range(0,5) ## this will generate list from 0 to n-1 = 4
     
     for i in range(5):
         print(i)
         
# Using else statement with for loop:
  else statement is used with for loop will be executed only if for loop terminates normally

num = [11,33,55,,39]
for i in num:
   if num%2 == 0:
      print("The list contain an even number")
      break
else:
  print('the list doesnt contain even number')

  
### Loop Control statement:
# Change the execution from normal sequence
# Break statement: Terminate the loop statement transfer the control to statement immidiate following the loop
# Continue statement: Skip the boy of current iteration & go back to next iteration
# PASS: ussed when statement required to be syntactically correct but you dont want to perform any action


### Iterator and Generator
#Iterator is an object which allow programmer to traverse throught all the elements of collection
#In Python iteratory has 2 method iter() & next()

list = [1, 2, 3, 40]
it = iter(list)    # Build an iterator object
print(next(it))    # Print next available element in iterator

#iterator object can be traverse through regular for loop
for x in it:
   print(x, end=" ")

#usintg while loop
while true:
  try:
     print(next(it)) 
  except StopIteration:
     sys.exit()


### Generator: Produce or yield sequence of values using yield method, 
# when generator function called it return generator obj -> when next() function called first time, function statement executed until it reaches the yield statement.

import sys
def fib(n):
    a, b, counter = 0, 1,0
    while true:
       if(counter > n):
          return
       else:
          yield a
          a, b = b, a+b
          counter += 1
          
          
f = fib(5)    # f is iterator obj

while true:
  try:
    print(next(f), end=" ")
  except StopIteration:
    sys.exit()
    
### Number Type Conversion
int(x):   convert x to plain int
long(x):  convert x to long int
float(x): convert x to floating point number

### String ############
#string special operator r
print(r'\n') # this will print \n as string instead of newline 


#'''(Tripal Quotes): This will allow the string to span across multiple line including tab & newline
>>> print(''' this \t is \n line''' )
 this    is
 line

#Capitalize: Capitalize first letter of string
>>> str = "this is string examples ... wow!!"
>>> print(str.capitalize())
This is string examples ... wow!! 
          
          
#Count: shows the count of perticular character
>>> print(str.count('i'))
3

#encode:

#decode:

#endwith:

# find: Determine if str occur in string, return index if found and -1 otherwise
>>> str = "this is string examples ... wow!!"
>>> str2="exam"
>>> print(str.find(str2))
15
>>> str2="exame"
>>> print(str.find(str2))
-1

#isalnum: Return true if string has at lease 1 character or Number and all characters are alphanumeric & false otherwise
>>> str2="this2021"  #without space
>>> print(str2.isalnum())
True

>>> str2="this 2021"  #with space
>>> print(str2.isalnum())
False

#isspace: Return true if string contain only space
>>> str2=" "
>>> print(str2.isspace())
True
>>> str2=""
>>> print(str2.isspace())
False

#join: Concatenate the string representation of element in sequence
>>> s="-"
>>> seq=("a","b","c")
>>> print(s.join(seq))
a-b-c

#len(string): print the lenth of string
>>> print(str)
this is string examples ... wow!!
>>> print(len(str))
33      
  
#replace:
>>> print(str)
this is string examples ... wow!!
>>> print(str.replace('is', 'was'))
thwas was string examples ... wow!!

# split:
>>> str="This is list"
>>> print(str.split())
['This', 'is', 'list']

>>> str="This,is,list"
>>> print(str.split(","))
['This', 'is', 'list']


#Splitlines
>>> str="this is line 1\n this is line2\n"
>>> print(str.splitlines())
['this is line 1', ' this is line2']

#strip: To Remove \n and space from string
>>> str=" hellow"
>>> print(str.strip())
hellow



### Decorator
def to_caps(func):
   def wrapper():
     output = func()
     return output.upper()
   return wrapper
   
@to_caps
def hello_world():
   print("hello, world")


print(hello_world())   
#print(hello_world())this means => to_caps(hello_world())   
   
#################################################################### Python Function ##########################################################################
#block of organized, reusable code that is used to perform a single.

>>> def mystr(str):
...    return str
...
>>> val = mystr("this is arg")
>>> print(val)
this is arg

####Function Argument:
#Required Argument: Are the argument pased to function in correct order, Number of argument should match to the function definition.
#Keywork Argument: When you use keyword args in function call the caller identifies the arguments by parameter name this allows us to skip the arg or place them out of order.
>>> def printme(name, age):
...    print(name, age)
...
>>> printme(age=30, name='kj')
kj 30

#Default Argument: This will take the default value if its not provided 
>>> def printme(name, age=30):
...    print(name, age)
...
>>> printme(name='kj')
kj 30

#variable length argument: you may need to process more args than you specified while defining them
#*(astric) is placed before the variable name that hold the values of all none keyword variable arguments.
#tuple remain empty if no additional arg are specified.

>>> def printinfo(arg1, *vartuple):
...   print(arg1)
...   for var in vartuple:
...      print(var)
...   return
...
>>> printinfo(10)
10
>>> printinfo(10,20,30)
10
20
30

#anonymous function(Lambda function): This is called becase they are not declared in standard manner using def keyword.
#you can use lambda keyworkd to create a small anonymous function
#lambda function take any number of arg but return just one value in the form of expression
#anonymous function can not be a direct call to print bcz lambda require an expression
# lambda function has thier own local namespace and can not accesss other.
>>> sum = lambda x,y:x+y
>>> sum(10,20)
30


#Filter: retrun true element, It takes 2 Args expression, sequence
>>> list(filter(lambda x:x%2==0,range(10)))
[0, 2, 4, 6, 8]

>>> [i for i in range(10) if i%2 == 0]  ##using list comprehension
[0, 2, 4, 6, 8]
>>>

###Python Module
#Module use  to organize your python code.
#grouping related module makes your code easy to understand
kjdevops1@cloudshell:~/python$ cat support.py
def print_fun(val):
    print("Hellow:", val)
    return

kjdevops1@cloudshell:~/python$ python3
>>> import support
>>> support.print_fun("zara")
Hellow: zara
>>>

### Package in python: Hierracal directory structure that define single python application env which consist of all the required module and subpackages.

kjdevops1@cloudshell:~/python/phone$ cat pots.py
def pots():
    print("I'm pots phone")
kjdevops1@cloudshell:~/python/phone$ cat isdn.py
def isdn():
    print("I'm isdn phone")
kjdevops1@cloudshell:~/python/phone$ cat g3.py
def g3():
    print("I'm g3 phone")
kjdevops1@cloudshell:~/python/phone$ cat __init__.py
from pots import pots
from isdn import isdn
from g3 import g3

################################################################# File IO ###############################################################################
#Berfore your read and write you have to open the file using python builtin function open() this function create a file obj. which would be utilize to call either support method associated with it.

syntax. fileobj = open(file_name [accessMode])
access Modes:
r  - read Only
rb - readonly(binary)  
r+ - read&Write
rb+ - readwrite (binary)
w - write only
w+ - write & reada 
a - appending
a+ - appending & reading

default funciton:
file.closed - Return true if file closed
file.mode - Return accesss mode
file.name - Return Name of file

kjdevops1@cloudshell:~$ cat first.txt
firstnm lastnm
kamlesh jain
Rahul   chogle

>>> fo=open("first.txt", "r+")
>>> str = fo.readlines()
>>> print(str)
['firstnm\tlastnm\n', 'kamlesh\tjain\n', 'Rahul\tchogle\n']
   
  
>>> fo=open("first.txt", "r")
>>> for index in range(4):
...   line = next(fo)
...   print(f"line no {index} - {line}")
...
line no 0 - firstnm     lastnm

line no 1 - kamlesh     jain

line no 2 - Rahul       chogle   


##Seek: set the file current position at the offset, where as its optional and default to 
#0 - Means absolute file position 
#1 - Means seek relative to current position
#2 - means seek relative to file end.

eg. fo.seek(0,0) - sets the pointer to begining 

#write:
>>> fo=open("first.txt", 'r+')
>>> str = "This is latest line"
>>> fo.seek(0,2)   #set the pointer to End of file
41
>>> line = fo.write(str)
>>> fo.seek(0,0)   #set the pointer to begining
0
>>> for index in range(4):
...    line = next(fo)
...    print(line)
...
firstnm lastnm
kamlesh jain
Rahul   chogle
This is latest line


################## OS file/Dir method
*os.chdir(path)          # change the director to path
os.chmod()              # change the file permission
*os.getcwd()             # Return the CWD
os.chown()              # 
os.link(src,dst)        # create the hard link pointing to src named dst
os.listdir()            # return the list containing the names of the entries in the directory given by path
*os.makedirs()           # REcurring dir creation funciton
os.readlink(dst)        # Return the string path to which the symlink is pointing
os.remove()             # remove the file path, If path is not found then OSError will be raised
os.removedirs(path)     # Remove dirs recuresively
os.rename()             # Rename the file or dir from src to dest


#eg:
path = "/tmp/mydir/newdir"
os.makedirs(path, 0755)

#below code will print all files names in dir
>>> import os, sys
>>> dirs = os.listdir()
>>> for files in dirs:
...   print(files)
...
cmd.py
input.py
support.py
test.py
phone

############################################################# Exception Handling #############################################################
# An exception is an event that occur when the normal flow gets disrupted, we must either handle the exception immidiately otherwise it will terminates & quits.

StopIteration
IoError
ZeroDivisionError
SystemExit

############################################################# Class in Python #############################################################
#user defined prototype that has set of attribute like variable, method


#!/usr/bin/python3

class Emp:
  empCount = 0
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Emp.empCount += 1

  def displaycount(self):
    print("total emp %d" %Emp.empCount)

  def display(self):
    print("Name:", self.name)
    print("Salary:", self.salary)

emp1 = Emp("KJ", 20000)
emp2 = Emp("RJ", 30000)

emp1.display()
emp2.display()
print("Total Emp %d" %Emp.empCount)


#### List comprehension
#creating list from onother list
syntax: [ action for i in list]

>>> [ i+1 for i in range(5)]
[1, 2, 3, 4, 5]

>>> [i*i for i in range(5)]
[0, 1, 4, 9, 16]

>>> [ i*i for i in range(5)]
[0, 1, 4, 9, 16]

#Print even number using list comprehension
>>> def print_even(list):
...    return [num for num in list if num%2 == 0 ]

>>> print_even(range(10))
[0, 2, 4, 6, 8]

#Print the file content using list comprehension
>>> print([line for line in open("test")])
['this is new line added']


#Reverse word
>>> str="kamlesh"
>>> print(str[::-1])


#How to convert a list into a string?
weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsString = ' '.join(weekdays)
print(listAsString)

#How to convert a list into a tuple?: By using Python <tuple()> function we can convert a list into a tuple. But we can’t change the list after turning it into tuple, because it becomes immutable.
weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsTuple = tuple(weekdays)
print(listAsTuple)

#How to convert a list into a set?
>>> weekdays = ['sun','mon','tue','wed','thu','fri','sat','sun','tue']
>>> listAsSet = set(weekdays)
>>> print(listAsSet)
set(['wed', 'sun', 'thu', 'tue', 'mon', 'fri', 'sat'])

#How to count the occurrences of a particular element in the list?
>>> weekdays = ['sun','mon','tue','wed','thu','fri','sat','sun','tue']
>>> print([[x, weekdays.count(x)] for x in set(weekdays)])
[['wed', 1], ['sun', 2], ['thu', 1], ['tue', 2], ['mon', 1], ['fri', 1], ['sat', 1]]

#What is NumPy array?
A) NumPy arrays are more flexible then lists in Python. By using NumPy arrays reading and writing items is faster and more efficient.

#What is a negative index in Python?
Python has a special feature like a negative index in Arrays and Lists. Positive index reads the elements from the starting of an array or list but in the negative index, Python reads elements from the end of an array or list.

>> import array
>>> a = [1, 2, 3]
>>> print a[-3]
>>> print a[-2]
>>> print a[-1]

#What is the output of the below program?
>>>names = ['Chris', 'Jack', 'John', 'Daman']
>>>print(names[-1][-1])
The output is: n

#What is Enumerate() Function in Python?
The Python enumerate() function adds a counter to an iterable object. enumerate() function can accept sequential indexes starting from zero.
weekdays = ['sun', 'mon', 'tue']
>>> for i, day in enumerate(weekdays):
...   print(i, day)
...
(0, 'sun')
(1, 'mon')
(2, 'tue')

#Python Concatenating Example:
>>> var="kamlesh"
>>> var2="jain"
>>> print(var+" "+var2)
kamlesh jain

#How to print the sum of the numbers starting from 1 to 100?
print sum(range(1,101))

#19) What is the output, Suppose list1 is [1, 3, 2], What is list1 * 2?
A) [1, 3, 2, 1, 3, 2]

#20) What is the output when we execute list(“hello”)?
A) [‘h’, ‘e’, ‘l’, ‘l’, ‘o’]

#Can you write a program to find the average of numbers in a list in Python?
#!/usr/bin/python3

n=int(input("Enter number:"))
a=[]
for i in range(0,n):
    element = int(input("Enter Element:"))
    a.append(element)
    avg=sum(a)/n
print("Average of Element is {}".format(round(avg,2)))

#### output #########
kjdevops1@cloudshell:~/python$ ./avg.py 
Enter number:3
Enter Element:1
Enter Element:2
Enter Element:3
Average of Element is 2.0


#Write a program to reverse a number in Python?
#!/usr/bin/python3
n=int(input("Enter Number:"))
rev=0
while n>0:
    rem = n%10
    rev = rev*10 + rem
    n = n//10
print("Reverse of number {}".format(rev))

kjdevops1@cloudshell:~/python$ ./reverse.py 
Enter Number:123
Reverse of number 321

#Write a program to find the sum of the digits of a number in Python?
#!/usr/bin/python3
n = int(input("Enter Number:"))
total=0
while n>0:
    rem = n%10
    total = total + rem
    n = n//10
print("Total of Given number {}".format(total))

kjdevops1@cloudshell:~/python$ ./total.py 
Enter Number:123
Total of Given number 6

#Write a Python Program to Check if a Number is a Palindrome or not?
#!/usr/bin/python3
n = int(input("Enter Num:"))
temp = n
rev = 0
while n>0:
    rem=n%10
    rev = rev*10+rem
    n=n//10
if(temp == rev):
    print("The Given Number is Pallindrome")
else:
    print("The Given Number is not Pallindrome")
    
kjdevops1@cloudshell:~/python$ ./palindrom.py
Enter Num:121
The Given Number is Pallindrome

#Write a Python Program to Count the Number of Digits in a Number?
#!/usr/bin/python3
n=int(input("Please Enter number"))
count=0
while n>0:
    rem = n%10
    count+=1
    n=n//10
print(count)

kjdevops1@cloudshell:~/python$ ./count_digit.py
Please Enter number: 1234
4

#Write a Python Program to Print Table of a Given Number?
#!/usr/bin/python3
n=int(input("Enter Number: "))
for i in range(1,11):
    print(n,"*", i, ": ", n*i)
    
kjdevops1@cloudshell:~/python$ ./table.py 
Enter Number: 5
5 * 1 :  5
5 * 2 :  10
5 * 3 :  15
5 * 4 :  20
5 * 5 :  25
5 * 6 :  30
5 * 7 :  35
5 * 8 :  40
5 * 9 :  45
5 * 10 :  50

#Write a Python Program to Check if a Number is a Prime Number?
#!/usr/bin/python3
n = int(input("Enter Number: "))
if(n%n == 0) and (n%2 == 0):
    print("{} is Prime".format(n))
else:
    print("{} is not Prime".format(n))
    
kjdevops1@cloudshell:~/python$ ./prime.py 
Enter Number: 12
12 is Prime
kjdevops1@cloudshell:~/python$ ./prime.py
Enter Number: 5
5 is not Prime

# to capitalize each letter using Map function
>>> list = ["kamlesh", "jain"]
>>> lst_up = map(str.upper, list)
>>> print(lst_up)
<map object at 0x7f8791eab9a0>
>>> print(list(lst_up))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable

#Unpack lst_up into list
>>> names_ucase = [*lst_up]
>>> names_ucase
['KAMLESH', 'JAIN']

#Write a Python Program to Check if a Number is an Armstrong Number?:  a number that is equal to the sum of the cubes of its own digits. For example, 370 is an Armstrong number since 370 = 3*3*3 + 7*7*7 + 0*0*0 .
#!/usr/bin/python3
n=int(input("Enter Number: "))
a = list(map(int, str(n)))
b = list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("The Number is Armstrong number")
else:
    print("The Number is not Armstrong number")
    
kjdevops1@cloudshell:~/python$ ./amstrong.py 
Enter Number: 370
The Number is Armstrong number

#Write a Python Program to Check if a Number is a Perfect Number?
#perfect number, a positive integer that is equal to the sum of its proper divisors. The smallest perfect number is 6, which is the sum of 1, 2, and 3.
#!/usr/bin/python3
n=int(input("Enter Number: "))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(sum == n):
  print("{} is perfect number".format(n))
else:
  print("{} is not perfect number".format(n))

kjdevops1@cloudshell:~/python$ ./perfect.py 
Enter Number: 6
6 is not perfect number
kjdevops1@cloudshell:~/python$ ./perfect.py
Enter Number: 7

#Write a Python Program to Find the Second Largest Number in a List?
#!/usr/bin/python3
n=int(input("Enter Num: "))
a = []
for i in range(1,n+1):
    ele = int(input("enter element: "))
    a.append(ele)
    a.sort()
print("second Largest element is {}",a[n-2])

kjdevops1@cloudshell:~/python$ ./find_second_large.py 
Enter Num: 4
enter element: 77
enter element: 45
enter element: 89
enter element: 22
second Largest element is {} 77

#Write a Python Program to Swap the First and Last Value of a List?
#!/usr/bin/python3
n=int(input("Enter Number: "))
a = []
for i in range(1,n+1):
    ele = int(input("Enter Element "+ str(i) + ":" ))
    a.append(ele)
    print("Current list", a)

temp = a[0]
a[0] = a[n-1]
a[n-1] = temp

print("New List", a)

Current list [4, 2, 3, 1]
New List [1, 2, 3, 4]

#Write a Python Program to Check if a String is a Palindrome or Not?
string=raw_input("Enter string:")
if(string==string[::-1]):
    print("The string is a palindrome")
else:
    print("The string isn't a palindrome")  

#check number is palindrome using recursion
n = int(input("please give a number : "))

def reverse(num):
    if num<10:
      return num 
    else:
      return int(str(num%10) + str(reverse(num//10)))

def isPalindrome(num):
    if num == reverse(num):
        return 1
    return 0
if isPalindrome(n) == 1:
    print("Given number is a palindrome")
else:
    print("Given number is a not palindrome") 
    

#Write a Python Program to Count the Number of Vowels in a String?
#!/usr/bin/python3
input=input("Enter String: ")
vowels = 0
for i in input:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        vowels +=1  

print(vowels)

kjdevops1@cloudshell:~/python$ ./find_vowals.py
Enter String: kamlesh
2

#Write a Python Program to Check Common Letters in Two Input Strings?
#!/usr/bin/python3
s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
  print(i)


kjdevops1@cloudshell:~/python$ ./check_common.py
Enter first string:Hello 
Enter second string:How are you
The common letters are:
o
e
H

#Python program to print Fibonacci series program in using Iterative methods
#!/usr/bin/python3
first, second = 0,1
n=int(input("Please Enter Number: "))
for i in range(0,n):
    if i<=1:
       result = i
    else:
       result = first + second
       first = second
       second = result
    print(result)

kjdevops1@cloudshell:~/python$ ./fibo.py 
Please Enter Number: 5     
0
1
1
2
3

#Python program to swap two number without using third variable
a = int(input("please give first number a: "))
b = int(input("please give second number b: "))
a=a-b
b=a+b
a=b-a
print("After swapping")
print("value of a is : ", a);
print("value of b is : ", b); 

#Python Code to calculate the factorial
#taking an integer input from user
num=int(input("Enter the whole number to find the factorial: "))
factorial = 1
if num < 0:
   	print("Factorial can't be calculated for negative number")
elif num == 0:
   print("Factorial of 0 is 1")
else:
#calculating the factorial of the input number
for i in range(1,num + 1):
  factorial = factorial*i
print("Factorial of",num,"is",factorial)

#Factorial using recurison

def fact(n):  
   if n == 1:  
       return n  
   else:  
#recursion 
       return n*fact(n-1)

num = int(input("Enter a whole number to find Factorial: "))  
if num < 0:  
   print("Factorial can't be calculated for negative number")  
elif num == 0:  
   print("Factorial of 0 is 1")  
else:  
   print("Factorial of",num,"is",fact(num))  


#Remove character from string in Python
str = input("please enter a string : ")
ch = input("please enter a character : ")
print(str.replace(ch," ")) 

#Python Program to count the occurrence of given character in a string.
string = input("Please enter String : ")
char = input("Please enter a Character : ")
count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
print("Total Number of occurence of ", char, "is :" , count)

#Python code to replace the string space with given character
#taking input from the user
string = input("Enter a String : ")
result = ''  #empty string
ch = input("Enter a Character : ")
for i in string:  #iterating using for loop
        if i == ' ':  #if any space found in the string
            i = ch   #replacing space with character
        result += i   #concatenating each character of the string without space
print(“String after removing space with t = ”,result)

#Python code to convert lowercase character to uppercase character of string
string = input("Enter a String : ")
result=''
for i in string:  #iterate through each letter/character from the string
        if i.islower():  #if lowercase
            i = i.upper() #converting lowercase into uppercase letter
        result += i #concatenating each character of the string without lowercase letter 
print("String after converting lower case to upper :",result)

#Python code to remove vowels from the string
#taking the input string from the user
string = input("Enter a String : ") 
result=''
for i in string:  
#iterating through each character of the string
    if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):  
     #seaching for vowels
        i = ''  
#if vowel found replace it with empty string
    result += i 
    #concatenate rest of the string
print("String after removing the vowels :",result)

#Remove Space from string
>>> string="This is Home"
>>> result=""
>>> for i in string:
...   if i!=" ":
...      result+=i
...
>>> print(result)
ThisisHome

#Python code to concatenate two string using join() function

#taking inputs from the user
str1 = input('Enter first string: ')
str2 = input('Enter second string: ')
#printing the output after using join() method
print("String after concatenation :","".join([str1, str2]))

#Remove repeated characters from string
def removeDuplicate(str):
	s=set(str)
	s="".join(s)
	print("Without Order:",s)
	
    t=""
	for i in str:
		if(i in t):
			pass
		else:
			t=t+i
		print("With Order:",t)
	
str="geeksforgeeks"
removeDuplicate(str)



#Python code to find sum of integers in the string
str1 = input('Enter a string: ')
sum=0
for i in string:
	#if character is a digit
    if i.isdigit():
		#taking sum of integral digits present in the string 
        sum=sum+int(i)
print("sum=",sum)


#Python code to find all non repeating characters in the string
#taking input from the user
str1 = input('Enter a string: ')
result=""
#iterating the characters of string
for i in str1:
    count = 0
    #another loop inside loop
    for j in str1:
	    if i == j:
	        count=count+1
	        if count > 1:
	            break
	        if count == 1:
	            result+=i
print("non repeating character =", result)

#Python code to sort string character in ascending order
#taking input from the user
string = input("Enter the string : ")
#converting string into list of its characters
strList=list(string) 
#sorting elements of list
sortedString=''.join(sorted(strList)) 
print("String Sorted in ascending order :", sortedString)


#Python program to sort string in descending order
#taking input from the user
string = input("Enter the string : ")
#converting string into list of its characters
strList=list(string) 
#sorting elements of list in reverse order by making ‘reverse = True’
sortedString=''.join(sorted(strList, reverse =True)) 
print("String Sorted in ascending order :", sortedString)

#Python Program to find largest and smallest number in an array
arr = []
n = int(input("enter size of array : "))
for x in range(n):
    x=int(input("enter element of array : "))
    arr.append(x)
largest = arr[0]
smallest = arr[0]
for i in range(n):
    if arr[i]>largest:
        largest = arr[i]
    if arr[i]<smallest:
        smallest = arr[i]
        
print(f"largest element in array is {largest}")
print(f"smallest element in array is {smallest}") 

#Python Program to Insert element at given location in array(list)
# given array (list)
arr = [1, 2, 3, 4, 5]
num=int(input("Enter a number to insert in array : "))
index=int(input("Enter a index to insert value : "))
if index >= len(arr):
    print("please enter index smaller than",len(arr))
else:
    # insering element ‘num’ at ‘index’ position
    arr.insert(index, num)  
print("Array after inserting",num,"=",arr)


#Python code to delete a given element of an array(list)
#taking input to fix the size of the array
size=int(input("Enter the number of elements you want in array: "))
arr=[]
# adding elements to the array
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
num=int(input("Enter a number to remove from array : "))
# removing element ‘num’ from the array.
arr.remove(num)
print("Array after removing",num,"=",arr)


##Python code to delete element from array at given index

#Python code to perform right rotation on array (list) elements by two positions        #https://quescol.com/interview-preparation/python-right-rotation
#taking the input from the user to fix the array size

def rightRotate(lists, num):
    output_list = []
 
    # Will add values from n to the new list
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])
 
    # Will add the values before
    # n to the end of new list
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])
 
    return output_list
 
 
# Driver Code
rotate_num = 3
list_1 = [1, 2, 3, 4, 5, 6]
 
print(rightRotate(list_1, rotate_num))

#another way
# Python program to right rotate
# a list by n using list slicing
n = 3
 
list_1 = [1, 2, 3, 4, 5, 6]
list_1 = (list_1[len(list_1) - n:len(list_1)]
                 + list_1[0:len(list_1) - n])
print(list_1)


## Python way to rotate list
https://www.geeksforgeeks.org/python-ways-to-rotate-a-list/?ref=lbp

Method #1 : Using Slicing
This particular method is the generic method and mostly employed to achieve this task and also been discussed in many articles as well. It works by just joining the later sliced part to the initial sliced part given the rotation number.


# Python3 code to demonstrate 
# rotation of list 
# using slice 
  
# initializing list
test_list = [1, 4, 6, 7, 2]
  
# printing original list 
print ("Original list : " + str(test_list))
  
# using slicing to left rotate by 3
test_list = test_list[3:] + test_list[:3]
  
# Printing list after left rotate
print ("List after left rotate by 3 : " + str(test_list))
  
# using slicing to right rotate by 3
# back to Original
test_list = test_list[-3:] + test_list[:-3]
  
# Printing after right rotate
print ("List after right rotate by 3(back to original) : "
                                         + str(test_list))
Output:
Original list : [1, 4, 6, 7, 2]
List after left rotate by 3 : [7, 2, 1, 4, 6]
List after right rotate by 3 ( back to original) : [1, 4, 6, 7, 2]
 
Method #2 : Using list Comprehension
This problem can also be solved by naive method, but its shorter implementation would be with the help of list comprehension. In this method, we just reassign the index to each value to specific position after rotation.


# Python3 code to demonstrate 
# rotation of list 
# using list comprehension
  
# initializing list
test_list = [1, 4, 6, 7, 2]
  
# printing original list 
print ("Original list : " + str(test_list))
  
# using list comprehension to left rotate by 3
test_list = [test_list[(i + 3) % len(test_list)]
               for i, x in enumerate(test_list)]
  
# Printing list after left rotate
print ("List after left rotate by 3 : " + str(test_list))
  
# using list comprehension to right rotate by 3
# back to Original
test_list = [test_list[(i - 3) % len(test_list)]
               for i, x in enumerate(test_list)]
  
# Printing after right rotate
print ("List after right rotate by 3(back to original) : " 
                                        + str(test_list))
Output:
Original list : [1, 4, 6, 7, 2]
List after left rotate by 3 : [7, 2, 1, 4, 6]
List after right rotate by 3(back to original) : [1, 4, 6, 7, 2]


################################## REGEX ########################################################################################
>>> str="cats are smarted then dogs"
>>> import re

>>> val=re.match(r'(.*) are (.*?) .*', str)

>>> val.group()
'cats are smarted then dogs'

>>> val.group(1)
'cats'

>>> val.group(2)
'smarted'

#search
>>> val=re.search(r'(.*) are (.*?) .*', str)
>>> val.group()
'cats are smarted then dogs'

>>> val.group(1)
'cats'

>>> val.group(2)
'smarted'

#Match vs Search
>>> val=re.search(r'dogs', str)
>>> val
<re.Match object; span=(22, 26), match='dogs'>

>>> val=re.match(r'dogs', str)    ## Match only check for match at beginning of the string where as seach check for match anywhere in the string
>>> val    #match evaluate at beginning of string only


## Replace entire comment from starting from # till end
>>> phone = "2004-959-559#this is phone number"
>>> re.sub(r'#.*', "", phone)
'2004-959-559'

>>> re.sub(r'\D+', "", phone)
'2004959559'

## find all the pattern matching string
>>> str="cats are smarted then dogs and dogs are faster"
>>> re.findall(r'dogs', str)
['dogs', 'dogs']

#find all string containing user followed by digit
>>> str="THe winners are: user9, userN, user8"
>>> re.findall(r'user\d', str)
['user9', 'user8']

#\D - Non digit
>>> re.findall(r'user\D', str)
['userN']

#\w - words
>>> re.findall(r'user\w', str)
['user9', 'userN', 'user8']

#Repeated Character
>>> str = "Password1234"
>>> re.search(r'\w{8}\d{4}', str)
<re.Match object; span=(0, 12), match='Password1234'>

#+ One or more
>>> str = "Date of start: 4-3 Date of registration:10-14"
>>> re.findall(r'\d+-\d+', str)
['4-3', '10-14']

#Search at beginning
>>> str="the 80s movie was better than the 90s"
>>> re.findall(r'^the\s\d+s', str)
['the 80s']

#search at the end
>>> str="the 80s movie was better than the 90s"
>>> re.findall(r'the\s\d+s$', str)
['the 90s']

##look ahead positive(?=sat), negative(?!run)
#files followed by tranfered
>>> str="tweet.txt transfered mypass.txt transfered, keyword.txt Error"
>>> re.findall(r'\w+\.txt(?=\stransfered)', str)
['tweet.txt', 'mypass.txt']

#find files that are followed by string other than transfered
>>> re.findall(r'\w+\.txt(?!\stransfered)', str)
['keyword.txt']



##look Behind   positive(?<=string)  negative(?<!string)
#Q: find user with member role
>>> str="member: Angus Yung, member: Kamlesh Jain, owner: Rahul raj"
>>> re.findall(r'(?<=member:)\s\w+\s\w+', str)
[' Angus Yung', ' Kamlesh Jain']

#Negative:
>>> re.findall(r'(?<!member:)\s\w+\s\w+', str)
[' Rahul raj']


## Inheritance
#!/usr/bin/python3
class Parent:
    def __init__(self):
        pass

    def parentmethod(self):
        print("Msg from Parent function")

class Child(Parent):
    def __init__(self):
        pass

    def childmethod(self):
        print("Msg from Child function")


shanu = Child()
shanu.childmethod()
shanu.parentmethod()

kjgcppractice@cloudshell:~ (main-aspect-345314)$ ./inheritance.py
Msg from Child function
Msg from Parent function



#################################### link list #####################################################################################
#Singly linked list: Create and Traverse Python Program
#Creating node class of the singly linked list  
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
#Creating addNode() to add newly created nodes.
    def addNode(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

 #Creating display() to print newly created nodes via traversing.
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
 
s = SinglyLinkedList()
n = int(input('enter the number of elements in linked list : '))
for i in range(n):
    data = int(input('Enter data: '))
    s.addNode(data)
print('The linked list: ', end = '')
s.display()

#Python program to insert a node in linked list
def pushAtLocation(self, newElement, position):
	#create a new node from the new element
	newNode = Node(newElement)
	if(position<1):
		print(“position should be greater than 1”)
	elif( position ==1):
	#add element at the beginning
		newNode.next = self.head
		self.head = newNode
	else:
	#create a ‘temp’ variable to traverse to the node previous to input position
		temp = self.head
		for i in range(1, position-1):
			if(temp!=Node):
				temp=temp.next

	# if previous node is not null
	if(temp!=None):
		newNode.next = temp.next
		temp.next = newNode
	else:
		# if previous node is null
		print(“previous node is null”)    
        
#Python program to reverse the singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class SinglyLinkedList:

    def __init__(self):
        self.head = None
 
    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
 
    # Function to add element at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # to show the elements of the linked list
    def show(self):
        temp = self.head
        while(temp):
            print (temp.data,end=" ")
            temp = temp.next
 
 

s = SinglyLinkedList()
print("Press 1 to add the element in the list : ")
print("Press 0 to stop adding the element in the list : ")
n=10

while(n!=0):
    n=int(input("Enter your choice: "))
    if(n==1):
        s.push(input("Enter the element to add in linked list : "))
    elif(n==0):
        break
    else:
        print("[INVALID INPUT]: try again")
        continue

print("Given linked list (Original Linked list) : ")
s.show()
s.reverse()
print("\nReversed linked list : ")
s.show()


#Python Program to Search an element in Singly linked list
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#creating linked list class
class SinglyLinkedList:
  def __init__(self):
    self.head = None

  #Adding new element at the end of the list
  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode

  #Searching the element
  def Search(self, ele):
    temp = self.head
    found = 0
    i = 0 

    if(temp != None):
      while (temp != None):
        i += 1
        if(temp.data == ele):
          found += 1
          break
        temp = temp.next
      if(found == 1):
        print(ele,"is found at position =", i)
      else:
        print(ele,"is not found in the given linked list.")
    else:
      print("The list is empty.")

  #to display the elements of the list
  def show(self):
    temp = self.head
    if(temp != None):
      print("The list elements are:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

                 
s = SinglyLinkedList()

print("press 1 to add element to the linked list")
print("press 0 to stop adding the element to the list")
n=10
#Add elements into the linkedlist.
while(n!=0):
    print("press 1 to add element to the linked list")
    print("press 0 to stop adding the element to the list")
    n=int(input("Enter your choice : "))
    if(n==1):
        s.push_back(int(input("Enter element to add : ")))

    elif(n==0):
        break
    else:
        print("[INVALID INPUT]: try again")
        continue
#display the elements of the list.
key = int(input("enter the element to search  into the linked list"))

s.show()
#searching the element in the list
s.Search(key)

#Linked list Deletion in Python: At beginning, End, Given location
def pop_at(self, position):     
  
  #1. check if the position is > 0
  if(position < 1):
    print("\nposition should be >= 1.")
  elif (position == 1 and self.head != None):
    
    #2. if the position is 1 and head is not null, make
    #   head next as head and delete previous head 
    nodeToDelete = self.head
    self.head = self.head.next
    nodeToDelete = None
  else:    
    
    #3. Else, make a temp node and traverse to the 
    #   node previous to the position
    temp = self.head
    for i in range(1, position-1):
      if(temp != None):
        temp = temp.next   
    
    #4. If the previous node and next of the previous  
    #   is not null, adjust links 
    if(temp != None and temp.next != None):
      nodeToDelete = temp.next
      temp.next = temp.next.next
      nodeToDelete = None 
    else:
      
      #5. Else the given node will be empty.
      print("\nThe node is already null.")


#Selection Sort - [3,1,2,0]
>>> a
[3, 1, 2, 0]
>>> for i in range(len(a)):
...   min = i
...   for j in range(i+1, len(a)):
...     if(a[min] > a[j]):
...       min = j
...   a[i], a[min] = a[min], a[i]
...
>>> a
[0, 1, 2, 3]

#twosum algo
kjdevops1@cloudshell:~/python (my-k8s-workload)$ cat twosum.py
#!/usr/bin/python3
nums=int(input("Enter number"))
arr=[]
for i in range(nums):
    val=int(input("Please pass the input"))
    arr.append(val)

result=9
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        total=0
        total=arr[i]+arr[j]
        if total == result:
            print(i,j)




#link list problems - https://www.alphacodingskills.com/python/ds/python-insert-a-new-node-at-a-given-position-in-the-linked-list.php#:~:text=In%20this%20method%2C%20a%20new,%2D%3E20%2D%3E30
#Interview Questions: https://www.codinginterview.com/google-interview-questions
https://www.educative.io/blog/google-coding-interview

#75 leet code problems and solution video: https://docs.google.com/spreadsheets/d/1A2PaQKcdwO_lwxz9bAnxXnIQayCouZP6d-ENrBz_NXc/edit#gid=0


#=======================================        Link List Operation  =================================================================#
##Traverse
def PrintList(self):
  
  #1. create a temp node pointing to head
  temp = self.head
  
  #2. if the temp node is not null continue 
  #   displaying the content and move to the 
  #   next ode till the temp becomes null
  if(temp != None):
    print("The list contains:", end=" ")
    while (temp != None):
      print(temp.data, end=" ")
      temp = temp.next
    print()
  else:
    
    #3. If the temp node is null at the start, 
    #   the list is empty
    print("The list is empty.")
    
####### Insert a Node at Start
def push_front(self, newElement):
  
  #1 & 2. allocate a new node
  #       and assign data element
  newNode = Node(newElement)
  
  #3. make next node of new node as head
  newNode.next = self.head
  
  #4. make new node as head 
  self.head = newNode     
  
#########  Insert Node at the end
def push_back(self, newElement):
  
  #1 & 2 & 3. allocate node, assign data element
  #          assign null to the next of new node
  newNode = Node(newElement)
  
  #4. Check the Linked List is empty or not,
  #   if empty make the new node as head 
  if(self.head == None):
    self.head = newNode
    return
  else:
    
    #5. Else, traverse to the last node
    temp = self.head
    while(temp.next != None):
      temp = temp.next
    
    #6. Change the next of last node to new node  
    temp.next = newNode


###### Insert New Node at given position
def push_at(self, newElement, position):     
  
  #1. allocate node to new element
  newNode = Node(newElement)

  #2. check if the position is > 0 
  if(position < 1):
    print("\nposition should be >= 1.")
  elif (position == 1):
    
    #3. if the position is 1, make next of the
    #   new node as head and new node as head
    newNode.next = self.head
    self.head = newNode
  else:    
    
    #4. Else, make a temp node and traverse to the 
    #   node previous to the position
    temp = self.head
    for i in range(1, position-1):
      if(temp != None):
        temp = temp.next   
    
    #5. If the previous node is not null, make 
    #   newNode next as temp next and temp next 
    #   as newNode.
    if(temp != None):
      newNode.next = temp.next
      temp.next = newNode  
    else:
      
      #6. When the previous node is null
      print("\nThe previous node is null.")  

#### Delete First Node
def pop_front(self):
  if(self.head != None):
    
    #1. if head is not null, create a
    #   temp node pointing to head
    temp = self.head
    
    #2. move head to next of head
    self.head = self.head.next 
    
    #3. delete temp node
    temp = None 

#### Delete Last Node
def pop_back(self):
  if(self.head != None):
    
    #1. if head in not null and next of head
    #   is null, release the head
    if(self.head.next == None):
      self.head = None
    else:
      
      #2. Else, traverse to the second last 
      #   element of the list
      temp = self.head
      while(temp.next.next != None):
        temp = temp.next
      
      #3. Change the next of the second 
      #   last node to null and delete the
      #   last node
      lastNode = temp.next
      temp.next = None
      lastNode = None

#### Delete node at given position

def pop_at(self, position):     
  
  #1. check if the position is > 0
  if(position < 1):
    print("\nposition should be >= 1.")
  elif (position == 1 and self.head != None):
    
    #2. if the position is 1 and head is not null, make
    #   head next as head and delete previous head 
    nodeToDelete = self.head
    self.head = self.head.next
    nodeToDelete = None
  else:    
    
    #3. Else, make a temp node and traverse to the 
    #   node previous to the position
    temp = self.head
    for i in range(1, position-1):
      if(temp != None):
        temp = temp.next   
    
    #4. If the previous node and next of the previous  
    #   is not null, adjust links 
    if(temp != None and temp.next != None):
      nodeToDelete = temp.next
      temp.next = temp.next.next
      nodeToDelete = None 
    else:
      
      #5. Else the given node will be empty.
      print("\nThe node is already null.")

      
#### Delete All Nodes
def deleteAllNodes(self):

  #1 & 2. create a temp node, if the head is not  
  #   null make temp as head and move head to head 
  #   next, then delete the temp, continue the 
  #   process till head becomes null
  while (self.head != None):
    temp = self.head
    self.head = self.head.next
    temp = None

  print("All nodes are deleted successfully.")  
  

#### Count Nodes
def countNodes(self):
  
  #1. create a temp node pointing to head
  temp = self.head
  
  #2. create a variable to count nodes
  i = 0

  #3. if the temp node is not null increase 
  #   i by 1 and move to the next node, repeat
  #   the process till the temp becomes null
  while (temp != None):
    i += 1
    temp = temp.next

  #4. return the count
  return i    

#### Delete Even Nodes
def deleteEvenNodes(self):  
  if (self.head != None):
    #1. if head is not null create nodes -
    #   evenNode and oddNode
    oddNode = self.head
    evenNode = self.head.next 

    while(oddNode != None and evenNode != None):
      
      #2. while oddNode and evenNode are not null
      #   make next of oddNode as next of evenNode
      #   and free evenNode   
      oddNode.next = evenNode.next
      evenNode = None

      #3. and make oddNode as next of oddNode
      oddNode = oddNode.next
      
      #4. Update oddNode and evenNode
      if(oddNode != None):
        evenNode = oddNode.next


#### Delete Odd Nodes
def deleteOddNodes(self):  
  if (self.head != None):
    
    #1. if head is not null, make next of head as
    #   new head and delete previous head
    temp = self.head
    self.head = self.head.next
    temp = None
    if (self.head != None):
      
      #2. if the new head is not null create 
      #   nodes - evenNode and oddNode
      evenNode = self.head
      oddNode = self.head.next 

      while(evenNode != None and oddNode != None):
        
        #3. while evenNode and oddNode are not null
        #   make next of evenNode as next of oddNode
        #   and free oddNode   
        evenNode.next = oddNode.next
        oddNode = None

        #4. and make evenNode as next of evenNode
        evenNode = evenNode.next
        
        #5. Update evenNode and oddNode
        if(evenNode != None):
          oddNode = evenNode.next

#### Search Element in linked list
def SearchElement(self, searchValue):
  #1. create a temp node pointing to head
  temp = self.head
  
  #2. create two variables: found - to track
  #   search, idx - to track current index
  found = 0
  i = 0 

  #3. if the temp node is not null check the
  #   node value with searchValue, if found 
  #   update variables and break the loop, else
  #   continue searching till temp node is null
  if(temp != None):
    while (temp != None):
      i += 1
      if(temp.data == searchValue):
        found += 1
        break
      temp = temp.next
    if(found == 1):
      print(searchValue,"is found at index =", i)
    else:
      print(searchValue,"is not found in the list.")
  else:
    
    #4. If the temp node is null at the start, 
    #   the list is empty
    print("The list is empty.")

##### Delete First Node by Key
def pop_first(self, key):     
  
  temp = self.head
  #1. check if the head is not null
  if(temp != None):
    
    #2. if head is not null and value stored at head
    #   is equal to the key, make head next as head
    #   and delete previous head
    if(temp.data == key):
      nodeToDelete = self.head
      self.head = self.head.next
      nodeToDelete = None
    else:

      #3. Else, traverse to the node previous to the 
      #   node with value equal to key, and adjust links 
      while(temp.next != None):
        if(temp.next.data == key):
          nodeToDelete = temp.next
          temp.next = temp.next.next
          nodeToDelete = None
          break

        temp = temp.next

#### Delete Last Node by Key
def pop_last(self, key):    

  #1. if head is not null create three nodes
  #   lastNode - to track last node with value
  #   equal to key, previousToLast - to track 
  #   node previous to lastNode, temp - to
  #   traverse through the list
  if(self.head != None):
    temp = None 
    previousToLast = None
    lastNode = None
    
    #2. traverse through the list and keep on updating
    #   lastNode and previousToLast whenever find a node
    #   with value equal to the specified key
    if(self.head.data == key): 
      lastNode = self.head
    
    temp = self.head
    while(temp.next != None):
      if(temp.next.data == key):
        previousToLast = temp
        lastNode = temp.next
      temp = temp.next
 
    #3. Delete the lastNode and update all links
    if(lastNode != None):
      if(lastNode == self.head):
        self.head = self.head.next
        lastNode = None
      else:
        previousToLast.next = lastNode.next
        lastNode = None

#### Delete All Nodes by Key
def pop_all(self, key):   
  
  #1. if the head is not null and value stored at
  #   head is equal to key, keep on adjusting the
  #   head as head next and deleting previous head
  #   until new head becomes null or not equal to key
  while(self.head != None and self.head.data == key):
    nodeToDelete = self.head
    self.head = self.head.next
    nodeToDelete = None

  #2. create a temp node to traverse through the
  #   list and delete nodes with value equal to 
  #   key and adjust links accordingly
  temp = self.head        
  if(temp != None):
    while(temp.next != None):
      if(temp.next.data == key):
        nodeToDelete = temp.next
        temp.next = temp.next.next
        nodeToDelete = None
      else:
        temp = temp.next

####################### swapNodeValues
#if the given list is 10->20->30->40->50. After swapping values of first and fourth nodes, the list will become 40->20->30->10->50.
def swapNodeValues(self, node1, node2):
  
  #1. count the number of nodes in the list
  temp = self.head
  N = 0
  while (temp != None):
    N += 1
    temp = temp.next

  #2. check if the swap positions are valid entries
  if(node1 < 1 or node1 > N or node2 < 1 or node2 > N):
    return

  #3. traverse to the nodes where values to be swapped
  pos1 = self.head
  pos2 = self.head
  for i in range(1, node1):
    pos1 = pos1.next;
  for i in range(1, node2):
    pos2 = pos2.next;

  #4. swap the values of two nodes
  val = pos1.data
  pos1.data = pos2.data
  pos2.data = val     

############################### find length of linked list
# This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.
    def getCount(self):
        temp = self.head # Initialise temp
        count = 0 # Initialise count
 
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

################################ Remove duplicates from sorted linked list
    # This function removes duplicates
    # from a sorted list        
    def removeDuplicates(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head
        
  ################################################# Buble sort
  #!/usr/bin/python3
def bublesort(input_list, find):
    low = 0
    high = len(input_list) - 1

    while low <= high:
      mid = low + high//2
      print(mid)
      guess = input_list[mid]
      if(guess == find):
          return guess
      elif guess > find:
          high = mid - 1
      else:
          low = mid+1


print(bublesort([1,3,4,6,9],3))

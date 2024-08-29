"""
a=input("Enter your number:")
b=input("Enter your number:")
c=input("Enter your number:")
min=a if a<b and a<c else b if b<c else c
max=a if a>b and a>c else b if b>c else c
print("Min value:",min)
print("Max value: ",max)

"""

"""
a=int(input("Enter First number:"))
b=int(input("Enter second number :"))
print("Both numbers are equal" if a==b else "First Number is less than second Number"
      if a<b else "First Number Greater than second number")
"""

"""
list1=["one","Two","Three"]
list2=["one","Two","Three"]
print(id(list1))
print(id(list2))
print(list1 is list2)
print(list1 is not list2)
print(list1 == list2)
"""

"""
x="hello learning python is very easy!!!"
print("h" in x)
print("d" in x)
print("d "  not in x)
print('Python ' in x)
print('python ' in x)
"""

"""
from math import pi
r=float(input("Enter the radius of a circle: "))
Area=pi*r**2
print("Thr Area of the circle is:",Area)
circum=2*pi*r
print("Circumference of circle is: ", circum)
"""

"""
a=input("Enter your first number:")
b=input("Enter your second number:")
x=int(a)
y=int(b)
print("The sum of two number:",x+y)
"""

"""
a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
print("sum",a+b)
"""

"""
eno=int(input("Enter Employee No."))
ename=input("Enter Employee name:")
eAge=int(input("Enter Employee Age:"))
esal=float(input("Enter Employee salary:"))
eAdd=input("Enter your address:")
married=bool(input("Employee Married[True|False]:"))

print("Please Confirm information:")
print("Employee No.:",eno)
print("Employee Name:",ename)
print("Employee Age:",eAge)
print("Employee Salary:",esal)
print("Employee Address:",eAdd)
print("Employee Married ? : ",married)
"""

""""
a,b=[int(x) for x in input("Enter 2 numbers:").split()]
print("Product is:",a*b)
"""

"""
I=eval(input("Enter List"))
print(type(I))
print(I)
"""

'''

from sys import argv
#argv=(10,20,30)
print(argv)
print(type(argv))
print(argv)
print("The Number of command Line Arguments:",len(argv))
print("The list of command Line Argument:",argv)
print("Command Line Arguments one by one:")
for x in argv:
    print(x)

'''
'''
from sys import argv
argv=("sidd",10,20,30)
sum=0
args=argv[1:]# its means that declared variable has been sliced from index 0
                        # bvecause of the string but there is no string then index start from 0
for x in args:
    n=int(x)
    sum=sum+n
print("The Sum:",sum)
'''

'''
import argv
print(type(argv))

from sys import argv
print("The List of Command Line Arguments:", argv)
print("Command Line Arguments one by one:")
for x in argv:
    print(x)


'''

"""
a,b,c=10,20,30
print("b value is %i and c value is %i" %(b,c))
print(a,b,c,sep=':')
"""

'''
s="Durga"
list=[10,20,30,40]
print("Hello %s... The List of items are %s" %(s,list))

'''

'''
I=[10,20,30,40]
t=(100,200,300,400)
print(I,"\n",t)
'''

'''
name="Durga"
salary=100000
friend="rahul"
print("Hello {0} your salary is {1} and your Friend{2} is waiting".format(name,salary,friend))
'''
'''
name=input("Enter name:")
if (name=="durga"):
    print("hello Durga Good Morning")
else:
    print("hello Guest Good Morning")
print("How are you!!!")
'''
"""
brand=input("Enter your favourite brand:")
if brand=="RC":
    print("It is children brand")
elif brand=="KF":
    print("It is not that much kick")
elif brand=="FO":
    print("Buy one get free One")
else:
    print("Other Brands are not recommanded")
"""
'''
#Write a program to find biggest of given 2 numbers from the commad prompt?
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
if n1>n2:
    print("The first number is greater:",n1)
else:
    print("The second number is greater:",n2)
'''

'''
#Write a program to find biggest of given 3 numbers from the commad prompt?
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))
if n1>n2 and n2>n3:
    print("The first number is bigger:",n1)
elif n2>n3:
    print("The second number is bigger:",n2)
else:
    print("The third number is bigger:",n3)
'''

'''
#Write a program to find smallest of given 3 numbers?
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))
if n1<n2 and n2<n3:
    print("the first number is smaller:",n1)
elif n2<n3:
    print("The second number is smaller:",n2)
else :
    print("The third number is smaller:",n3)
'''
'''
#Write a program to check whether the given number is even or odd?
num=int(input("Enter the number first:"))
if (num%2==0):
    print("%d is even number"%num)
else:
    print("%d is odd number"%num)
'''

'''
#Write a program to check whether the given number is in between 1 and 100?
num=int(input("Enter the number:"))
if(num>=1 and num<=100):
    print("The number",num,"is between 1 to 100")
else:
    print("The number",num,"is not between 1 to 100")
'''

'''
#Write a program to take a single digit number from the key board and print is value inEnglish word?
n=int(input("Enter the single digit number:"))
if n==0:
    print("ZERO")
elif n==1:
    print("ONE")
elif n==2:
    print("TWO")
elif n==3:
    print("THREE")
elif n==4:
    print("FOUR")
elif n==5:
    print("FIVE")
elif n==6:
    print("SIX")
elif n==7:
    print("SEVEN")
elif n==8:
    print("EIGHT")
elif n==9:
    print("NINE")
else:
    print("Please enter the number between 0 to 9")
'''

'''
#To print characters present in the given string
a="Siddharth"
for x in a:
    print(x)
'''
'''
#To print characters present in string index wise
s=input("Enter some string: ")
i=0
for x in s:
    print("The character present at",i,"index is:",x)
    i=i+1
'''
'''
for x in range(10):
    print("hello->",x)
'''
'''
for x in range(21):
    if(x%2!=0):
        print(x)
'''
'''
for x in range(10,0,-1):
    print(x)
'''

'''
list=eval(input("Enter List:"))
sum=0;
for x in list:
    sum=sum+x;
print("The sum is:",sum)
'''
'''
x=1
while x<=10:
    print(x)
    x=x+1
'''
'''
#To display the sum of first n numbers
n=int(input("Enter the number:"))
sum=0
i=0
while i<=n:
    sum=sum+i
    i+=1
print(sum)

'''
'''
#write a program to prompt user to enter some name until entering Durga
name=" "
while name!="siddharth":
    name=input("Enter name:")
print("Thanks for confirmation")
'''
'''
# infinite loop 
i=0
while True:
    i+=1
    print("Hello",i)
'''
'''
for x in range(4):
    for y in range(4):
        print("i=",x,"  j=",y)
'''

'''
#Write a program to dispaly *'s in Right angled triangled form
n=int(input("Enter the number of rows:"))
for i in range (1,n+1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()
'''
'''
#Alternate way
n=int(input("Ente your no. of rows:"))
for i in range(1,n+1):
    print("* "*i)
'''
'''
n=int (input("Enter number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=' ')
    print("* "*i)
'''

'''
n=int (input("Enter number of rows:"))
for i in range(1,n+1):
    #for j in range(n-i):
        print(" "*(n-i),end=' ')
        for k in range(1,i):
            
            print("*",end=' ')    
        print()
'''
'''
n= int(input("Ente the number to print: "))
for i in range(10):
        if i==n:
                print("processing is enough... plz break")
                break
        print(i)
'''

"""
cart=[10,20,30,40,300,456,54,98,900,500]
for item in cart:
        if item>600:
                print("To print this order insurence must be required")
                break
        print(item)
"""
'''
n=int(input("Enter the number to print table: "))
for i in range(1,11):
        print(n,"x",i,"=",n*i)
'''
'''
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,1+i):
        print("*",end=" ")
    print()
'''
'''
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("* "*i)
'''
'''
cart=[10,20,30,40,500,700,232,454,900,899,122,23]
for item in cart:
    if item>=500:
        print("We cannot process this item:",item)
        continue
    print(item)
'''
'''
n=int(input("Enter the number : "))
for i in range(1,n+1):
    if i%2==0:
        print("even number:",i)
        continue
    print("Odd number:",i)
'''
'''
numbers=[10,20,30,0,5,56,0,30,25]
for n in numbers:
    if n==0:
        print("Hey how we can divide zero... just skipping")
        continue
    print("500/{}={}".format(n,500/n))
'''
'''
cart=[10,20,30,40,50,60,600,70,80,800,454]
for item in cart:
    if item>=500:
        print("We cannot process this order")
        continue
    print(item)
'''
'''
for i in range(100):
    if i%9==0:
        print(i)
    else: pass
'''
'''
#Check for Vowels

char = input("Enter a character: ")

if char in 'aeiouAEIOU':
    print(char, "is a vowel")
else:
    print(char, "is a consonant")
'''
'''
#sum of the elements of the list
list=[1,2,3,4,5,6,7,8,9,787]
sum=0
for i in list:
    sum=sum+i
print("Sum: ",sum)
'''
'''
#Reverse a string
user_input=input("Enter a string: ")
reversed_string=" "
for char in user_input:
        reversed_string=char+reversed_string
print("Reversed string: ",reversed_string)
'''
'''

#find the largest number in the list
def find_largest_number(numbers):
    if len(numbers)==0:
        return none
    largest=numbers[0]
    for number in numbers:
        if number>largest:
            largest=number
    return largest
numbers=[5,7,9,11,1,3,54,8,21,99,104,14]
largest_number=find_largest_number(numbers)
print(f"The largest number in the list is: {largest_number}")
'''
#count occurances of a character in a string
#Taking string input from the user
string=input("Enter a string: ")
#Taking character input from the user
alpha=input("Enter char to count: ")
#initialize a counter to count occurance of character
count=0

for char in string:
    #if condition is true then increment the counter
    if char==alpha:
        count +=1

print(f"The condition '{alpha}' occurs {count} times in string.")

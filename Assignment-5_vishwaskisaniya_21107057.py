#Question- 1

a= input("Enter a string: ")
b= len(a)
while b>0:
    print(a[b-1], end='')
    b=b-1
print("\n") 

#-------------------------------------------------------------------------------

#Question- 2

lowerrange1= input("Enter the lower range: ")
lowerrange=int(lowerrange1)
upperrange1= input("Enter the upper range: ")
upperrange=int(upperrange1)
n= int(input("Enter the number: "))
#to keep the starting and end not included
i= lowerrange+1
while i<upperrange:
    if(i%n==0):
        print(i)
    i=i+1
print("\n")
    
#-------------------------------------------------------------------------------

# Question- 3

import math
a=int(input("ENTER THE FIRST SIDE: "))
b=int(input("ENTER THE second SIDE: "))
c=int(input("ENTER THE third SIDE: "))
s=(a+b+c)/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area of the triangle: ',area)
print("\n")

#-------------------------------------------------------------------------------

# Question- 4

for i in range(1,6):
    for j in range(0,i):
        print('*', end='')
    print()
for i in range(0,5):
    j=4-i
    while(j>0):
        print('*', end='')
        j=j-1
    print()
print("\n")

#-------------------------------------------------------------------------------
    
# Question- 5

a1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a=a1
n= int(input("Enter the number: "))
for i in range(1,n+1):
    if len(a)<i:
        a=a+a1
    for j in range(0,i):
        print(a[j], end='')
        
    print()
    
    a=a[i:]
print("\n")
    
#-------------------------------------------------------------------------------

# Question- 6

n=int(input("Enter the number till you want to check: "))

for i in range (2, n+1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        print(i)
print("\n")
        
#-------------------------------------------------------------------------------

# Question- 7


for i in range (1,500):
    if(i%7==0 and i%11==0):
        print(i)
print("\n")
        
#-------------------------------------------------------------------------------

# Question- 8

# creating an empty list
lst = []
  
# number of elements as input
print("Enter 10 Elements to add in a list")

n = 10
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) # adding the element
      
print("Entered list is:  ", lst)

#Part-1
print("Positive numbers in List are: ")
  
#traversing
for i in lst:   
    # checking condition
    if i >= 0:
       print(i, end = " ")
       print("\n")

#Part-2
print("Negative numbers in List are: ")
  
#traversing
for i in lst:   
    # checking condition
    if i <= 0:
       print(i, end = " ")
       print("\n")

#Part-3
print("Odd numbers in List are: ")
  
#traversing
for i in lst:   
    # checking condition
    if i %2 != 0:
       print(i, end = " ")
       print("\n")

#Part-4
print("Even numbers in List are: ")
  
#traversing
for i in lst:   
    # checking condition
    if i %2 == 0:
       print(i, end = " ")
       print("\n")

#Part-5
print('Frequecy of respective nos are: ')
for i in lst:
    if(type(i)==float):   # so no repetition occurs
        continue
    n=0
    j=0
    while j<10:
        if(lst[j]==i):
            n=n+1
            lst[j]=1.1   # an decimal no which would be used afterwards to distinguish it from others
        j=j+1
    print('Frequency of ',i,'is :',n)
print("\n")
    
#-------------------------------------------------------------------------------

# Question- 9

a= ['vishwas','vishwas','pulkit','soumik','soumik','pulkit','kundu','dheeraj']
for i in a:
    g=0
    n=0
    if(i=='----'):
        continue

    for j in a:
        if(i==j):
            n=n+1
            a[g]='----'
        g=g+1
    print(i," occured ",n," times")
    
#-------------------------------------------------------------------------------














# Question- 1

# Takiong integer input from
n = int(input("Enter any number: "))
sum1 = 0   # this will be used to add divisble numbers

# checking if it is perfect number
if n > 0:   # Makeing sure number is positive
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")
else :
    print("Only positve integers can be perfect number.")



# Question- 2

# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]


# taking input
print("Kindly enter alphabets only.")
s = input("Enter word/sentence to be checked: ").replace(" ","").lower()
ans = isPalindrome(s)   # calling function

# checking palindrom
if ans:
    print("Yes")
else:
    print("No")



# Question- 3

# Print Pascal's Triangle in Python
from math import factorial

r = int(input("Enter the number of rows: "))    # r for rows
for i in range(r):
    for j in range(r-i+1):

        # for left spacing
        print(end=" ")

    for j in range(i+1):

        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    # for new line
    print()



# Question- 4
# Check if the string is pangram
  
def pangram(str):
    All_alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in All_alphabets:
        if i not in str.lower():   # As python is case sensitive, so we have to check its small letters too
            return False
  
    return True
      
# Example:
string = "The quick brown fox jumps over the lazy dog"
if(pangram(string) == True):
    print("Yes, The given string is pangram!")
else:
    print("No")


    
# Question- 5

items=[n for n in input().split('-')]
print(items)
items.sort()
print(items)
print('-'.join(items))



# Question- 6

def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: $ {kwargs['student_name']}")

    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: $ {kwargs['student_name']}")
            print(f"Student Class: $ {kwargs['student_class']}")


student_data(student_id='SV12', student_name='Jean Garner')

student_data(student_id='SV12', student_name='Jean Garner', student_class ='V')



# Question- 7

# creating class
class Student:
    pass 
class Marks:
    pass
# instance
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nChecking whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))



# Question- 8
# return a list of lists of length 3 


def three_Sum(num):
    if len(num)<3: return []
    num.sort()
    result=[]
    for i in range(len(num)-2):
        left=i+1
        right=len(num)-1
        if i!=0 and num[i]==num[i-1]:continue
        while left<right:
            if num[left]+num[right]==-num[i]:
                result.append([num[i],num[left],num[right]])
                left=left+1
                right=right-1
                while num[left]==num[left-1] and left<right:left=left+1
                while num[right]==num[right+1] and left<right: right=right-1
            elif num[left]+num[right]<-num[i]:
                left=left+1
            else:
                right=right-1
    return result
 
nums1=[-25, -10, -7, -3, 2, 4, 8, 10]

print(three_Sum(nums1))




# Question- 9

class validation:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0


print(validation().is_valid_parenthese("(){}[]"))
print(validation().is_valid_parenthese("()"))
print(validation().is_valid_parenthese("[)"))
print(validation().is_valid_parenthese("({[)]"))
print(validation().is_valid_parenthese("{{{"))





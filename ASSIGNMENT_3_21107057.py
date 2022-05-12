#Question-1

#Enter a decimal number and get its binary equivalent

#METHOD--> 1
num = int(input("Enter any number: "))

result = bin(num)

print("Binary equivalent of ",num,"is: ", result,"\n")

#METHOD--> 2
decimal_number = int(input("Enter a decimal number: "))
number_bin = []
while decimal_number > 0:
    bin_digit = decimal_number%2
    number_bin.append(bin_digit)
    decimal_number = decimal_number//2
number_bin.reverse()
print("The binary equivalent is:")
for i in number_bin:
    print(i, end=" ")
print("\n")

#Question-2
#METHOD--> 1
print("Welcome to this interactive python calculator")
expression = input("Enter the expressions by using only these operators (+,-,*,/,**,%,//):")
print("The result is ", end=" ")
print(eval(expression))
print("\n")

#METHOD--> 2
print("This calculator works for 4 numbers only:)\n\n")
num1 = int(input("Enter number: "))
op1 = str(input("Enter operator: "))
num2 = int(input("Enter number: "))
op2 = str(input("Enter operator: "))
num3 = int(input("Enter number: "))
op3 = str(input("Enter operator: "))
num4 = int(input("Enter number: "))

string = '''Your expression:
((<num1> <op1> <num2>) <op2>(<num3>)) <op3><num4> '''
print(string.replace("<num1>",str(num1)).replace("<op1>",str(op1)).replace("<num2>",str(num2)).replace("<op2>",str(op2)).replace("<num3>",str(num3)).replace("<op3>",str(op3)).replace("<num4>",str(num4)))


#Arithmatic Operators--> +,-,*,\

r1= 0
r2= 0
r3= 0
if op1 == "+":
    r1 = num1+num2
    
elif op1 == "-":
    r1 = num1-num2

elif op1 == "*":
    r1 = num1*num2
    
elif op1 == "/":
    r1 = num1/num2
    


if op2 == "+":
    r2 = r1+num3
    
elif op2 == "-":
    r2 = r1-num3

elif op2 == "*":
    r2 = r1*num3
    
elif op2 == "/":
    r2 = r1/num3

    

if op3 == "+":
    r3 = r2+num4
    print("Output of the given expression is: ",r3)
elif op3 == "-":
    r3 = r2-num4
    print("Output of the given expression is: ",r3)
elif op3 == "*":
    r3 = r2*num4
    print("Output of the given expression is: ",r3)
elif op3 == "/":
    r3 = r2/num4
    print("Output of the given expression is: ",r3)


#Question-3

import math as M

#part(a)

a1 = 3
a2 = 4
a3 = 5
answer_a = (a1 + a2)*a3
print("Result of part (a) is: ", answer_a)
print("\n")

#part(b)
print("Choose the value of n")
n = float(input("The value of n taken is: "))
expression_b = (n*(n-1))/2
print("The result of part (b) is: ", expression_b)
print("\n")

#part(c)
print("Choose the value of r")
radius = float(input("The value of radius taken in: "))
expression_c = (4 * M.pi * (radius**2))
print("The result of part (c) is: ", expression_c)

#part(d)
r = float(input("Enter the value of r: "))
a = float(input("Enter the value of angle a: "))
b = float(input("Enter the value of angle b: "))
print("The result of part (d) is: ", end=" ")
print(((r*((M.cos(a))**2)) + (r*((M.sin(b))**2)))**0.5)
print("\n")

#part(e)
x1 = float(input("enter the value of x1:"))
x2 = float(input("enter the value of x2:"))
y1 = float(input("enter the value of y1:"))
y2 = float(input("enter the value of y2:"))
print("The result of part (e) is: ", end=" ")
if x2 == x1:
    print("NOT DEFINED")
else:
    print("(y2-y1)/(x2-x1)", (y2-y1/(x2-x1)))
print("\n")

#Question-4

print("In the range(5): ")
for i in range(5):
    print(i)

print("In the range(3, 10): ")
for i in range(3, 10):
    print(i)
print('\n')

print("In the range(4, 13, 3): ")
for i in range(4, 13, 3):
    print(i)
print('\n')

print("In the range(15 ,5, -2): ")
for i in range(15, 5, -2):
    print(i)
print("\n")

print("In the range(5, 3): ")
for i in range(5, 3):
    print(i)
print("\n")

#Question-5

print('''This program computes molecular weight of
carbohydrates, for this we need to enter number of
atoms of hydrogen, carbon and oxygen.''')
#number of atoms cannot be negative
num_hydrogen = int(input("Enter the number of hydrogen atoms: ")) 
num_carbon = int(input("Enter the number of carbon atoms:")) 
num_oxygen = int(input("Enter the number of oxygen atoms:")) 

# now calculating the weight of elements by multiplying their number of atoms and atomic mass
weight_of_hydrogen = num_hydrogen*1.00794
weight_of_carbon = num_carbon*12.0107
weight_of_oxygen = num_oxygen*15.9994

#weight of carbohydrate would be sum of weight of hydrogen , oxygen and carbon
weight_of_carbohydrate = weight_of_hydrogen + weight_of_carbon + weight_of_oxygen
print("The weight of carbohydrate: ", weight_of_carbohydrate)

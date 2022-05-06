#QUESTION 1
'''For taking length of string
First take input of string'''

string = "Python is a case sensitive language"

#len() is used for taking length of given string.
print("A) Length of the given string: ",len(string),"\n") 

# This is for giving output string in reverse order.
print("B) Reverse of the given string is :")
print(string[::-1],"\n")    

#slicing the string.
new_string = string[10:26]
print("C) New sliced string is: ","\n", new_string,"\n")

#replace a string using replace fun. in string slicing,
Replaced_string= string.replace('a case sensitive' , 'object oriented')
print("D) String after replacing: ", "\n" ,Replaced_string ,"\n")

#Finding the index of "a" in the input string.
print("E) Index of substring 'a' is:", string.find("a"),"\n")

#Printing the string without white spaces using replace in string.
print("F) Sting without white spaces: ","\n",string.replace(" ", ""))

#----------------------------------------------------------------------------------------------

#QUESTION 2

#Taking input from User.
name = str(input("Name of Applicant: "))
'''I have used different data types here
        like int, str andfloat'''
SID = int(input("Enter your college ID:"))

dep_name = str(input("Enter your department name: "))

cgpa = float(input("Enter your CGPA: "))

'''Here string is formed using multiline comment command which
gives us the string in the same body formate as we write inside this.'''

string= '''Hey, <name> Here!          
My SID is <SID>
I am from <dep_name> department and my CGPA is <cgpa>'''

#As the string is replaced multiple times...we use this slicing in the given way.
print(string.replace("<name>", name).replace("<SID>", str(SID)).replace("<dep_name>", dep_name).replace("<cgpa>", str(cgpa)))


#------------------------------------------------------------------------------------------------------------------------------


#QUESTION 3

#Use of Bitwise Operators.
a = 56
b = 10

#Use of Bitwise AND(&) operator.
print("A. a & b =", a & b)

#Use of Bitwise OR(|) operator.
print("B. a | b =", a | b)
 
#Use of Bitwise XOR(^) operator.
print("C. a ^ b =", a ^ b)

#Use of shift(left) operator.
print("D. a << 2 = ", a << 2)

#Use of shift(both) operator.
print("E. a >> 2 = ", a >> 2," and ", "b >> 4 = ", b >> 4 )


#----------------------------------------------------------------------------------------------


#QUESTION 4

# Taking input
string= str(input("Enter any string: "))

# Using string slicing to find a word in the string
checked = string.find("name")

# Making a loop for printing yes and no for the required outputs.
# Here '==' is comparison operator
if checked == -1:     # '-1' is the value as an output of find function indicating the absence of particular string in it.
    print("No")
    
else:
    print("Yes")


#----------------------------------------------------------------------------------------------


#QUESTION 5

# Taking inputs of the sides of the triangle.
n1 = int(input("Enter First length : "))
n2 = int(input("Enter Second length : "))
n3 = int(input("Enter Third length : "))

# Checking the condition for triangle to be formed.
F1 = n1 > n2 + n3
F2 = n2 > n1 + n3
F3 = n3 > n1 + n2

# Here we check wheather the all conditions are satisfied or not.
Output = str(F1 or F2 or F3)

print("The triangle can be formed?")

# Using string slicing.
print(Output.replace("True", "No!").replace("False", "Yes!"))


#----------------------------------------------------------------------------------------------


#QUESTION 6

a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))

c = (a^b)
d = bin(c)

count = 0
for i in d[2:]:
    if i=="1":
        count+=1
        print(count)
    

#----------------------------------------------------------------------------------------------

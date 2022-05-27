#Question- 1

print("Grading system of a school!")

marks = int(input("Enter your marks obtained( out of 100): "))

#if-elif loop is used here!

if marks < 25:
    print("Your Grade is: F")
elif 25 <= marks <= 45:
    print("Your Grade is: E")
elif 45 < marks <= 50:
    print("Your Grade is: D")
elif 50 < marks <= 60:
    print("Your Grade is: C")
elif 60 < marks <= 80:
    print("Your Grade is: B")
elif 80 < marks < 100:
    print("Your Grade is: A")

#-----------------------------------------------------------------------------

#Question- 2

year = int(input("\nEnter any Year:"))

if year%4 == 0 and year%100 !=0:
    print(year, "is a Leap Year")
elif year%400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not an Leap Year")

#-----------------------------------------------------------------------------

#Question- 3

#Before using random function we have to import random module in our programme.
    
import random

print("\nIt's a one to one digit multiplication Game")
i=1        # Number of trials of game
while i <=10:             #Loop will continue till 10th trial of questions.
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    print("Question-",i,":", x, "*", y)
    r = int(input("Enter your result:"))   #r is result to be enteredby user.
    if r == x*y:
        print("Right!")
    else:
        print("Wrong!", "The correct answer is:", x*y)
    i+= 1      #Incriment of one trial 


#-----------------------------------------------------------------------------

#Question- 4
    
print("\n")
for x in range(200):
    if x % 5 == 2:
        if x % 6 == 3:
            if x % 7 == 2:
                print("There are total", x," candies in the bowl.")
        

#-----------------------------------------------------------------------------    
    

























    

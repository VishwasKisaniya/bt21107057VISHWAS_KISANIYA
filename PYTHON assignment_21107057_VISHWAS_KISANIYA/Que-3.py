seconds = int(input("Enter the total number of seconds: "))

#For minutes
minutes = seconds//60  # floor divisio operato is used.

#For minute _seconds
minute_seconds = seconds%60  # Modulus operator is used.

print("Entered", seconds,"seconds", "=" , minutes,  "minutes" , minute_seconds,"seconds")

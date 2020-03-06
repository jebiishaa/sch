# name  = input("Enter your name: ")
# print(f"my name is {name}")
# output the distance covered
print("How many kilometres did you cover today?")
# lets input the distance we covered
kms=input()
#convert the distance to miles
miles=float(kms)/1.60934
# place the number of decimal you need
miles=round(miles,2)
# print the output of the distance
print(f"Your{kms}kilometre distance is{miles}miles")

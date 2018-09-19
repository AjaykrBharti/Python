#Create a Python project to guess a number that has randomly selected.
from numpy import *
i = 0
n = 0
times = int(input("Enter no. of time you want to play this game :"))
while n < times:
    inputNo = int(input("Enter the no: "))
    a = int(random.rand()* 10)
    if inputNo == a:
        i = i + 1
        print("You have earned ",i," point.")
        print("Actual no: ",a)
    else:
        print("You have earned 0 point.")
        print("Actual no: ",a)
    n = n+1
print("Game End")

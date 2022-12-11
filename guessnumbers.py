# generate random number
import random
mynum = random.randint(0, 10)
print("I Have a number in my mind can you guess it")

while True:
    usernum = int(input("Enter your Guess:     "))
    if (mynum == usernum):
        print("Yes You are right")
        break
    elif (mynum > usernum):
        print("My number is greater than the number you entered.Try Again", end="\n\n")
    else:
        print("My number is smaller than the number you entered", end="\n\n")

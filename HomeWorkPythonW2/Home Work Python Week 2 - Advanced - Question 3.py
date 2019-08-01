
import random

def number_picked():
    return random.randint(0,200)


def Guess_Number_Function(secret_number):
    guessed_number = -1
    delta = int(secret_number-guessed_number) 
    while (delta != 0):
        guessed_number=int(input('Guess a number between 0 and 200:'))
        delta = secret_number-guessed_number 
        if (abs(delta)<=10 and delta!=0):
            print ("Close")
            if (secret_number % 2 == 0): print("The number is even")
            else: print ("The number is odd")      
            if (secret_number % 3 == 0): print("The number is divisible by 3")
        elif (delta > 100 ):
            print ('Way Upper')
        elif (delta > 10 and delta <= 100 ):
            print ('Upper')
        elif (delta < -10 and delta >= -100 ):
            print ('Lower')
        elif (delta < -100):
            print ('Way Lower')

    print ("Bingo! The number was " + str(secret_number))
    
secret_number = number_picked()    
Guess_Number_Function(secret_number)    





import random
import time

def guessed_number(from_number,to_number):
    return random.randint(from_number,to_number)

print("Think of a number between 0 and 200")
time.sleep(5)

guess = -1

Start_Range = 0
End_Range = 200
answer = "No"
while (answer != 'Yes'):
    guess = guessed_number(Start_Range, End_Range)
    answer = input("Is your number " + str(guess) + "?")
    if answer == 'No':
        answer_2 = input ("Is your number bigger, smaller or equal to" + str(int((Start_Range + End_Range)/2)) + "(b/s/e) ?")
        if answer_2 == 'e':
            answer = "Yes"
        if answer_2 == 'b':
            Start_Range = int((Start_Range + End_Range)/2)
        if answer_2 == 's':
            End_Range = int((Start_Range + End_Range)/2)                  
    
    
print ('Bingo')






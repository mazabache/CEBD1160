
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



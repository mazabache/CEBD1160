#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time

def number_picked():
    return random.randint(0,200)

secret_number = number_picked()
guessed_number = -1
delta = int(secret_number-guessed_number) 
while (delta != 0):
    guessed_number=int(input('Guess a number between 0 and 200:'))
    delta = secret_number-guessed_number
#    print(delta)
#    print(secret_number)
    if (abs(delta)<=10 and abs(delta)>0):
        print ("Close")
    elif (delta > 100 ):
        print ('Way Upper')
    elif (delta > 10 and delta <= 100 ):
        print ('Upper')
    elif (delta < -10 and delta >= -100 ):
        print ('Lower')
    elif (delta < -100):
        print ('Way Lower')

print ('Bingo')


# In[ ]:





# In[ ]:





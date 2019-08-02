#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import time

def guessed_number(from_number,to_number,mod):
    guess=random.randint(from_number,to_number)
    while (guess%mod !=0):
        guess=guess+1
    return guess
        

print("Think of a number between 0 and 200")
time.sleep(5)

guess = -1

Start_Range = 0
End_Range = 200
answer = "No"
while (answer != 'Yes'):
    guess = guessed_number(Start_Range, End_Range)
    answer = input("Is your number " + str(guess) + " Yes/No ?")
    if answer == 'No':
        answer_2 = input ("Is your number bigger, smaller or equal to" + str(int((Start_Range + End_Range)/2)) + "(b/s/e) ?")
        if answer_2 == 'e':
            answer = "Yes"
        if answer_2 == 'b':
            Start_Range = int((Start_Range + End_Range)/2)
        if answer_2 == 's':
            End_Range = int((Start_Range + End_Range)/2)                      

print ('Bingo')


# In[ ]:





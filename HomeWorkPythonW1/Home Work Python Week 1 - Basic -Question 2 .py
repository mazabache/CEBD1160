#!/usr/bin/env python
# coding: utf-8

# In[16]:


for x in range(1, 101):
  if (x%3==0 and x%5==0):
    print("FizzBuz")
  elif (x%5==0):
    print("Buzz")
  elif (x%3==0):
    print("Fizz")
  else:
    print(x)


# In[ ]:





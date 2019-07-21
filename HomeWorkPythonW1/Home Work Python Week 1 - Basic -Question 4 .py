#!/usr/bin/env python
# coding: utf-8

# In[11]:


not_allowed=['A','E','I','O','U','a','e','i','o','u']
input_str=input("Enter a string:")
result_str=''
for char in input_str:
    if char in not_allowed:
        result_str+=''
    else:
        result_str+=char
print (result_str)


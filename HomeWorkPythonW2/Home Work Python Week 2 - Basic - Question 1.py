#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Remove_Duplicates_from_List(X):
  return list( dict.fromkeys(X) ) 

mylist = Remove_Duplicates_from_List(["a", "b", "a", "c", "c"])

print(mylist) 


# In[ ]:





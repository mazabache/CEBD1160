#!/usr/bin/env python
# coding: utf-8

# In[14]:


def Is_Number_in_Ordered_List(mylist, number):
    for i in mylist:
        if i==number:
            return True
    return False

print (Is_Number_in_Ordered_List ([1,2,3],5))

print (Is_Number_in_Ordered_List ([1,2,3],2))


# In[ ]:





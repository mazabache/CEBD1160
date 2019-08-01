#!/usr/bin/env python
# coding: utf-8

# In[20]:


def Remove_Odd_Numbers_from_List(mylist):
    for i in mylist:
        if (i % 2 != 0) :
            mylist.remove(i)
    return(mylist)

print(Remove_Odd_Numbers_from_List([1,4,9,16,25,36,49,64,81,100]))


# In[ ]:





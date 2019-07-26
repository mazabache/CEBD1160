#!/usr/bin/env python
# coding: utf-8

# In[14]:


items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))


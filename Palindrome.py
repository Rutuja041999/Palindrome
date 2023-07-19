#!/usr/bin/env python
# coding: utf-8

# In[1]:


def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


l=[]
for i in range(2000,3201):
    if(i%7==0 and i%5!=0):
        l.append(str(i))
print(','.join(l))
        
    


# In[ ]:





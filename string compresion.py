
# coding: utf-8

# In[3]:


def compress(s):
    new=''
    for i in s:
        if i not in new:
            new+=i
            new+=str(s.count(i))
    return new
        


# In[5]:


compress('aaabbbcaaad')


# In[9]:


compress('    ')


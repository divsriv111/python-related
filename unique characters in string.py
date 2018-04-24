
# coding: utf-8

# In[11]:


def unique_char(s):
    for i in s:
        if s.count(i) > 1:
            return False
    return True


# In[13]:


unique_char('abcdd')


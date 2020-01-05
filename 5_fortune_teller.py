#!/usr/bin/env python
# coding: utf-8

# In[27]:


#RANDOM GENERATOR 

BTS=["Namjoon","Taehyung","Yoongi","Jin","Jhope","Jimin","Jungkook"]
item=random.choice(BTS)
print('Your best friend is',item)


# In[28]:


import random 

#lists of random items
home=['mansion','apartment','RV','lakehouse','loft']
location=['london','sydney','san diego','colorado springs','chicago','shanghai','taipei','busan']
hobby=['building houses','gardening','baking cakes','painting','fishing']

#user input
age=int(input('What is your current age?'))

#random generator
home=random.choice(home)
location=random.choice(location)
hobby=random.choice(hobby)
print(home)
print(location)
print(hobby)

if age+20<=40:
    print ('seems like you are not near retirement!')
elif 40<age+20<=60:
    print ('you are almost near retirement! By the time you retire, you will be living in',location,'in a',home,'and pick up',hobby)
else:
    print ('you can retire now!','enjoy your retirement in a beautiful',home,'in',location, 'where you will also pick up',hobby)


# In[ ]:





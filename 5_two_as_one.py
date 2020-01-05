#!/usr/bin/env python
# coding: utf-8

# In[33]:


#TWO AS ONE 
#Get three integers from the user and then tell the user whether two of them can add to make the third. 
#Different combinations: 
#A+B=C 
#A+C=B
#B+C=A

lst=[]

for i in range(0,3): 
    x = int(input('please enter 3 numbers')) 
  
    lst.append(x)

print (lst)

if (lst[0]+lst [1] == lst[2]):
    print ('two numbers in this list add up to the third number!')
elif (lst[0]+lst [2] == lst[1]):
    print ('two numbers in this list add up to the third number!')
elif (lst[1]+lst [2] == lst[0]):
    print ('two numbers in this list add up to the third number!')
else: 
    print('None of these two numbers in this list add up to the third number!')


# In[ ]:





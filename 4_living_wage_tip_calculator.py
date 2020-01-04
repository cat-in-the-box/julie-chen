#Min wage is $13.50 per hour. Living wage for single adult is $15.97 per hour. 
#Tipped employees actually get paid $9 (with assumption tips will make up for it)
#Coffee shop. 3 employees. 20 customers/hour. average bill is $5. 

#Purpose: Calculate how much tip per hour an employee needs

#version 1: Average minimum wage (service affects whether the tip lands below or above that)

print('Thanks for visiting The Little Cup today! I am Timmy, your Tip calculator.')

order_amt=float(input('What is your total order amount so I can help you calculate your tip?'))

while True:
    service=input('Did you enjoy your service today? Please input either: "Great" to tip 20%, "Decent" to tip 15% or "Could be better" to tip 10%')
    if service in ('Great','Decent','Could be better','great','decent','could be better'): 
        break 
    else:
        print ('mhmm I don\'t think I understood that. Please try again.')
    
if service in ('Great','great'):
    total_bill=round(order_amt*1.2,2)

if service in ('Decent','decent'):
    total_bill=round(order_amt*1.15,2)

if service in ('Could be better','could be better'):
    total_bill=round(order_amt*1.1,2)
                    
print('Your total bill is $' + str(total_bill))
    


# In[2]:


#version 2: Bring it up to the minimum wage, and extra good service goes on top of that
#Min wage is $13.50 per hour. Living wage for single adult is $15.97 per hour. 
#for one employee, they get paid $9. To meet min wage of $13.50, in one hour, they need to get $4.50 to make up the difference.
#$4.50 divide by 20 customers is $0.23 before service tip. 
#For three employees, that is $0.67 before service tip. 

print('Thanks for visiting The Little Cup today! I am Timmy, your Tip calculator.')

order_amt=float(input('What is your total order amount so I can help you calculate your tip?'))

n=str(order_amt+0.67)

while True: 
    add_tip=input('Would you like to pay additional tip of $0.67 before service tip for our employees to meet the min wage?')    
    if add_tip in ('Yes','yes','No','no'): 
        break 
    else:
        print ('mhmm I don\'t think I understood that. Please try again.')

        
if add_tip in ('Yes','yes'):    
    print('Great! Your bill comes out to $' + n + ' before service tip')
    
    while True:
        service=input('Did you enjoy your service today? Please input either: "Great" to tip 20%, "Decent" to tip 15% or "Could be better" to tip 10%')
        if service in ('Great','Decent','Could be better','great','decent','could be better'): 
            break 
        else:
            print ('mhmm I don\'t think I understood that. Please try again.')
    
    if service in ('Great','great'):
            total_bill=round((order_amt+0.67)*1.2,2)
    if service in ('Decent','decent'):
            total_bill=round((order_amt+0.67)*1.15,2)
    if service in ('Could be better','could be better'):
            total_bill=round((order_amt+0.67)*1.1,2)
    print('Your total bill is $' + str(total_bill))

    
if add_tip in ('No','no'):
    print ('Thanks for letting us know.')
    
    while True:
        service=input('Did you enjoy your service today? Please input either: "Great" to tip 20%, "Decent" to tip 15% or "Could be better" to tip 10%')
        if service in ('Great','Decent','Could be better','great','decent','could be better'): 
            break 
        else:
            print ('mhmm I don\'t think I understood that. Please try again.')
              
    if service in ('Great','great'):
            total_bill=round(order_amt*1.2,2)
    if service in ('Decent','decent'):
            total_bill=round(order_amt*1.15,2)
    if service in ('Could be better','could be better'):
            total_bill=round(order_amt*1.1,2)
    print('Your total bill is $' + str(total_bill))


# In[6]:


#version 3: Bring it up to the living wage, and extra service goes on top of that
#Living wage for single adult is $15.97 per hour. 
#for one employee, they get paid $9. To meet min wage of $15.97, in one hour, they need to get $6.97 to make up the difference.
#$4.50 divide by 20 customers is $0.35 before service tip. 
#For three employees, that is $1.05 before service tip. 

print('Thanks for visiting The Little Cup today! I am Timmy, your Tip calculator.')

order_amt=float(input('What is your total order amount so I can help you calculate your tip?'))
n=str(order_amt+1.05)

while True: 
    add_tip=input('Would you like to pay additional tip of $1.05 before service tip for our employees to meet the min wage?')
    if add_tip in ('Yes','yes','No','no'):
        break
    else: 
        print ('mhmm I don\'t think I understood that. Please try again.')
        
if add_tip in ('Yes','yes'):    
    print('Great! Your bill comes out to $' + n + ' before service tip')
    
    while True: 
        service=input('Did you enjoy your service today? Please input either: "Great" to tip 20%, "Decent" to tip 15% or "Could be better" to tip 10%')
        if service in ('Great','Decent','Could be better','great','decent','could be better'): 
            break 
        else:
            print ('mhmm I don\'t think I understood that. Please try again.')
            
    if service in ('Great','great'):
            total_bill=round((order_amt+1.05)*1.2,2)
    if service in ('Decent','decent'):
            total_bill=round((order_amt+1.05)*1.15,2)
    if service in ('Could be better','could be better'):
            total_bill=round((order_amt+1.05)*1.1,2)
    print('Your total bill is $' + str(total_bill))

    
    
if add_tip in ('No','no'):
    print ('Thanks for letting us know.')
    
    while True: 
        service=input('Did you enjoy your service today? Please input either: "Great" to tip 20%, "Decent" to tip 15% or "Could be better" to tip 10%')
        if service in ('Great','Decent','Could be better','great','decent','could be better'): 
            break 
        else:
            print ('mhmm I don\'t think I understood that. Please try again.')
            
    if service in ('Great','great'):
            total_bill=round(order_amt*1.2,2)
    if service in ('Decent','decent'):
            total_bill=round(order_amt*1.15,2)
    if service in ('Could be better','could be better'):
            total_bill=round(order_amt*1.1,2)
    print('Your total bill is $' + str(total_bill))

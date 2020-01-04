''' PLANNNING 
print("Let's find out who your bestie is in BTS!")

print('What do you like doing in your free time?')
print("Please type in a letter based on the selection below.\n" +
      "Fishing 1\n" +
      "Taking a walk in the park 3 
Gaming 5
Sleeping 7
Travel to other countries 9

What is your favorite food? 
Seafood 1
Meat 3 
Ramen 5
Lamb skewers 7

If you could be anyone of these, which would you be?
Tennis player 1
Police Officer 3
Farmer 5
Office worker 7

Which is your favorite movie?
Forrest Gump 1 
The Big Short 3
Call Me By Your Name 5
Eternal Sunshine of the Spotless Mind 7


Jin - 2
Jhope -7
Yoongi - 11
Namjoon 14
Jimin - 17
Taehyung- 18
Jungkook 19

END PLANNING '''


## BTS QUIZ CODE 

Left to Right: V, Yoongi, Jin, Jhope, Namjoon/RM, Jimin, Jungkook :) 

total=0
print('Let us find out who your bestie is in BTS!')

print('What do you like doing in your free time?')
print('Please type in a letter based on the selection below.\n A.Fishing\n B.Taking a walk in the park\n C.Gaming\n D.Sleeping\n E. Travel to other countries') 
free_time=input()
if free_time=='A':
    total2=total+1
elif free_time=='B':
    total2=total+3
elif free_time=='C':
    total2=total+5
elif free_time=='D':
    total2=total+7
else: total2=total+9


print('What is your favorite food?')
print('Please type in a letter based on the selection below.\n A.Seafood\n B.Meat\n C.Ramen\n D.Lamb Skewers') 
favfood=input()
if favfood=='A':
    total2=total2+1
elif favfood=='B':
    total2=total2+3
elif favfood=='C':
    total2=total2+5
else: 
    total2=total2+7


print('If you could be anyone of these, which would you be?')
print('Please type in a letter based on the selection below.\n A.Tennis Player\n B.Police Officer\n C.Farmer\n D.Office worker') 
profession=input()
if profession=='A':
    total2=total2+1
elif profession=='B':
    total2=total2+3
elif profession=='C':
    total2=total2+5
else: 
    total2=total2+7


print('Which is your favorite movie?')
print('Please type in a letter based on the selection below.\n A.Forrest Gump\n B.The Big Short\n C.Call Me By Your Name\n D.Eternal Sunshine of the Spotless Mind') 
movie=input()
if movie=='A':
    total2=total2+1
elif movie=='B':
    total2=total2+3
elif movie=='C':
    total2=tota2l+5
else: 
    total2=total2+7



if total2 < 7: 
    print('Jin')

if 6<total2<11:
    print('Jhope')
    
if 10<total2<14: 
    print ('Yoongi')
    
if 13<total2<18: 
    print ('Namjoon')    

if 17<total2<20: 
    print ('Jimin')    
    
if 19<total2<22: 
    print ('V')    
    
if 21<total2: 
    print ('Jungkook')    
     





#If the user inputs tip as a float (ie: 0.1) 
bill=float(input('what is your bill amount?'))
tip=float(input('what is your tip percentage in decimal?'))
total=bill*tip
print(total)

#If the user inputs tip as a percentage (ie: 10) 
bill=float(input('what is your bill amount?'))
tip=float(input('what is your tip percentage?'))/100
total=bill*tip
print(total)
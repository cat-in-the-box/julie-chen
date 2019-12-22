#Our neighbor sleeps 9pm - 7am (21:00 to 7:00)
#The bird can’t be noisy while the neighbor is asleep, or we’re in trouble!
#Tell us whether we are in trouble or not
#What variables do I need? time, bird noisy (yes/no)



time=float(input('What is the current hour? Please input 24 HH integer.'))
noisy_bird=input('Is the bird currently noisy? (Y/N)')

if time>=21 or time<=7:
    if noisy_bird=='Y':
        print ('The noisy bird is disturbing the neighbor')
    elif noisy_bird=='N':
        print('The neighbor is sleeping soundly')
        
else:
    print('The neighbor is sleeping soundly')

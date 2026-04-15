   #Eligible for marraige 
gender = input('Enter gender(M/F):')
age = int(input('Enter age:'))
if(gender == 'F'):
    if(age >= 18):
        print('Eligible for marriage.')
    else:
        print('pehle padhai karo.')
else:
    if(age >= 21):
        print('Eligible for marriage.')
    else:
        print('pehle kama lo.')
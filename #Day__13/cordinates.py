# Zip function

names = ['Arup','Arya','Akash','Ritham']
roll = [4,3,2,1]

zipped = zip(roll,names)

setted = set(zipped)
print(setted) # {(3, 'Arya'), (4, 'Arup'), (2, 'Akash'), (1, 'Ritham')}
# output is not fixed


# zip() in forloops

for i,j in zip(names,roll):
    print("Name is {} roll is {} ".format(i,j))

'''Name is Arup roll is 4 
Name is Arya roll is 3 
Name is Akash roll is 2 
Name is Ritham roll is 1 '''

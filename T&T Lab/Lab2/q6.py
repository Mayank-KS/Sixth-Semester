# Delete a list of keys from a dictionary

dictionary = {
    'e1' : 'roll' ,
    'e2' : 'number' ,
    'e3' : 200 ,
    'e4' : 5 ,
    'e5' : 10 ,
    'e6' : 13
    }

li_remove = ['e2', 'e3', 'e4']

for x in li_remove :
    del dictionary[x]
    
print(dictionary.items())
    



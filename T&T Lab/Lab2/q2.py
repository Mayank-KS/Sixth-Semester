# Merge two python dictionaries into one

d1 = {
      'e1' : 69 ,
      'e2' : 96 ,
      'e3' : 11 ,
      'e4' : 22
      }

d2 = {
      'e5' : 200 ,
      'e6' : 5 ,
      'e7' : 10 ,
      'e8' : 13
      }

for x,y in d2.items():
    d1[x] = y
    
print(d1.items())
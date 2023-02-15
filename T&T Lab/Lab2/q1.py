# Convert two lists into a dictionary

l1 = ['A','B','C','D']
l2 = [200,5,10,13]
l3 = {}

y = 0

for x in l1:
    l3[x] = l2[y]
    y=y+1

print(l3)
print(type(l3))
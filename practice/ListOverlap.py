
import numpy as np

# set lists
a = np.array([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],int)
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],int)
c = np.empty(0,int)

for x in a:
    for y in b:
        if x == y:
            if x in c:
                print( x,'already exists')
            else:    
                 c = np.append(c,x)


print(c)            
  
# set a random list
a = np.random.randint(0,20,size=20)
b = np.random.randint(0,16,size=16)
c = np.empty((0,0),int)
print(a)
print(b)
for ii in a:
    for kk in b:
        if ii == kk:
            if ii in c:
                print( ii,'already exists')
            else:    
                 c = np.append(c,ii)


print(c)
   


p = np.array([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],int)
v = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],int)

print(set(p) & set(v))



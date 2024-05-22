l = ["hello","mmy","ds","dsdff"]
y = ["ok","odlfkd","sa","dsds"]
z = len(x)-1
h = []
for k in range(0,z+1):
    g= x[k]+y[k]
    h = h+ [g]
print(h)


#ek do fix karke dusre se ultiply kia hai
k = ["hello","mmy","ds","dsdff"]
y = ["ok","odlfkd","sa","dsds"]
z = [ h+g for h in k for g in y]
print(z)
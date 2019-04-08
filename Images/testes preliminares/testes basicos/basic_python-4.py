A = []
for k in range(10):
    m = -(k-5)**2 + 16
    A.append(m)
print A
max = 0
for x in range(10):
    print A[x]
    if max < A[x]:
        max = A[x]
    print "max local = ", max
print "max global = ", max
    

N=0
M=0
for x in range(5):
    for y in range(x+1):
        N = N + 1
        print "y=", y
        print "N=", N
    for z in range(x+1,6):
        M = M + 1
        print "z=", z
        print "M=", M
        

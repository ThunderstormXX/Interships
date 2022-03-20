J = input()
S = input()

b = set()
cac = int(0) 
for i in range( len( J )):
    b.add(J[i])
for i in range( len( S )):
    if S[i] in b:
        cac +=1       
print( cac)

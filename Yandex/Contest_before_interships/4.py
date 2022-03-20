mass = []
def recursive(str ,N ,k):
    #print( N , " " , k , " " , str)
    if(N != 0):            
        if(N != k):
            recursive(str+"(" , N -1 , k + 1)
        if k != 0:
            recursive(str+")" , N - 1 , k-1 )
    else:
        print(str)

N = int(input())

recursive("",2*N,0)

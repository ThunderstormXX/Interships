
c = int(0)
max1 = int(0)
N = int(input())
for i in range(N):
    x = input()
    if x == "1":
        c+=1
        max1 = max(max1,c)
    else:
        max1 = max(max1,c)
        c = 0
print(max1)
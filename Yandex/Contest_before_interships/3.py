N = int(input())
curr = ""
mass = []
for i in range(N):
    x = input()
    if curr != x :
        mass.append(x)
        curr = x
for i in mass:
    print(i)
str1 = input()
str2 = input()
if(len(str1) != len(str2)):
    print(0)
else:
    dict1 = {}
    dict2 = {}
    for i in str1:
        if dict1.get(i) != None :
            dict1[i] = dict1[i] + 1
        else :
            dict1[i] = 0
    for i in str2:
        if dict2.get(i) != None :
            dict2[i] = dict2[i] + 1
        else :
            dict2[i] = 0    
    
    print( int(dict1 == dict2))
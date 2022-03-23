#FOR AND GENERATORS

#a = range(6) - это ксати класс такой

a = [i**2 for i in range(1,10)]
print(a)
b = [ i/2 for i in a ]
print(b)
c = [ i**2 for i in range(1,10) if i % 3 == 0 ]
print(c)
d = [i for i in open("test.txt")]
print(d)
e = [i for i in range(10,20,3)]                     # С шагом 3 от 10 до 20
print(e)

#OOP in python

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return self.name + " " + str(self.age) 

    # Another instance method
    def speak(self, sound):
        return sound
a =Dog("Inokentiy",19)
print(a.species ," ", a.description())

#Data STRUCTURES


#list
    #methods :
        #len(a) #type(a) # list((a,3,4)) - конструктор для листа( преобразовать к листу)
        # append()	Adds an element at the end of the list
        # clear()	Removes all the elements from the list
        # copy()	Returns a copy of the list
        # count()	Returns the number of elements with the specified value
        # extend()	Add the elements of a list (or any iterable), to the end of the current list
        # index()	Returns the index of the first element with the specified value
        # insert()	Adds an element at the specified position
        # pop()	Removes the element at the specified position
        # remove()	Removes the item with the specified value
        # reverse()	Reverses the order of the list
        # sort()	
a = [1,2,3]
b = [[1 ,2 ,3],[2 , 3 ,4],[4,5,6]]
print(a , " " , type(a))
#dict
    #methods:
        # clear()	Removes all the elements from the dictionary
        # copy()	Returns a copy of the dictionary
        # fromkeys()	Returns a dictionary with the specified keys and value
        # get()	Returns the value of the specified key
        # items()	Returns a list containing a tuple for each key value pair
        # keys()	Returns a list containing the dictionary's keys
        # pop()	Removes the element with the specified key
        # popitem()	Removes the last inserted key-value pair
        # setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
        # update()	Updates the dictionary with the specified key-value pairs
        # values()	Returns a list of all the values in the dictionary
a = { "kek1" : 1 , "kek2" : 2}
print(a["kek1"] , " " , type(a))

#tuple
    #methods:
        # count()	Returns the number of times a specified value occurs in a tuple
        # index()	Searches the tuple for a specified value and returns the position of where it was found
a = (1,2,3)
print(a , " ", type(a) )
#set 
    #methods:
        # add()	Adds an element to the set
        # clear()	Removes all the elements from the set
        # copy()	Returns a copy of the set
        # difference()	Returns a set containing the difference between two or more sets
        # difference_update()	Removes the items in this set that are also included in another, specified set
        # discard()	Remove the specified item
        # intersection()	Returns a set, that is the intersection of two other sets
        # intersection_update()	Removes the items in this set that are not present in other, specified set(s)
        # isdisjoint()	Returns whether two sets have a intersection or not
        # issubset()	Returns whether another set contains this set or not
        # issuperset()	Returns whether this set contains another set or not
        # pop()	Removes an element from the set
        # remove()	Removes the specified element
        # symmetric_difference()	Returns a set with the symmetric differences of two sets
        # symmetric_difference_update()	inserts the symmetric differences from this set and another
        # union()	Return a set containing the union of sets
        # update()	Update the set with the union of this set and others
a = {2 , 1,3}
print(a , " " , type(a))


















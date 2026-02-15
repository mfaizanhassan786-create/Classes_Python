#set is the collection of unordered, immutable and unindexed elements.


Collection = {1, 2, 3, 4, 5}
print(Collection)
print(type(Collection))
print(len(Collection))
print(max(Collection))
print(min(Collection))
print(sum(Collection))
print(sorted(Collection))

#Another:

collection = {"Hello", "World", "Python", "Java", "C++"}
print(collection)
print(type(collection))

#What is the empty set?


Collection = set()

#Some are the elements in the sets.

#Add element:

collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
print(collection)
print(len(collection))
print(sum(collection))
collection.add((5, 6, 7))
# collection.add([8, 9, 10]) #it will the error because the mutable.
print(collection)

# #Remove element:

collection.remove(1)
print(collection)

# #Discard element:

collection.discard(2)
print(collection)

#Clear element:

collection.clear()
print(collection)

#pop element:

collection = {"Hello", "World", "Coding","Python"}
print(collection.pop())
print(collection.pop())
print(collection.pop())


# There are two methods of the sets:
#01.union. (combines both set values & returns new)
#02.Intersaction. (combines common values & return new)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))
 
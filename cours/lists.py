#list (Arrays)

"""
There are four collection data types in the Python programming language:
   1) List - is a collection which is ordered and changeable. Allows duplicate members.
   2) Tuple - is a collection which is ordered and unchangeable. Allows duplicate members.
   3) Set - is a collection which is unordered and unindexed. No duplicate members.
   4) Dictionary - is a collection which is unordered, changeable and indexed. No duplicate members.

"""

#how to create a list
myList = ["Mickael", "Benjamin", "Sebastien", "Djamila", "Benjamin", "Lionel"]
print(myList)

#for access the lists items use index number
print(myList[2]) #will ouput Sebastien
print(myList[-1]) #negative indexing can also be used

#return the range of specifying index
print(myList[3:5])
#negative index can be used also
print(myList[-4:-2])

#change an item in a list
myList[1] = "Cyrielle"
print(myList)

#loop throught a list
for i in myList:
    print(i) #will output all of my list

#check is an item exist in a list
if "Benjamin" in myList:
    print("Yes, Benjamin is in my list" )
else:
    print("Benjamin is not in my list")
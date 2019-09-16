
#Chaine de caractère
string = "Bonjour tout le monde!" 
print(string)

strings = """Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. """

print(strings) #multiline string by using three quotes or three single quotes

#strings are arrays!
print(string[0]) #will output "B"

#you can slice a string by using brackets
print(string[0:7])

#use negative index
print(string[-6:-1])

#know the lenth of a string by using len() function
print("The length of string variable " + str(len(string)))

#function to remove whitespaces strip()
removeWhiteSpaces = "  Bonjour tout le monde  "
print(removeWhiteSpaces) #with spaces
print(removeWhiteSpaces.strip()) #without spaces

stringToLower = "Bonjour Tout Le MONDE!" 
#return to lowercase
print(stringToLower.lower())
#make string to uppercase
print(stringToLower.upper())

#this method replace a string with another string , replace Bonjour with Hello
print(string.replace('Bonjour', 'Hello'))

#this method split a string ito a substring and it finds instances of separator
hello = "bonjour, tout, le, monde"
print(hello.split(","))

#check if a phrase is present in a string or not and return bool 
text =" It was a beautiful day today!"
t = "was" in text  
print(t)    #True
#not in
txt = "was" not in text
print(txt)

#to concatenate two differents variables use +
x = "Bonjour "
y = "tout le monde"
z = x + y
print(z) # output "Bonjour tout le monde

"""
You can't concatenate a string with an integer, you must change his data types
ex : print("Hello number " + 3) - does'nt work
print("Hello number " + str(3)) - work
"""
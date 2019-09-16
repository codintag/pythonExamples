
string = "Bonjour tout le monde"  #str
print(type(string))

integer = 34  
print(type(integer))   #int

flottant = 34.5 
print(type(flottant))  #float

compleks = 2j 
print(type(compleks))  #complex

tab = ["Python", "Django", "Flask"]
print(type(tab))       #list

tuples = ("Python", "Django", "Flask")
print(type(tuples))    #tuple

rnge = range(10)
print(type(rnge))      #range

dictionnaire = {'name': 'Mickael', 'age': 35}
print(type(dictionnaire))  #dic

sept = {"Mickael", "Romain", "Benjamin", "Lionel"}
print(type(sept))       #set

sceptique = frozenset({"Mickael", "Romain", "Benjamin", "Lionel"})
print(type(sceptique)) #frozenset

boolean = True  #or False
print(type(boolean))  #bool

bjr = b"Bonjour"
print(type(bjr))      #bytes

btArr = bytearray(5)
print(type(btArr))    #bytearray

memoire = memoryview(bytes(5))
print(type(memoire))  #memoryview


"""
Constructor functions str("Bonjour"), int(34), float(34.5), complex(1j), list(("Python", "Django", "Flask")), tuple(("Python", "Django", "Flask")), range(6), dict('name': 'Mickael', 'age': 35), set(("Mickael", "Romain", "Benjamin", "Lionel")), frozenset(("Mickael", "Romain", "Benjamin", "Lionel")), bool(5), bytes(5), bytearray(5), memoryview(bytes(5))
"""
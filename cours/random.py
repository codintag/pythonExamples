from random import *

rnd = randint(2, 6) #give you an integer
print(rnd)


n = random()
print(n) #give a number between 0 and 1

x = uniform(12, 18)
print(x) #give a float number


liste = [ "Mickael", "Lionel", "Djamila", "Benjamin"]
résultat = choice(liste)
print(résultat)  # choose an element in a list

letters = ["a", "b", "c", "d", "e"]
shuffle(letters)
print(letters) #shuffle a list shuffle(liste)
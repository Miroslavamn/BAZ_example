# Diccionario
# 1. Crear un diccionario donde cuentes las veces que aparece cada nombre en 'dogs'
# 2. Imprime la cantidad de prerros que se llaman 'Rocky' y 'Sparky'
# 3. Imprime la lista con los diferentes nombres de perros
from collections import defaultdict

dogs = ['Sparky', 'Hunter', 'Loki', 'Astro', 'Sparky', 'Rocky', 'Rocky', 'Toby', 'Chelsea', 'Maple', 'Maya', 'Loki',
        'Sparky', 'Toby', 'Sparky', 'Dexter', 'Fido', 'Sparky']

# 2. Imprime la cantidad de prerros que se llaman 'Rocky' y 'Sparky'
dog_dict = defaultdict (int)
for dog in dogs:
    dog_dict [dog]+= 1
print('Rocky:', dog_dict['Rocky'])
print('Sparky:', dog_dict['Sparky'])

# 3. Imprime la lista con los diferentes nombres de perros
print('Lo nombres son:', list(dog_dict.keys()))
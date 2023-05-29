#Diccionario
#1. Crear un diccionario donde cuentes las veces que aparece cada nombre en 'dogs'
#2. Imprime la cantidad de prerros que se llaman 'Rocky' y 'Sparky'
#3. Imprime la lista con los diferentes nombres de perros

if __name__ == '__main__':
    dogs = ['Sparky', 'Hunter', 'Loki', 'Astro', 'Sparky', 'Rocky', 'Rocky', 'Toby', 'Chelsea', 'Maple', 'Maya', 'Loki',
            'Sparky', 'Toby', 'Sparky', 'Dexter', 'Fido', 'Sparky']
    valor1 = 'Sparky'
    valor2 = 'Rocky'

    freq = dogs.count(valor1)
    freq2 = dogs.count(valor2)

    # 2. Imprime la cantidad de prerros que se llaman 'Rocky' y 'Sparky'
    print("La cantidad de perros que se llaman Sparky son:", freq, "y los que se llaman Rocky son:", freq2)

    # 3. Imprime la lista con los diferentes nombres de perros


nuevalista = set(dogs)
print("Los diferentes nombres son:", nuevalista)







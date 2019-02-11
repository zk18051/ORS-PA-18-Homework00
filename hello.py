def greet(name, prezime):
    """

    :type prezime: object
    """
    print('Hello there ' +   name +' '+ prezime)
    print(name, prezime)
    print(prezime)

greet('Zijad', 'Kurpejovic')

type(5)
print(type)
korisnik_unio1 = input('Unesite prvi broj: ')
korisnik_unio2 = input('Unesite drugi broj: ')
if (not korisnik_unio1.isnumeric()) or (not korisnik_unio2.isnumeric()):
    print('Nijeste unijeli dobar broj')
    quit()
print(korisnik_unio1)
print (korisnik_unio2)
zbir = int(korisnik_unio1) + int(korisnik_unio2)
print(zbir)

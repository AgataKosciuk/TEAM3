# wersja 1.0
wiek = input("Podaj wiek: ")

if wiek.isdigit() == False:
    exit("Wiek musi być liczbą całkowitą")
wiek = int(wiek)

if wiek>120:
    exit('Wiek jest nieprawidłowy, podaj realny wiek')

if wiek >= 18 and wiek <= 40:
    print("Witaj w naszym sklepie")

elif wiek >= 40 and wiek <= 100:
    print("Witaj w naszym sklepie")
    print("W Twoim wieku alkohol jest niewskazany")

else:
    print("Jesteś za małody. Zapraszamy na Disney.com")

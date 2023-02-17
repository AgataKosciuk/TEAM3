#wiek = input("Podaj wiek użytkownika:")
#sprawdzamy czy podany wiek jest liczbą całkowitą:
#if wiek.isdigit() == False:
#	exit("Wiek musi byc liczna calkowita")
#wiek=int(wiek)
#if wiek>=18 and wiek<=40:
#	print("Witaj w naszym sklepie z alkoholem")
#elif wiek>40:
#	print("Witaj w naszym sklepie z alkoholem")
#	print("Prosze korzystac z umiarem")
#else:
#	exit("Jestes za mlody/a na alkohol. Zapraszamy na disney.com")

#Jesli uzytkownikiem jest kobieta +30 to aperol spritz pierwszy gratis!

region = input("Wybierz region. Wpisz USA dla regionu USA, EUR dla Europy.")

if region == "USA" or region == "EUR":
    pass
else:
    exit("Podaj oznaczenie płci jako USA lub EUR.")

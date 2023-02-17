wiek = input("Podaj wiek użytkownika:")
#sprawdzamy czy podany wiek jest liczbą całkowitą:
if wiek.isdigit() == False:
	exit("Wiek musi byc liczna calkowita")
wiek=int(wiek)
if wiek>=18 and wiek<=40:
	print("Witaj w naszym sklepie z alkoholem")
elif wiek>40:
	print("Witaj w naszym sklepie z alkoholem")
	print("Prosze korzystac z umiarem")
else:
	exit("Jestes za mlody/a na alkohol. Zapraszamy na disney.com")
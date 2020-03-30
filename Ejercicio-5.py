c=float(input("Cantidad a invertir? "))
ie=float(input("Interés porcentual anual? "))
a=int(input("Años?"))
for i in range(a):
    amount *= 1 + ie / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(c, 2)))
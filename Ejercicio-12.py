f=input("Introduce una frase: ")
l=input("Introduce una letra")
c=0
for i in f:
    if i==l:
        c+=1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (l, c, f))
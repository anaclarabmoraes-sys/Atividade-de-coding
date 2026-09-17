a= int(input("Informe o primeiro número: "))
b= int(input("Informe o segundo número: "))

if a % b == 0 or b % a == 0:
    print ("São multiplos.")

else:
    print ("Não são multiplos.")
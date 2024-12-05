positivo = 0
negativo = 0
for x in range (5):
    num = int(input("Digite um numero"))
    
    if num> 0 :
        positivo += 1
        
    if num<0:
        negativo+=1
        
print(f"{positivo} numeros são positivos")

print(f"{negativo} são negativos")

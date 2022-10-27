# 1. Básico: imprime todos los números enteros del 0 al 150.

for i in range(151):
    print(i)


#2. Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.

for i in range(5,1001):
    if i % 5 ==0:
        print (i)



# 3. Contar, a la manera del Dojo: imprime números enteros del 1 al 100. 
#Si es divisible por 5, imprime "Coding” en su lugar. 
#Si es divisible por 10, imprime "Coding Dojo".

for i in range(1, 101):
    if i % 10 == 0:
        print('Coding Dojo')
    elif i % 5 ==0:
        print('Coding')
    else: 
        print(i)


# 4. Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.

ressum = 0
for i in range(0,500001):
    if i % 2 != 0:
        ressum +=i
print (ressum)


# 5. Contador flexible: establece tres variables: lowNum, highNum, mult. 
#Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. 
#Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas).

def contadorflexible(lowNum,highNum,mult):
    for i in range(lowNum,highNum+1):
        if i % mult == 0:
            print(i)
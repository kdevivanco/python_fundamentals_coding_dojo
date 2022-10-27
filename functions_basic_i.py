#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

# retorna 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# No se ha definido la primera funcion, botará un error : NameError

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# retorna 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# retorna solo 5 porque el print viene despues (no imprime el 10)


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# x = NoneType porque se llama a print y no a return
# imprime 5, imprime None

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#Imprime 3, Imprime 5 y nos bota un error porque no se puede sumar dos None

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# imprime 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# imprime 100, retorna 10 (no se llega al "return 7" porque cumple la segunda condicion)

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b < c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
'''
Imprime: 
7
14
21
'''


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# imprime 8
# no se llega al segundo return

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
'''
500
500
300
500
# Esto sucede porque b en el 'enviornment' global es b = 500, pero localmente
para la funcion b es 300, es como si fueran dos variables distintas
'''


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
'''
500
500
300
500
'''


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
'''
500
500
300
300
# b es asignada al valor del return de foobar = 300, por eso es sobreescrita en la linea
134 y cuando se imprime ahora es ese nuevo valor = 300
'''



#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

'''
imprime 1 (funcion foo)
imprime 3 (llama a la funcion bar())
imprime 2 (funcion foo)
'''

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

'''
1
3
5
10
#lo mismo que en la anterior pero ahora la funcion foo retorna 10, 
esto se almacena en y al hacer y = foo()
y luego se imprime cuando se pasa print(y)
'''


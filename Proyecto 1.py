# Proyecto final en consola
#Benjamin Calle Macusaya
def suma ():
    SW2 = True
    while SW2 == True:
        print(f'Introduzca los valores que desea sumar: ')
        a = float(input('Valor 1: '))
        b = float(input('Valor 2: '))
        oper=a+b
        print(f'La suma de {a} y {b} es: {round(oper,3)}')
        print(f'¿Quiere realizar otra suma?')
        YN = input('Yes(Y)/No(N): ')
        m = YN.upper()
        if m == 'Y':
            SW2 = True
        else:
            SW2 = False
        SW = False

def resta ():
    SW2 = True
    while SW2 == True:
        print(f'Introduzca los valores que desea restar: ')
        a = float(input('Valor 1: '))
        b = float(input('Valor 2: '))
        oper = a-b
        print(f'La resta de {a} y {b} es: {round(oper,3)}')
        print(f'¿Quieres realizar otra resta?')
        YN2 = input('Yes(Y)/No(N): ')
        m2 = YN2.upper()
        if m2 == 'Y':
            SW2 = True
        else:
            SW2 = False
        SW = False

def multiplicacion ():
    SW2 = True
    while SW2 == True:
        print(f'Introduzca los valores que desea multiplicar: ')
        a = float(input('Valor 1: '))
        b = float(input('Valor 2: '))
        oper = a*b
        print(f'La multiplicación de {a} y {b} es: {round(oper,3)}')
        print(f'¿Quieres realizar otra multiplicación?')
        YN2 = input('Yes(Y)/No(N): ')
        m2 = YN2.upper()
        if m2 == 'Y':
            SW2 = True
        else:
            SW2 = False
        SW = False

def division ():
    SW2 = True
    while SW2 == True:
        print(f'Introduzca los valores que desea dividir: ')
        a = float(input('Valor 1: '))
        b = float(input('Valor 2: '))
        oper = a/b
        print(f'La división de {a} y {b} es: {round(oper,3)}')
        print(f'¿Quieres realizar otra división?')
        YN2 = input('Yes(Y)/No(N): ')
        m2 = YN2.upper()
        if m2 == 'Y':
            SW2 = True
        else:
            SW2 = False
        SW = False

menu = ''' MENU DE OPERACIONES
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir del programa'''
print(f'CALCULADORA EN PYTHON')
SW = True

while SW == True:
    print(f'{menu}')
    ope = int(input(f'Introduzaca el numero de operacion que desea: '))
    if ope == 1:
        print(suma())
    elif ope == 2:
        print(resta())
    elif ope == 3:
        print(multiplicacion())
    elif ope == 4:
        print(division())
    elif ope == 5:
        print(f'Programa finalizado')
        SW = False
    else:
        print(f'Elija una de las opciones dentro del menu')
        SW = True
# Proyecto final con interfaz de usuario
#Benjamin Calle Macusaya
import tkinter as tk
root = tk.Tk()
valorA = tk.StringVar()
valorB = tk.StringVar()

mensaje = tk.StringVar()


def suma ():
    x = float(valorA.get())
    y = float(valorB.get())
    ope = x + y
    mensaje.set(f'El resultado es: {round(ope, 3)}')
    valorA.set('')
    valorB.set('')

def resta ():
    x = float(valorA.get())
    y = float(valorB.get())
    ope = x - y
    mensaje.set(f'El resultado es: {round(ope, 3)}')
    valorA.set('')
    valorB.set('')

def multiplicacion ():
    x = float(valorA.get())
    y = float(valorB.get())
    ope = x * y
    mensaje.set(f'El resultado es: {round(ope, 3)}')
    valorA.set('')
    valorB.set('')

def division ():
    x = float(valorA.get())
    y = float(valorB.get())
    ope = x / y
    mensaje.set(f'El resultado es: {round(ope, 3)}')
    valorA.set('')
    valorB.set('')

root.geometry('350x370')
root.title('Calculadora con Pycharm')

root.configure(bg="#455A64")

tk.Label(root, text='Calculadora', bg="#455A64", fg='white', font=('', 20)).place(x=100,y=20)


#Suma
tk.Label(root, text='Introduzca sus valores\n(use "." para decimales)', bg="#455A64", fg='white', font=('', 13)).place(x=17, y=95)
tk.Entry(root, justify='center', textvariable=valorA, font=('', 10)).place(x=35, y=180)
tk.Entry(root, justify='center', textvariable=valorB, font=('', 10)).place(x=35, y=210)
tk.Button(root, text='Sumar', bd=0, command=suma).place(x=220, y=100)
tk.Button(root, text='Restar', bd=0, command=resta).place(x=220, y=150)
tk.Button(root, text='Multiplicar', bd=0, command=multiplicacion).place(x=220, y=200)
tk.Button(root, text='Dividir', bd=0, command=division).place(x=220, y=250)


tk.Label(root, textvariable=mensaje, bg="#455A64", fg='white', font=('', 15)).place(x=33, y=310)
tk.Button(root, text='Salir', bd=0, command=root.destroy).place(x=300, y=320)

root.mainloop()
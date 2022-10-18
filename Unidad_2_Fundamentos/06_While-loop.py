'''
Autor:Edgar Francisco Hernandez Mendez 
Fecha:18/10/22
Actividad: modificar el ciclo while para usar una verificación booleana

'''
while True:
    x=input("Enter a number to count to: (Enter q to quit.)")
    if x == 'q' or x == 'quit':
        break

    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
        
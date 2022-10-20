
'''
Autor:Edgar Francisco Hernandez Mendez
Fecha:20/10/22
ACtividad:Create an empty list.

'''

file = open("devices.txt", "a")
while True:
    newItem = input("Nombre del dispositivo: ")
    if newItem == "exit":
        print("All done!")
        break
    file.write(newItem + "\n")
file.close()


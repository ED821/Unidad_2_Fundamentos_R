
'''
Autor:Edgar Francisco Hernandez Mendez
Fecha:20/10/22
ACtividad:Create an empty list.

'''



file=open("devices.txt","r")
for line in file:
    line = line.strip()
    if "Switch" in line:
         print(line)
file.close()








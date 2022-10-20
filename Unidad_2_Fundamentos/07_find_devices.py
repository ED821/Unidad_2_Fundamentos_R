
'''
Autor:Edgar Francisco Hernandez Mendez
Fecha:20/10/22
ACtividad:Create an empty list.

'''



#file=open("devices.txt","r")
#for line in file:
 #   line = line.strip()
  #  if "Switch" in line:
   #      print(line)
#file.close()




file = open("devices.txt", "a")
while True:
 newItem = input("Nombre del dispositivo: ")
 if newItem == "exit":
    print("All done!")
 break
 file.write(newItem + "\n")
file.close()

#devices=[]
#file=open(-"devices.txt","r")
#for item in file:
 #   if "Cual es dispositivo a encontrar" in item.strip:
  #  print(item.strip)
  #devices.append(item.strip())
#file.close()
#print(devices)






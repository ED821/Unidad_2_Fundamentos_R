'''
Autor: Edgar Francisco Hernandez Mendez
Fecha:09/11/2022
Descripción: Este punto final devuelve una lista de empresas que admiten transacciones de entrega de alimentos.
'''
#importamos
import requests
import urllib.parse

#Sustraemos el main api
main_api = "https://api.yelp.com/v3/transactions/delivery/search"
#Obtenemos la clave API
key = "yrDmJpxSP4op4oMQ42TVWSNmFfeBFOoPOujAWaL_E2CFH37OA-g8jmcCPijHo6dIILCa26EjsYh4PcpsXMRKTYeUXpqxpeRIZtR6XTFIuUDSvIOc9sAxiM-zF3lsY3Yx"


#Hacemos un ciclo llamdo while, junto con su  salida
while True:
   location = input("Ingresa tu location: ")
   if location =="salir" or location == "s": 
        break
    
   longitude = input("Ingresa la longitude: ")
   if longitude =="salir" or longitude == "s": 
        break
    
   latitude = input("Ingrese su latitude: ")
   if latitude =="salir" or latitude == "s":
       break   
   headers  =  {'Authorization': 'Bearer %s' % key}
   parametros = {"location ": location, 
                 "longitude": longitude,
                 "latitude": latitude }


   url_status = requests.get(main_api, headers=headers, params=parametros)
   json_data = url_status.json()
   json_status = json_data['businesses']
   #print(json_data)
   
   
   #Declarmso un IF y pedimos especificamente algunos datso
   if str(url_status) == "<Response [200]>":
            print("API Status: " + str(url_status) + " = A successful route call.\n")
            entregas_de_alimentos = url_status.json()['total']
            query = url_status.json()['businesses']
            for q in query:
                print(" ENTREGA DE ALIMENTOS ")
                print('==================================================================================')                   
                print("Número de entregas: ",entregas_de_alimentos)
                print("Nombre del location: {}".format(q['alias']))
                print("Ciudad en la que se encuentra: {}".format(q['url'])) 
                print('====latitude================latitude========================================')  
   elif str(url_status) == "<Response [400]>":
                print("****************")
                print("For Staus Code: " + str(url_status) + "; Invalid user inputs for one or both locations.")
                print("****************\n")
                print("=============================================")
   else:
                print("************************")
                print("For Staus Code: " + str(url_status) + ", Refer to:")
                print("https://www.yelp.com/developers/documentation/v3/transaction_search")
                print("************************\n")
   
   







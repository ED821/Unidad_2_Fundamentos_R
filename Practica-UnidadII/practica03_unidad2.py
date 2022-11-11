'''
Autor: Edgar Francisco Hernandez Mendez
Fecha:09/11/2022

Descripción: Este punto final devuelve una lista de empresas según el número de teléfono proporcionado. 
    Es posible que más de una empresa tenga el mismo número de teléfono
  
'''
#Hacemos una importacion 
import requests
#Obtenermos las API
main_api = "https://api.yelp.com/v3/businesses/search/phone"
#Sustraemos la KEY
key = "yrDmJpxSP4op4oMQ42TVWSNmFfeBFOoPOujAWaL_E2CFH37OA-g8jmcCPijHo6dIILCa26EjsYh4PcpsXMRKTYeUXpqxpeRIZtR6XTFIuUDSvIOc9sAxiM-zF3lsY3Yx"
#Hacemos un ciclo while, junto una salida predeterminada 
while True:
    phone = input("Ingresa tu numero de telefono ejm. +14159083801: ")
    if phone == "salir" or phone == "s":
        break
    locale = input("Ingresa tu localidad ejm. en_US: ")
    if locale == "salir" or locale == "s":
        break
    headers  =  {'Authorization': 'Bearer %s' % key}
    parametros = {"phone": phone, 
                 "locale": locale}

    url_status = requests.get(main_api, headers=headers, params=parametros)
    json_data = url_status.json()
    json_status = json_data ['businesses']
    print(json_status)
    
    #Se declaran IF Y ELIF, junto con datos especificos de la API
    if str(url_status) == "<Response [200]>":
            print("API Status: " + str(url_status) + " = A successful route call.\n")
            num_lugares = url_status.json()['total']
            query = url_status.json()['businesses']
            for q in query:
                print("INFORMACIÓN DE LOS LUGARES")
                print('==================================================================================')                   
                print("Número de lugares encontrados: ",num_lugares)
                print("Nombre del lugar: {}".format(q['alias']))
                print("Telefono: {}".format(q['phone']))
                print("Radio: {}".format(q['rating']))
                print('==================================================================================')  
    elif str(url_status) == "<Response [400]>":
                print("****************")
                print("For Staus Code: " + str(url_status) + "; Invalid user inputs for one or both locations.")
                print("****************\n")
                print("=============================================")
    else:
                print("************************")
                print("For Staus Code: " + str(url_status) + ", Refer to:")
                print("https://www.yelp.com/developers/documentation/v3/business_search")
                print("************************\n")
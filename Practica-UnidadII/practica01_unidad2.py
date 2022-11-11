'''
Autor: Edgar Francisco Hernandez Mendez
Fecha:09/11/2022


Nombre de API: Registered Domain Names Search

Descripción: La búsqueda de dominios registrados
             comprueba las listas de dominios registrados 
             en busca de nombres que contengan determinadas 
             palabras/frases/números o símbolos.V
'''
# Importamos algunas librerias
import requests
import urllib.parse


# Agregamos la URL de la API
main_api = "https://api.domainsdb.info/v1/domains/search?"
while True:
    # El ciclo optiene la busqueda de dichos doiminios
    dominio = input(
        "Ingrese el palabra, frase, numero de un dominio que quiera buscar: ")
    if dominio == "Salir" or dominio == "s":
        break
    url = main_api + urllib.parse.urlencode({"domain": dominio})
    print(url)

    json_data = requests.get(url).json()
    
    print("total de articulos: " + str(json_data ['total']))
    print("tiempo de busqueda: " + str(json_data ['time']))
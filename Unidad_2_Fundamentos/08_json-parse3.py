'''
Autor:Edgar Francisco Hernandez Mendez
Fecha:25/10/22
Actividad:Añadir entrada de usuario para la dirección

'''
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = ""
dest = ""
key  = "YqnZF5cYJWqfhyTkWuiOacgC11Yjtpcq"
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")

while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

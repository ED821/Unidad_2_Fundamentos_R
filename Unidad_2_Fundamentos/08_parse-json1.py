'''
Autor:Edgar Francisco Hernandez Mendez
Fecha:25/10/22
Actividad:Probar la solicitud de URL

'''
from ast import main
from sys import orig_argv
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Higalgo Guanajuato"
dest = "Mexico"
key  = "YqnZF5cYJWqfhyTkWuiOacgC11Yjtpcq"
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})


json_data = requests.get(url).json()
print(json_data) 
 

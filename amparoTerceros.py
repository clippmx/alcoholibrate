import requests, json

#url = 'http://localhost:8888/webservices/usuarios/amparo-terceros'

url = 'http://alcoholibrate.mx/webservices/usuarios/amparo-terceros'


params = {
	'idUsuario' : '9',
	'nombre':'Cesar',
	'apellidos':'Alvarez',
	'ubicacion': 'DF',
	'telefono': '12345678'
	}


# Headers necesarios
headers = {'Content-Type': 'application/json'}

r = requests.get(url, data=json.dumps(params), headers=headers)

print r.text
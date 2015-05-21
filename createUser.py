import requests, json

#url = 'http://localhost:8888/webservices/usuarios/create/'

url = 'http://alcoholibrate.mx/webservices/usuarios/registro'


params = {
	'nombre':'Ricardo',
	'apellidos':'Boy',
	'correo': 'richieboy@hotmail.com',
	'password': 'avalos123',
	'telefono': '12312345',
	'ubicacion': 'DF',
	'idTarjeta': '1234567890',
	'telefono2': '12312345',
	}


# Headers necesarios
headers = {'Content-Type': 'application/json'}

r = requests.post(url, data=json.dumps(params), headers=headers)

print r.text
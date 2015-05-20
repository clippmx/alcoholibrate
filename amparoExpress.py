import requests, json

#url = 'http://localhost:8888/webservices/usuarios/amparo-express'

url = 'http://alcoholibrate.mx/webservices/usuarios/amparo-express'


params = {
	'nombre':'Cesar',
	'apellidos':'Alvarez',
	}


# Headers necesarios
headers = {'Content-Type': 'application/json'}

r = requests.post(url, data=json.dumps(params), headers=headers)

print r.text
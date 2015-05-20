import requests, json

#url = 'http://localhost:8888/webservices/usuarios/amparo'

url = 'http://alcoholibrate.mx/webservices/usuarios/amparo'

params = {
	'idUsuario': '2'
	}

# Headers necesarios
headers = {'Content-Type': 'application/json'}

r = requests.post(url, data=json.dumps(params), headers=headers)

print r.text
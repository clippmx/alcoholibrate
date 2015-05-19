import requests, json

#url = 'http://localhost:8888/webservices/usuarios/status-amparo-terceros'

url = 'http://alcoholibrate.mx/webservices/usuarios/status-amparo-terceros'

params = {
	'idAmparoTercero': '1'
	}

# Headers necesarios
headers = {'Content-Type': 'application/json'}

r = requests.get(url, data=json.dumps(params), headers=headers)

print r.text
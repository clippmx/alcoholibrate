import requests, json

#url = 'http://localhost:8888/webservices/usuarios/status-amparo-express'

url = 'http://alcoholibrate.mx/webservices/usuarios/status-amparo-express'

params = {
	'idAmparoExpress': '1'
	}

# Headers necesarios
headers = {'Content-Type': 'application/json'}

r = requests.post(url, data=json.dumps(params), headers=headers)

print r.text
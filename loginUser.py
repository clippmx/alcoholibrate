import requests, json

#url = 'http://localhost:8888/webservices/usuarios/login'

url = 'http://alcoholibrate.mx/webservices/usuarios/login'

params = {
	'correo': 'jhonzya@hotmail.com',
	'password': 'jhonzya123'
	}

# Headers necesarios
headers = {'Content-Type': 'application/json'}

r = requests.get(url, data=json.dumps(params), headers=headers)

print r.text
import json

import requests

# link = "https://webhook-test.com/4aaa251bae9968476de62359c4933eea"
link = "https://n8n.tecnotriks.com.br/webhook/78e10a2a-75fc-4e7e-8769-08534c79d7d2"

data = {
    "pergunta": "Matheus Campos",
    "nome": "Bruno",
    "idade": 40
}

data_json = json.dumps(data)

print(data_json)

response = requests.post(link, json=data_json)

print(response.json())

import json #importa a biblioteca 'json'

items = [
    {
        "id": 1,
        "nome": "bagulho",
        "description": "apenas um bagulho",
        "location": "em uma caixa"
    }, {
        "id": 2,
        "name": "tranqueira",
        "description": "apenas uma tranqueira",
        "location": "em um gaveteiro"
    }, {
        "id": 3,
        "name": "parada",
        "description": "apenas uma parada", 
        "location": "na esquina"
    }
]

def get_all():
    var_json = json.dumps(items, indent=4) #converte o dicionario 'items' para json e armazenar em var_json
    print(var_json) #imprime o json
    
def get_one(id):
    var_json = json.dumps(items, indent=4)
    print(var_json)
    
#get_all()
get_one(1)

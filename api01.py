#importa a biblioteca 'json'.
import json

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
    # converte o dicionario 'items' para json e armazenar em var_json
    var_json = json.dumps(items, indent=4)
    
    #imprime o json
    print(var_json)
    
def get_one(id):
    var_json = json.dumps(items, indent=4)
    print(var_json)
    
#get_all()
get_one(1)

import json

items = [
    {
        "id": 1,
        "nome": "bagulho",
        "description": "apenas um bagulho",
        "location": "em uma caixa"
    }, 
    {
        "id": 2,
        "name": "tranqueira",
        "description": "apenas uma tranqueira",
        "location": "em um gaveteiro"
    }, 
    {
        "id": 3,
        "name": "parada",
        "description": "apenas uma parada", 
        "location": "na esquina"
    }
]

def get_all():
    var_json = json.dumps(items, indent=2)
    return var_json
    
def get_one(id):
    var_json = json.dumps(items[id], indent=2)
    return var_json
    
print (get_all())
print (get_one(1))

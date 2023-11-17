# -*- coding: utf-8 -*-

# Importa bibliotecas.
from flask import Flask, jsonify, request, abort, make_response, json, Response
import sqlite3

# Cria aplicativo Flask.
app = Flask(__name__)

# Configura o character set das transações HTTP para UTF-8.
json.provider.DefaultJSONProvider.ensure_ascii = False

# Especifica a base de dados SQLite3.
database = "./db/temp_db.db"

# Obtém todos os registros válidos de 'item'.
# Request method → GET
# Request endpoint → /items
# Response → JSON


@app.route("/items", methods=["GET"])
def get_all():
    try:
        # Conectar ao banco de dados SQLite.
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Consulta SQL para selecionar todos os itens ativos.
        sql = "SELECT * FROM item WHERE item_status != 'off'"
        cursor.execute(sql)
        rows_data = cursor.fetchall()
        conn.close()

        # Converter os resultados em uma lista de dicionários.
        list_data = []
        for row_data in rows_data:
            list_data.append(dict(row_data))

        # Retornar os dados ou um erro se nenhum item for encontrado.
        if list_data:
            return list_data
        else:
            return {"error": "Nenhum item encontrado"}

    # Tratamento de exceções.
    except sqlite3.Error as error:
        return {"error": f"Erro ao acessar o banco de dados: {str(error)}"}
    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}


@app.route("/items/<int:id>", methods=["GET"])
def get_one(id):
    print(f"O ID é {id}")
    return {"Olá": "mundo"}


# Roda aplicativo Flask.
if __name__ == "__main__":
    app.run(debug=True)

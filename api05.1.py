# -*- coding: utf-8 -*-

import json
import sqlite3
import os

# Definição do caminho do banco de dados.
database = './db/temp_db.db'

# Função para obter todos os itens da tabela 'item'.


def get_all_items():
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

# Função para obter um item específico pelo ID.


def get_one_item(id):
    try:
        # Conectar ao banco de dados SQLite.
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Consulta SQL para selecionar um item específico por ID.
        sql = "SELECT * FROM item WHERE item_status != 'off' AND item_id = ?"
        cursor.execute(sql, (id,))
        row_data = cursor.fetchone()
        conn.close()

        # Retornar os dados do item ou um erro se não for encontrado.
        if row_data:
            return dict(row_data)
        else:
            return {"error": "Item não encontrado"}
    
    # Tratamento de exceções.
    except sqlite3.Error as error:
        return {"error": f"Erro ao acessar o banco de dados: {str(error)}"}
    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}


# Limpar a tela do console.
os.system('cls')

# Imprimir todos os itens formatados como JSON.
print(
    json.dumps(
        get_all_items(),
        ensure_ascii=False,
        indent=2
    )
)

print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')

# Imprimir um item específico pelo ID formatado como JSON.
print(
    json.dumps(
        get_one_item(1),
        ensure_ascii=False,
        indent=2
    )
)

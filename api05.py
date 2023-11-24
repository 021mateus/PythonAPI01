# -*- coding: utf-8 -*-

# Importa as bilbiotecas de dependências.
import json
import sqlite3
import os

# Define o banco de dados.
database = './db/temp_db.db'


# Função get_all_items()
# Obtém e retorna todos os registros válidos da tabela 'item'.
# Retorna como uma 'list' de 'dict'.
def get_all_items():

    # Cria uma conexão com o banco de dados SQLite.
    conn = sqlite3.connect(database)

    # Define que a troca de dados entre Python e SQLite acontece na forma de Row (um registro por linha).
    # Isso permite acessar as colunas tanto por índice quanto por nome.
    conn.row_factory = sqlite3.Row

    # Cria um objeto de cursor, utilizado para percorrer os resultados de consultas SQL.
    # Ele permite que você execute comandos SQL, recupere dados do banco de dados e iteraja sobre os resultados.
    # Mantém um 'ponteiro' que indica onde você está nos resultados da consulta, permitindo que você itere sobre eles ou recupere dados específicos.
    cursor = conn.cursor()

    # Query para consultar os registros na tabela 'item'.
    sql = "SELECT * FROM item WHERE item_status != 'off'"

    # Executa o SQL acima no banco de dados.
    cursor.execute(sql)

    # "Puxa" os dados do cursor para o Python, armazenando em 'rows_data'.
    rows_data = cursor.fetchall()

    # Desconecta do banco de dados.
    # Guarda recursos, aumenta a segurança, evita corrupção de dados.
    conn.close()

    # Uma 'list' para armazenar as SQLite.Row no forma de 'dict'.
    list_data = []

    # Loop que obtém cada SLite.Row da memória (rows_data).
    for row_data in rows_data:

        # Converte a SQLite.Row em 'dict' e adiciona no final de 'list_data'.
        list_data.append(dict(row_data))

    # Verifica se há registros antes de retornar...
    if list_data:

        # Se houver registros, retorna tudo.
        return list_data

    else:

        # Se não houver registros, retorna erro.
        return {"error": "Nenhum item encontrado"}


# Função get_one_item(id)
# Obtém um 'item' único e válido do banco de dados, identificado pelo 'id'.
# Retorna como um 'dict'.


def get_one_item(id):

    # Incializa o banco de dados.
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Query de consulta.
    # Observe o curinga '?' no lugar do valor do atributo.
    sql = "SELECT * FROM item WHERE item_status != 'off' AND item_id = ?"

    # Executa o código passando o valor do ID para o curinga na forma de 'tuple'.
    # Observe a vírgula após o 'id' na 'tuple'. Isso evita que a tuple seja interpretada como um parâmetro.
    cursor.execute(sql, (id,))

    # Retorna o resultado da consulta para 'row_data'.
    row_data = cursor.fetchone()

    # Fecha a conexão com o banco de dados.
    conn.close()

    # Se o registro existe...
    if row_data:

        # Converte SQLite.Row para dicionário e retorna.
        return dict(row_data)

    else:

        # Se não encontrar o registro, retorna erro.
        return {"error": "Registro não encontrado"}


# Limpa o console.
os.system('cls')

# Exemplo para obter todos os 'item' válidos.
print(  # Exibe no console.
    json.dumps(  # No formato JSON.
        get_all_items(),  # Os items obtidos desta função.
        ensure_ascii=False,  # Usando a tabela UTF-8 (acentuação).
        indent=2  # Formatando o JSON.
    )
)

print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')

# Exemplo para obter um 'item' pelo ID.
print(
    json.dumps(
        get_one_item(5),
        ensure_ascii=False,
        indent=2
    )
)

-- Apaga as tabelas caso exista
-- CUIDADO! isso 
DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS owner;

-- criar a tabela 'owner'.
CREATE TABLE owner (
    owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    onwer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    owner_name TEXT,
    owner_email TEXT,
    owner_password TEXT,
    owner_birth DATE,
    owner_status TEXT COMMENTS "Valores: on, off",
    owner_field1 TEXT,
    owner_filde2 TEXT
);

-- popular a tabela 'owner' com dados 'fake'.
INSERT INTO owner (owner_id, onwer_date, owner_name, owner_email, owner_password, owner_birth, owner_status)
VALUES
     ('1', '2023-09-28 10:11:12', 'Joca da Silva', 'joca@silva.com', '123', '1988-12-14', 'on'),
	 ('2', '2023-09-28 10:11:12', 'Luca Oliveira', 'luca@oliveira.com', '123', '1990-10-05', 'on'),
	 ('3', '2023-09-28 10:11:12', 'Wesley Braga', 'wesley@braga.com', '123', '2001-09-12', 'off'),
	 ('4', '2023-09-28 10:11:12', 'Ana Vitoria', 'ana@vitoria.com', '123', '1974-05-15', 'off'),
     ('5', '2023-09-28 10:11:12', 'Maria Porto', 'maria@porto.com', '123', '1998-11-23', 'on'),
	 ('6', '2023-09-28 10:11:12', 'Leandro Mello', 'leandro@mello.com', '123', '1999-12-24', 'on'),
	 ('7', '2023-09-28 10:11:12', 'Luis Martins', 'luis@martins.com', '123', '2002-03-10', 'off');
	 
-- crie a tabela 'item'.
CREATE TABLE item (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
	item_date DATETIME DEFAULT CURRENT_TIMESTAMP,
	item_name TEXT,
	item_description TEXT,
	item_location TEXT,
	item_owner INTEGER,
	item_status TEXT DEFAULT 'on',
	item_field1 TEXT,
	item_fild2 TEXT,
	FOREIGN KEY (item_owner) REFERENCES owner (owner_id)
);

-- popula 'item' com dados  'fake' aleatorios.
INSERT INTO item 
(item_date, item_name, item_description, item_location, item_owner, item_status)
VALUES
     ('2023-05-12 14:15:00', 'produto1', 'descrição do produto 1', 'localização 1', 1, 'on'),
	 ('2023-05-13 09:30:00', 'produto2', 'descrição do produto 2', 'localização 2', 2, 'on'),
     ('2023-05-14 15:45:00', 'produto3', 'descrição do produto 3', 'localização 3', 3, 'on'),
     ('2023-05-15 12:00:00', 'produto4', 'descrição do produto 4', 'localização 4', 4, 'on'),
     ('2023-05-16 11:20:00', 'produto5', 'descrição do produto 5', 'localização 5', 5, 'on'),
     ('2023-05-17 14:00:00', 'produto6', 'descrição do produto 6', 'localização 6', 6, 'on'),
     ('2023-05-18 10:10:00', 'produto7', 'descrição do produto 7', 'localização 7', 7, 'on');



    
	 
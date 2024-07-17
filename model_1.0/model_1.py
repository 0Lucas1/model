#Importando o módulo que fornece uma DB-API
import sqlite3

#Criando as classes:


#Classe Jogos:

class Jogos:
    def __init__(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Jogos(
            id_jogo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_jogo VARCHAR(30) NOT NULL,
            descricao VARCHAR(30) NOT NULL,
            D_lancamento VARCHAR(30) NOT NULL,
            C_etaria VARCHAR(30) NOT NULL,
            precoR$ REAL NOT NULL,
            quant_players INTEGER NOT NULL
            );
        """)
        conn.commit()
        conn.close()
        
    def add_game(self, nome: str, descricao: str, DL: str, CE: str, preco: float, quant_players: int):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(f"""
        INSERT INTO Jogos(nome_jogo, descricao, D_lancamento, C_etaria, precoR$, quant_players)
        VALUES('{nome}','{descricao}', '{DL}', '{CE}', {preco}, {quant_players});
        
        """)
        conn.commit()
        conn.close()
        
    def select_games(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Jogos;")
        registros = []
        for registro in cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_jogo': registro[1],
                'descricao': registro[2],
                'data_lancamento': registro[3],
                'classificacao_etaria': registro[4],
                'precoR$': registro[5],
                'quantidade_players': registro[6]
            })
        conn.close()
        return registros
    
    def del_game(self, id: int):
        conn = sqlite3.connect("meuDB.db")
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Jogos WHERE id_jogo = {id};")
        conn.commit()
        conn.close()
        
    def update_game(self, id: int, nome: str, descricao: str, DL: str, CE: str, preco: float, quant_players: int):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE Jogos SET nome_jogo = '{nome}', descricao = '{descricao}', D_lancamento = '{DL}', C_etaria = '{CE}', precoR$ = {preco}, quant_players =  {quant_players}
            WHERE  id_jogo = {id};
            """)
        conn.commit()
        conn.close()
        
    
#Classe Desenvolvedores:

class Desenvolvedores:
    def __init__(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Desenvolvedores(
            id_dev INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_dev VARCHAR(30) NOT NULL
            );
        """)
        conn.close()
        
    def add_dev(self, nome: str):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(f"""
        INSERT INTO Desenvolvedores(nome_dev)
        VALUES('{nome}');
        """)
        conn.commit()
        conn.close()
        
    def select_devs(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Desenvolvedores;")
        registros = []
        for registro in cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_dev': registro[1]
            })
        conn.close()
        return registros
    
    def del_dev(self, id: int):
        conn = sqlite3.connect("meuDB.db")
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Desenvolvedores WHERE id_dev = {id};")
        conn.commit()
        conn.close()
    
    def update_dev(self, id: int, nome: str):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE Desenvolvedores SET nome_dev = '{nome}'
            WHERE  id_dev = {id};
            """)
        conn.commit()
        conn.close()

#Classe Plataformas:

class Plataformas:
    def __init__(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Plataformas(
            id_plata INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_plata VARCHAR(30) NOT NULL,
            fabricante VARCHAR(30) NOT NULL
            );
        """)
        conn.close()
        
    def add_plata(self, nome: str, fabricante: str):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(f"""
        INSERT INTO Plataformas(nome_plata, fabricante)
        VALUES('{nome}', '{fabricante}');
        """)
        conn.commit()
        conn.close()
        
    def select_plata(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Plataformas;")
        registros = []
        for registro in cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_plata': registro[1],
                'frabricante': registro[2]
            })
        conn.close()
        return registros
    
    def del_plata(self, id: int):
        conn = sqlite3.connect("meuDB.db")
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Plataformas WHERE id_plata = {id};")
        conn.commit()
        conn.close()
    
    def update_plata(self, id: int, nome: str, fabricante: str):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE Plataformas SET nome_plata = '{nome}', fabricante = '{fabricante}'
            WHERE  id_plata = {id};
            """)
        conn.commit()
        conn.close()
        
#Classe Gêneros:

class Generos:
    def __init__(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Generos(
            id_gen INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_gen VARCHAR(30) NOT NULL
            );
        """)
        conn.close()
        
    def add_gen(self, nome: str):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(f"""
        INSERT INTO Generos(nome_gen)
        VALUES('{nome}');
        """)
        conn.commit()
        conn.close()
    
    def select_gen(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Generos;")
        registros = []
        for registro in cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_gen': registro[1]
            })
        conn.close()
        return registros
    
    def del_gen(self, id: int):
        conn = sqlite3.connect("meuDB.db")
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Generos WHERE id_gen = {id};")
        conn.commit()
        conn.close()
        
    def update_gen(self, id: int, nome: str):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE Generos SET nome_gen = '{nome}'
            WHERE  id_gen = {id};
            """)
        conn.commit()
        conn.close()
        

#Objetos de cada tabela:

Obj_Jogo = Jogos()
Obj_Dev = Desenvolvedores()
Obj_Plata = Plataformas()
Obj_Gen = Generos()

#Importando tudo do módulo "model"
from model_1 import *

#Classes associativas:

#Classe JogoDev

class JogoDev:
    def __init__(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS JogoDev(
            id_game INTEGER,
            id_developer INTEGER,
            PRIMARY KEY (id_game, id_developer),
            FOREIGN KEY (id_game) REFERENCES Jogos(id_jogo) ON DELETE CASCADE,
            FOREIGN KEY (id_developer) REFERENCES Desenvolvedores(id_dev) ON DELETE CASCADE
            );
        """)
        conn.close()
        
    def add_Jogo_Dev(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id_jogo FROM Jogos;")
        last_value = cursor.fetchall()[-1][0]
        cursor.execute(f"""
                INSERT INTO JogoDev(id_game, id_developer)
                VALUES({last_value}, {last_value});
                """)
        conn.commit()
        conn.close()
            
    def select_associacoesJD(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM JogoDev;")
        registros = []
        for registro in cursor.fetchall():
            registros.append({
                'id_game': registro[0],
                'id_dev': registro[1]
            })
        conn.close()
        return registros
    
#Classe JogoPlata

class JogoPlata:
    def __init__(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS JogoPlata(
            id_game INTEGER,
            id_plataforma INTEGER,
            PRIMARY KEY (id_game, id_plataforma),
            FOREIGN KEY (id_game) REFERENCES Jogos(id_jogo) ON DELETE CASCADE,
            FOREIGN KEY (id_plataforma) REFERENCES Plataformas(id_plata) ON DELETE CASCADE
            );
        """)
        conn.close()
        
    def add_Jogo_Plata(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id_jogo FROM Jogos;")
        last_value = cursor.fetchall()[-1][0]
        cursor.execute(f"""
                INSERT INTO JogoPlata(id_game, id_plataforma)
                VALUES({last_value}, {last_value});
                """)
        conn.commit()
        conn.close()
            
    def select_associacoesJP(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM JogoPlata;")
        registros = []
        for registro in cursor.fetchall():
            registros.append({
                'id_game': registro[0],
                'id_plataforma': registro[1]
            })
        conn.close()
        return registros
    
#Classe JogoGen

class JogoGen:
    def __init__(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS JogoGen(
            id_game INTEGER,
            id_genero INTEGER,
            PRIMARY KEY (id_game, id_genero),
            FOREIGN KEY (id_game) REFERENCES Jogos(id_jogo) ON DELETE CASCADE,
            FOREIGN KEY (id_genero) REFERENCES Generos(id_gen) ON DELETE CASCADE
            );
        """)
        conn.close()
    
    def add_Jogo_Gen(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id_jogo FROM Jogos;")
        last_value = cursor.fetchall()[-1][0]
        cursor.execute(f"""
                INSERT INTO JogoGen(id_game, id_genero)
                VALUES({last_value}, {last_value});
                """)
        conn.commit()
        conn.close()
    
    def select_associacoesJGEN(self):
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM JogoGen;")
        registros = []
        for registro in cursor.fetchall():
            registros.append({
                'id_game': registro[0],
                'id_genero': registro[1]
            })
        conn.close()
        return registros


#Objetos de cada tabela:

Obj_JDEV = JogoDev()
Obj_JPLATA = JogoPlata()
Obj_JGEN = JogoGen()

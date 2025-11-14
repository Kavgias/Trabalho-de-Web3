import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="instituto_tamandua"
    )

def inserir_inscricao(dados):
    con = conectar()
    cursor = con.cursor()
    sql = """INSERT INTO inscricoes (nome, data_nascimento, email, telefone, instagram)
             VALUES (%s, %s, %s, %s, %s)"""
    valores = (dados["nome"], dados["data_nascimento"], dados["email"], dados["telefone"], dados["instagram"])
    cursor.execute(sql, valores)
    con.commit()
    con.close()

def listar_inscricoes():
    con = conectar()
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM inscricoes ORDER BY data_inscricao DESC")
    registros = cursor.fetchall()
    con.close()
    return registros

def deletar_inscricao(id):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM inscricoes WHERE id = %s", (id,))
    con.commit()
    con.close()

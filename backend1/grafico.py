import mysql.connector
import matplotlib.pyplot as plt
from datetime import datetime

def gerar_grafico():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="instituto_tamandua"
    )
    cursor = con.cursor()
    cursor.execute("SELECT MONTH(data_inscricao), COUNT(*) FROM inscricoes GROUP BY MONTH(data_inscricao)")
    dados = cursor.fetchall()
    con.close()

    meses = [datetime(2025, m[0], 1).strftime('%b') for m in dados]
    qtd = [m[1] for m in dados]

    plt.figure(figsize=(7, 5))
    plt.bar(meses, qtd)
    plt.title("Inscrições por Mês")
    plt.xlabel("Mês")
    plt.ylabel("Quantidade")
    plt.savefig("backend/grafico.png")


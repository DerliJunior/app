import os
import pyodbc

database = os.environ.get("DATABASE")
server = os.environ.get("SERVER")
user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
port = os.environ.get("PORT")

stringConnection = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password};PORT={port}"

try:
    conexao = pyodbc.connect(stringConnection)
    cursor = conexao.cursor()
    
    nome = 'Joao'
    ra= '87639'
    id_curso = 1
    semestre = 1
    

    query = f"INSERT INTO alunos (nome, ra, id_curso, semestre) VALUES (?, ?, ?, ?); \
              SELECT @@IDENTITY AS book_id;"

    cursor.execute(query, nome, ra, id_curso, semestre)
    book_id = cursor.fetchone()[0]
    print(book_id)
    cursor.commit()

    # query = f'SELECT * FROM alunos where id = ?'
    # aluno = cursor.execute(query, id_aluno).fetchone()

    # print(f"Nome: {aluno[1]} - RA: {aluno[2]} - Curso: {aluno[3]} - Semestre: {aluno[4]}")

    print('Conectado com sucesso!')
except Exception as err:
    print(f'Erro: {err}')
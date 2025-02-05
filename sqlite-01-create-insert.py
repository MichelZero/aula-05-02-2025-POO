#
# DQL - Linguagem de Consulta de Dados
# DQL - (select)

# DML - Linguagem de Manipulação de Dados (dados)
# DML (insert, update e delete) (insere, atualiza e deleta registros)

# DDL - linguagem de definição e dados (Metadados)
# DDL (create, alter, drop) (cria, altera e deleta as tabelas)

# DCL - Linguagem de Controle de Dados (controle de acesso ao banco)
# DCL (grant e revoke) (adiciona e remove, permissões de acesso)

# DTL - Linguagem de Transação de Dados (gerenciar transações de dados)
# DTL - (begin, commit e rollback) (inicia, confirma e desfaz uma transação)

# vamos usar apenas os seguintes instruções (DQL, DML, DDL e DTL):
# create
# insert
# select
# delete
# update
# commit

# se aparecer o erro 'sqlite3.DatabaseError: database disk image is malformed'
# pode apagar o bando e recomeçar 
# isso aconteceu muito comigo pq o replit caiu muito a conexão enquanto eu estava trabalhando nele

# C -> CREATE
# R -> READ
# U -> UPDATE
# D -> DELETE

'''
1 - importar o SQLite3
2 - criar o banco ou conecta o banco
3 - criar o cursor
4 - SQL (criar tabela, executar instruções SQL)
4.1 - execute
4.2 - para garantir a transação no banco (commit)
4.3 - fechar o banco
'''

# 1 - importar o SQLite3
import sqlite3 as db

# 2 - criar o banco ou conecta o banco
db1 = db.connect("agenda.db")

#3 - criar o cursor
curso = db1.cursor()

# 4 - SQL (criar tabela, executar instruções SQL)
#4.1 - execute
# curso.execute(" código SQL aqui")
#curso.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
curso.execute("CREATE TABLE IF NOT EXISTS pessoas (nome text, idade integer, email text)")

#inserindo dados na tabela pessoas
#  TABLE pessoas (nome text, idade integer, email text)"
curso.execute("INSERT INTO pessoas VALUES('joão', 10, 'joao@gmail.com')")
curso.execute("INSERT INTO pessoas VALUES('pedro', 15, 'pedro@gmail.com')")
curso.execute("INSERT INTO pessoas VALUES('paulo', 20, 'paulo@gmail.com')")

#4.2 - para garantir a transação no banco (commit)
db1.commit()

#4.3 - fechar o banco
#db1.close()

############# select  ############################
sql_select = "SELECT * FROM pessoas"
curso.execute(sql_select)
#print(type(curso.fetchall()))
#print(curso.fetchall())
tabela = curso.fetchall()
for i in tabela:
  print(i)
  
# fechar DB
#db1.close()

#################### delete ######################
try:
  # correto
  sql_delete = "DELETE from pessoas WHERE idade = 10"
  curso.execute(sql_delete)
  db1.commit()
  
  # printar a tabela
  curso.execute(sql_select)
  print(curso.fetchall())
  #db1.close()
  print("dados removidos!")
  
except Exception as e:
  print(str(e))

#################### update ######################
try:
  sql_update = "UPDATE pessoas SET idade = 25 WHERE nome = 'pedro'"
  curso.execute(sql_update)
  
  # printar a tabela
  curso.execute(sql_select)
  print(curso.fetchall())
  db1.close()
  print("update realizado!")
except Exception as e:
  print(str(e))
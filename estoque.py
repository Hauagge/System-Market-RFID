from psycopg2 import psycopg2




def conecta_db():
  con = psycopg2.connect(host='localhost', 
                         database='estoque',
                         user='postgres', 
                         password='docker')
  return con



def inserir_db(sql, value):
    con = conecta_db()
    cur = con.cursor()
    try:
        cur.execute(sql,value)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

def consultar_db(sql):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(sql)
  recset = cur.fetchall()
  registros = []
  for rec in recset:
    registros.append(rec)
  con.close()
  return registros
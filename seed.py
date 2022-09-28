import psycopg2 
from uuid import uuid4
import csv
from lib.interface import read_tag




def seed(sql, values):

    con = psycopg2.connect(
        host='localhost', 
        database='estoque',
        user='postgres', 
        password='docker')
    cur = con.cursor()
    print("Connecction susccess")
    # sql = 'CREATE TABLE IF NOT EXISTS estoque (id serial primary key, name varchar(100),EPC varchar(50), price INT)'
    # cur.execute(sql)
    print(sql, values)
    cur.execute(sql,values)
    con.commit()
    # cur.execute('select * from estoque')
    # recset = cur.fetchall()
    # for rec in recset:
    #     print(rec)

    # for i in dados.index:
    #     sql = """
    #     INSERT into public.deputados (id,uri,nome,siglaPartido,uriPartido,siglaUf,idLegislatura,urlFoto,email) 
    #     values('%s','%s','%s','%s','%s','%s','%s','%s','%s');
    #     """ % (myuuid, df['uri'][i], df['nome'][i], df['siglaPartido'][i], df['uriPartido'][i], df['siglaUf'][i], df['idLegislatura'][i], df['urlFoto'][i], df['email'][i])
    #     inserir_db(sql)


    con.close()



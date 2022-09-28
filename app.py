from time import sleep
from turtle import clear
from typing import ValuesView
from psycopg2 import *
from center import *
from lib.interface import read_tag
from tkinter import *

def getOneFromDB(value):
    try:
        con = connect(host='localhost', 
                database='estoque',
                user='postgres', 
                password='docker')
        cur = con.cursor()
        cur.execute("SELECT name, price FROM estoque WHERE epc LIKE %s",[value])
        data = cur.fetchone()
        qntdEspaco = 60 - len(str(data[0]))
        espacos = qntdEspaco * "."
  
        content = str(data[0])+ espacos + "R$" + str(data[1])
    
        return content
    except(Exception, DatabaseError) as error:
        print(error)

def getFromDB():
    try:
        con = connect(host='localhost', 
                database='estoque',
                user='postgres', 
                password='docker')
        cur = con.cursor()
        sql = "select epc from estoque limit 15"
        cur.execute(sql)
        data = cur.fetchall()

        return data
    except(Exception, DatabaseError) as error:
        print(error)
   
def tags_read():
 
    tags = read_tag()
 
    for row in tags:
   
        product =  getOneFromDB(row)
        print(product)
        
        texto_leituras.insert(END,product)

root = Tk()
root.title('Sistema')
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

texto_orientacao = Label(root, text ="Realizar Leituras")
texto_orientacao.grid(column=1, row=0, padx=10, pady=10)


frame1=Frame(root)
frame1.grid(column=1, row=2,sticky='NS')


texto_leituras = Listbox(frame1)
texto_leituras.grid(padx=10,pady=10)
texto_leituras.config(width=50,height=30)


# texto_leituras.grid(column=1, row=2,  padx=400, pady=20 )


botao = Button(root, text ="Realizar Leitura",command=tags_read )
botao.grid(column=1, row=3, padx=10, pady=10)

root.mainloop()

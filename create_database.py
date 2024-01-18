import sqlite3 

connection = sqlite3.connect('laic.db')
cursor = connection.cursor()
print('Database Initialization')


table = """CREATE TABLE Classe_1 (
            Visites INTEGER,
            Iprimes INTEGER,
            V_Monetaire REAL,
            P_Secourues INTEGER,
            H_Medicales INTEGER,
            E_Bibliques INTEGER
); """

table_2 = """CREATE TABLE Classe_2 (
            Visites INTEGER,
            Iprimes INTEGER,
            V_Monetaire REAL,
            P_Secourues INTEGER,
            H_Medicales INTEGER
            E_Bibliques INTEGER
); """

table_3 = """CREATE TABLE Classe_3 (
            Visites INTEGER,
            Iprimes INTEGER,
            V_Monetaire REAL,
            P_Secourues INTEGER,
            H_Medicales INTEGER,
            E_Bibliques INTEGER
); """

table_4 = """CREATE TABLE Classe_4 (
            Visites INTEGER,
            Iprimes INTEGER,
            V_Monetaire REAL,
            P_Secourues INTEGER,
            H_Medicales INTEGER,
            E_Bibliques INTEGER
); """

table_5 = """CREATE TABLE Classe_5 (
            Visites INTEGER,
            Iprimes INTEGER,
            V_Monetaire REAL,
            P_Secourues INTEGER,
            H_Medicales INTEGER,
            E_Bibliques INTEGER
); """


cursor.execute(table)
cursor.execute(table_2)
cursor.execute(table_3)
cursor.execute(table_4)
cursor.execute(table_5)

print('Table is ready')
connection.close()




root.mainloop()

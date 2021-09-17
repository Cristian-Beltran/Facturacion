import cx_Oracle
ip = '192.168.2.250' #ip
port = 1521  #port
SID = 'ATBPRU'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
connect = cx_Oracle.connect('FA53', 'FA53', dsn_tns)

cursor = connect.cursor()
cursor.execute('SELECT * FROM NAF')
registros = cursor.fetchall()
for r in registros:
    print(str(r))

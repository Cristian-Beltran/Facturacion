import cx_Oracle

connection = cx_Oracle.connect("FA53/FA53@192.168.2.250:1521/ATBPRU")
print("Connection ..... OK")
cursor = connection.cursor()
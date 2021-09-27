import cx_Oracle

connect = cx_Oracle.connect("FA53/FA53@192.168.2.250:1521/ATBPRU")
sql = """
       select * for interfaz_fe  
        """
print("Conexion correcta")
cursor = connect.cursor()


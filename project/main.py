from flask import Flask,render_template
import cx_Oracle

app = Flask(__name__)
connection = cx_Oracle.connect("FA53/FA53@192.168.2.250:1521/ATBPRU")
cursor = connection.cursor()

     

@app.route('/')
def index():
    sql = """
        select NO_DOCU,GRUPO,NO_CLIENTE,FECHA,TOTAL,COD_CONTROL,CENTROD,TIPO_DOC,RUTA,NO_ORDEN
        FROM interfaz_fe
        where no_cia='01'  
        and origen='TV'
        and impreso='S'
        and to_char(fecha,'yyyy')=to_char('2019')
        and no_docu||no_orden||TIPO_DOC in (select distinct(no_factu||no_f300||tipo_doc)
        from ARFAFL_DET
        where no_cia='01'
        and periodo = '2019')
        order by fecha,no_docu;        j
    """
    result = cursor.execute(sql)
    contex = {
        'DATA':result
    }
    return render_template('index.html',contex=contex) 
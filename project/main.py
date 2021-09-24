from flask import Flask,render_template
from db import table,header,details
from app import create_app
from forms import FilterForm

app = create_app()

@app.route('/',methods=['GET', 'POST'])
def index(): 
    filter_form = FilterForm()
    fecha = '2021'
    if filter_form.validate_on_submit():
        fecha = (filter_form.fecha.data)
        print(fecha)
    data = table(fecha) 
    contex = {
        'DATA':data,
        'filter':filter_form
    }
    return render_template('index.html',contex=contex) 

@app.route('/download/<string:no_docu>/<string:grupo>/<string:no_cliente>/<string:centrod>/<string:tipo_doc>/<string:ruta>/<string:no_orden>')
def download_fact(no_docu,grupo,no_cliente,centrod,tipo_doc,ruta,no_orden):
    head = header(centrod,tipo_doc,no_docu,ruta,grupo,no_cliente,no_orden)
    detail = details(centrod,tipo_doc,ruta,no_orden,no_docu)
    contex = {
        'head' : head,
        'detail': detail,
    }
    return render_template('print.html',contex=contex)

@app.route('/print/<string:no_docu>/<string:grupo>/<string:no_cliente>/<string:centrod>/<string:tipo_doc>/<string:ruta>/<string:no_orden>')
def print_fact(no_docu,grupo,no_cliente,centrod,tipo_doc,ruta,no_orden):
    head = header(centrod,tipo_doc,no_docu,ruta,grupo,no_cliente,no_orden)
    detail = details(centrod,tipo_doc,ruta,no_orden,no_docu)
    contex = {
        'head' : head,
        'detail': detail,
    }
    return render_template('print.html',contex=contex)

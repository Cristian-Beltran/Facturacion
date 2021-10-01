from flask import Flask,render_template,jsonify,request,redirect,url_for
from db import table,header,details,clientes,cliente,arfapar,insert_cabecera,insert_detalle
from app import create_app
from forms import FilterForm,RegisterFactu
from pdf import printPDF
from datetime import datetime
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

@app.route('/facturacion',methods=['GET', 'POST'])
def facturacion():    
    factu_form = RegisterFactu()
    if request.method=='POST':
        now = datetime.now()
        data = arfapar()
        orden = data[0]
        no_docu = data[1] +1
        grupo = (factu_form.grupo.data)
        if int(grupo) < 50:
            ruta = '01'
        else:
            ruta = '02'
        cliente = (factu_form.cliente.data)
        no_ruc = (factu_form.no_ruc.data)
        nbr_cliente =(factu_form.nbr_cliente.data)
        direccion = (factu_form.direccion.data)
        observ1 = (factu_form.observ1.data)
        total_items = (factu_form.total_items.data)
        tipo_doc_ref = (factu_form.tipo_doc_ref.data)
        ruta_ref = (factu_form.ruta_ref.data)
        no_docu_ref = (factu_form.no_docu_ref.data)
        moneda  = (factu_form.moneda.data)

        no_arti = (factu_form.no_arti.data)
        precio = (factu_form.precio.data)
        no_item_ref = (factu_form.no_item_ref.data)
        nivel = (factu_form.nivel.data)
        spot = (factu_form.spot.data)
        segundo = (factu_form.segundo.data)
        fech_ini = (factu_form.fech_ini.data)
        fech_fin = (factu_form.fech_fin.data)
        pases = (factu_form.pases.data)
        programa = (factu_form.programa.data)
        detalle = (factu_form.detalle.data)
        insert_cabecera(no_docu,ruta,grupo,cliente,no_ruc,nbr_cliente,direccion,now.date(),observ1,total_items,precio-(precio*.13),precio*.13,precio,tipo_doc_ref,ruta_ref,no_docu_ref,orden,moneda)

        insert_detalle(no_docu,ruta,1,no_arti,precio,precio-(precio*.13),precio*.13,no_item_ref,orden,now.year,now.date(),nivel,spot,segundo,fech_ini,fech_fin,pases,programa,(precio-(precio*0.13))/pases,detalle)
        return redirect(url_for('index'))
    contex = {
        'factu_form':factu_form,
    }
    return render_template('factura.html',contex=contex) 



@app.route('/download/<string:no_docu>/<string:grupo>/<string:no_cliente>/<string:centrod>/<string:tipo_doc>/<string:ruta>/<string:no_orden>')
def download_fact(no_docu,grupo,no_cliente,centrod,tipo_doc,ruta,no_orden):
    head = header(centrod,tipo_doc,no_docu,ruta,grupo,no_cliente,no_orden)
    detail = details(centrod,tipo_doc,ruta,no_orden,no_docu)
    print(type(head))
    contex = {
        'head' : head,
        'detail': detail,
    }
    printPDF()
    return render_template('print.html',contex=contex)

@app.route('/print/<string:no_docu>/<string:grupo>/<string:no_cliente>/<string:centrod>/<string:tipo_doc>/<string:ruta>/<string:no_orden>')
def print_fact(no_docu,grupo,no_cliente,centrod,tipo_doc,ruta,no_orden):
    head = header(centrod,tipo_doc,no_docu,ruta,grupo,no_cliente,no_orden)
    detail = details(centrod,tipo_doc,ruta,no_orden,no_docu)
    contex = {
        'head' : head,
        'detail': detail
    }
    return render_template('print.html',contex=contex)








"""Direcciones para obtener una lista completa de los grupos y los clientes"""

@app.route('/_get_clientes/<string:grupo>')
def _get_clientes(grupo):
    clientes_data = clientes(grupo)
    clientes_array = []
    for cliente in clientes_data:
        cliente_obj= {}
        cliente_obj['id'] = cliente[0]
        cliente_obj['name'] = cliente[1]
        clientes_array.append(cliente_obj)
    
    return jsonify({'clientes':clientes_array})

@app.route('/_get_cliente/<string:no_cliente>')
def _get_cliente(no_cliente):
    cliente_data = cliente(no_cliente)
    cliente_obj={}
    cliente_obj['cedula'] = cliente_data[1] 
    cliente_obj['nombre'] = cliente_data[0]
    return jsonify(cliente_obj)
from flask import render_template,jsonify,request,redirect,url_for,make_response
from flask_qrcode import QRcode
from app.db import table,header,details,clientes,cliente,arfapar_insert,insert_cabecera,insert_detalle,nit,arfapar_impresion,codigo
from app import create_app
from app.forms import FilterForm,RegisterFactu
from datetime import datetime
from app.tools import numero_to_letras,date
import pdfkit

app = create_app()
QRcode(app)


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
        data = arfapar_insert()
        orden = data[0]
        no_docu = int(data[1]) +1
        llave = data[2]
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

        nit_empresa = nit()
        cod_control = codigo(orden,no_docu,nit_empresa[0],now.date(),(precio-(precio*0.13)),llave) 

        print(tipo_doc_ref,type(tipo_doc_ref))
        insert_cabecera(no_docu,ruta,grupo,cliente,no_ruc,nbr_cliente,direccion,now.date(),observ1,total_items,(precio-(precio*.13)),(precio*.13),(precio),tipo_doc_ref,ruta_ref,no_docu_ref,orden,moneda,cod_control)

        insert_detalle(no_docu,ruta,1,no_arti,precio,precio-(precio*.13),precio*.13,no_item_ref,orden,now.year,now.date(),nivel,spot,segundo,fech_ini,fech_fin,pases,programa,(precio-(precio*0.13))/pases,detalle)
        
        return redirect(url_for('index'))

    contex = {
        'factu_form':factu_form,
    }
    return render_template('factura.html',contex=contex) 






"""Direcciones de descarga e impresión"""

@app.route('/download/<string:no_docu>/<string:grupo>/<string:no_cliente>/<string:centrod>/<string:tipo_doc>/<string:ruta>/<string:no_orden>')
def download_fact(no_docu,grupo,no_cliente,centrod,tipo_doc,ruta,no_orden):
    head = header(centrod,tipo_doc,no_docu,ruta,grupo,no_cliente,no_orden)
    detail = details(centrod,tipo_doc,ruta,no_orden,no_docu)
    fecha = date(head[7])
    dinero_texto = numero_to_letras(head[11]*6.96)
    arfapar = arfapar_impresion(head[13])
    nit_empresa = nit() 
    contex = {
        'head' : head,
        'detail': detail,
        'date':fecha,
        'dinero_texto':dinero_texto,
        'arfapar':arfapar,
        'nit':nit_empresa

    }
    rendered = render_template('print.html',contex=contex)
    pdf = pdfkit.from_string(rendered,False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=test.pdf'
    return response

@app.route('/print/<string:no_docu>/<string:grupo>/<string:no_cliente>/<string:centrod>/<string:tipo_doc>/<string:ruta>/<string:no_orden>')
def print_fact(no_docu,grupo,no_cliente,centrod,tipo_doc,ruta,no_orden):
    head = header(centrod,tipo_doc,no_docu,ruta,grupo,no_cliente,no_orden)
    detail = details(centrod,tipo_doc,ruta,no_orden,no_docu)
    fecha = date(head[7])
    if head[15]=='D':
        dinero_texto = numero_to_letras(head[11]*6.96)
    else:
        dinero_texto = numero_to_letras(head[11])

    arfapar = arfapar_impresion(head[13])
    nit_empresa = nit() 
    contex = {
        'head' : head,
        'detail': detail,
        'date':fecha,
        'dinero_texto':dinero_texto,
        'arfapar':arfapar,
        'nit':nit_empresa
    }
    rendered = render_template('print.html',contex=contex)
    pdf = pdfkit.from_string(rendered,False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=test.pdf'
    return response








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
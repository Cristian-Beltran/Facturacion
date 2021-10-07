import cx_Oracle

connect = cx_Oracle.connect("FA53/FA53@192.168.2.250:1521/ATBPRU")
cursor = connect.cursor()

def table(periodo):
    sql = """
            select NO_DOCU,GRUPO,NO_CLIENTE,FECHA,TOTAL,COD_CONTROL,CENTROD,TIPO_DOC,RUTA,NO_ORDEN
            FROM interfaz_fe
            where no_cia='01'  
            and origen='TV'
            and impreso='S'
            and to_char(fecha,'yyyy')=to_char(:periodo)
            and no_docu||no_orden||TIPO_DOC in (select distinct(no_factu||no_f300||tipo_doc)
            from ARFAFL_DET
            where no_cia='01'
            and periodo = :periodo)
            order by fecha,no_docu
        """
    result = cursor.execute(sql,periodo=periodo)
    return result

def header(centro,tipo_doc,factu,ruta,grupo,clien,ord_auto):
    sql = """
            select TIPO_DOC tipo_doc_c,NO_DOCU no_docu_C,RUTA ruta_c, GRUPO grupo_c, NO_CLIENTE no_cliente_C, NO_RUC no_ruc_c, NBR_CLIENTE nbr_cliente_c,FECHA fecha_c, TIPO_CAMBIO tipo_cambio_c, OBSERV1 observ1_c, OBSERV2 obvserv2_c, TOTAL total_c, NO_SERIE no_serie_c, NO_ORDEN no_orden_c, NO_SUCURSAL no_sucursal, MONEDA moneda_c, IMPRESO impreso_c, COD_CONTROL cod_control_c, OBSERV4 observ4_c, SUB_TOTAL sub_total_c, DESCUENTO descuento_c, IMPUESTO impuesto_c
            from interfaz_fe
            where no_cia='01' 
                and centrod=:p_centro
                and tipo_doc=:p_tip_doc
                and no_docu=:p_factu
                and ruta=:p_ruta
                and grupo=:p_grupo
                and no_cliente=to_number(:p_clien) 
                and no_orden=:p_ord_auto
        """
    result = cursor.execute(sql,p_centro=centro,p_tip_doc=tipo_doc,p_factu=factu,p_ruta=ruta,p_grupo=grupo,p_clien=clien,p_ord_auto=ord_auto)
    return result.fetchone()

def details(centro,tipo_doc,ruta,ord_auto,factu):
    sql = """
            select NO_CIA,CENTROD,TIPO_DOC,PERIODO,FECHA,NO_F300,RUTA,NO_FACTU,NIVEL,SPOT,SEGUNDO,FECH_INI,FECH_FIN,PASES,TOTAL,PROGRAMA,COSTO_SEG,NO_LINEA,BODEGA,CLASE,CATEGORIA,NO_ARTI,DETALLE
            from ARFAFL_DET
            where no_cia='01'
                and centrod=:p_centro
                and tipo_doc=:p_tipo_doc
                and ruta=:p_ruta
                and no_f300=:p_ord_auto
                and no_factu=:p_factu
        """
    result = cursor.execute(sql,p_centro=centro,p_tipo_doc=tipo_doc,p_ruta=ruta,p_ord_auto=ord_auto,p_factu=factu)
    return result.fetchall()


def grupos():
    sql= """
            select grupo,descripcion 
            from ARCCGR 
            where no_cia=1
        """
    result = cursor.execute(sql)
    return result.fetchall()

def clientes(grupo):
    sql= """
            select no_cliente, nombre 
            from ARCCMC 
            where no_cia='01'
            and grupo=:p_grupo
        """
    result = cursor.execute(sql,p_grupo=grupo)
    return result.fetchall()

def cliente(no_cliente):
    sql= """
            select nombre,cedula 
            from ARCCMC 
            where no_cia='01'
            and no_cliente=:p_no_cliente
        """
    result = cursor.execute(sql,p_no_cliente=no_cliente)
    return result.fetchone()

def articulos():
    sql= """
        select servicio,descripcion
        from ARFASE 
        where no_cia=1 
      """
    result = cursor.execute(sql)
    return result.fetchall()

def arfapar_insert():
    sql="""
        select orden, nume_act from arfapar where uso='S'
        """
    result = cursor.execute(sql)

    sql = """Update arfapar set nume_act=:p_nume_act where uso='S'"""
    cursor.execute(sql,p_nume_act=str(int(result[1])+1))
    return result.fetchone()

def arfapar_impresion(orden):
    sql="""
        select * from arfapar where orden=:p_orden"""
    
    datos = cursor.execute(sql,p_orden=orden).fetchone()
    sql="""
        select detalle from arfa_texto where llave=:p_rubro 
        """
    rubro = cursor.execute(sql,p_rubro=datos[15]).fetchone()
    sql="""
        select detalle from arfa_texto where llave=:p_ley 
        """
    ley = cursor.execute(sql,p_ley=datos[16]).fetchone()
    result=[datos[14],rubro[0],ley[0]]
    return result
    

def insert_cabecera(no_docu,ruta,grupo,no_cliente,no_ruc,nbr_cliente,direccion,fecha,observ1,total_items,sub_total,impuesto,total,tipo_doc_ref,ruta_ref,no_docu_ref,no_orden,moneda):
    sql="""
        insert into interfaz_fe(movimiento,origen,no_cia,centrod,tipo_doc,no_docu,ruta,grupo,no_cliente,no_ruc,nbr_cliente,direccion,fecha,tipo_cambio,observ1,observ2,observ3,total_items,sub_total,descuento,impuesto,total,imp_sino,porc_iv,tipo_doc_ref,ruta_ref,no_docu_ref,no_serie,no_orden,no_sucursal,validado,error,moneda,servicio_fact,tipo_fact,afecta_saldo,impreso,cod_control,observ4,rol,regional) values('FA','TV','01','01','01',:p_no_docu,:p_ruta,:p_grupo,:p_no_cliente,:p_no_ruc,:p_nbr_cliente,:p_direccion,:p_fecha,6.96,:p_observ1,'',:p_observ3,:p_total_items,:p_sub_total,0,:p_impuesto,:p_total,'S',13,:p_tipo_doc_ref,:p_ruta_ref,:p_no_docu_ref,'1',:p_no_orden,'1','N','',:p_moneda,'.','E','S','S','','','','')
        """
    cursor.execute(sql,p_no_docu=no_docu,p_ruta=ruta,p_grupo=grupo,p_no_cliente=no_cliente,p_no_ruc=no_ruc,p_nbr_cliente=nbr_cliente,p_direccion=direccion,p_fecha=fecha,p_observ1=observ1,p_observ3=no_docu,p_total_items=total_items,p_sub_total=sub_total,p_impuesto=impuesto,p_total=total,p_tipo_doc_ref=tipo_doc_ref,p_ruta_ref=ruta_ref,p_no_docu_ref=no_docu_ref,p_no_orden=no_orden,p_moneda=moneda)

def insert_detalle(no_docu,ruta,no_item,no_arti,precio,total,iven_n,no_item_ref,no_orden,periodo,fecha,nivel,spot,segundo,fech_ini,fech_fin,pases,programa,costo_seg,detalle):
    sql="""
        insert into interfaz_fl(no_cia,centrod,tipo_doc,no_docu,ruta,no_item,clase,categoria,no_arti,cantidad,porc_desc,precio,descuento,total,i_ven,iven_n,no_item_ref,un_devuel,no_serie,no_orden,no_sucursal,validado,error,moneda,almacen,detalle) values('01','01','01',:p_no_docu,:p_ruta,:p_no_item,'000','000',:p_no_arti,1,0,:p_precio,0,:p_total,'S',:p_iven_n,:p_no_item_ref,'','0',:p_no_orden,'1','N','','','.','') 
        """ 
    cursor.execute(sql,p_no_docu=no_docu,p_ruta=ruta,p_no_item=no_item,p_no_arti=no_arti,p_precio=precio,p_total=total,p_iven_n=iven_n,p_no_item_ref=no_item_ref,p_no_orden=no_orden)
    sql="""
        insert into arfafl_det(no_cia,centrod,tipo_doc,periodo,fecha,no_f300,ruta,no_factu,no_linea,bodega,clase,categoria,no_arti,nivel,spot,segundo,fech_ini,fech_fin,pases,total,programa,costo_seg,detalle) values('01', '01','01',:p_periodo,:p_fecha,:p_no_orden,:p_ruta,:p_no_docu,:p_no_item,'0000','000','000',:p_no_arti,:p_nivel,:p_spot,:p_segundo,:p_fech_ini,:p_fech_fin,:p_pases,:p_total,:p_programa,:p_costo_seg,:p_detalle) 
        """
    cursor.execute(sql,p_periodo=periodo,p_fecha=fecha,p_no_orden=no_orden,p_ruta=ruta,p_no_docu=no_docu,p_no_item=no_item,p_no_arti=no_arti,p_nivel=nivel,p_spot=spot,p_segundo=segundo,p_fech_ini=fech_ini,p_fech_fin=fech_fin,p_pases=pases,p_total=total,p_programa=programa,p_costo_seg=costo_seg,p_detalle=detalle) 


def nit():
    sql ="""select no_ruc from ARCGMC where no_cia='01'"""
    result = cursor.execute(sql)
    return result.fetchone() 
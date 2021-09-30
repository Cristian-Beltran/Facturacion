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


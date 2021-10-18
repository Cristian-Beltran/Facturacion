from flask_wtf import FlaskForm
from wtforms.fields import html5,StringField,DateField,SubmitField,SelectField,IntegerField,DecimalField,FloatField
from wtforms import validators,Form,FieldList,FormField
from .db import grupos,articulos,clientes



class FilterForm(FlaskForm):
    fecha = StringField('Ingrese una fecha',[validators.Required()])
    submit = SubmitField('Enviar')




class RegisterFactu(FlaskForm):
    grupo = SelectField('Seleccione un grupo',[validators.Required()],choices=[(grupo [0],grupo[0]+". "+grupo [1]) for grupo in grupos()])
    cliente = SelectField('Seleccione un cliente',[validators.Required()],choices=[(cliente[0],cliente[1]) for cliente in clientes(36)])
    no_ruc = html5.IntegerField('Ingrese el CI o NIT ',[validators.Required(),validators.Length(min=0,max=16)])
    nbr_cliente = StringField('Nombre de cliente',[validators.Required(),validators.Length(min=0,max=80)])
    direccion = StringField('Ingrese la dirección',[validators.Required(),validators.Length(min=0,max=80)])
    observ1 = StringField('Observacion (opcional)',default=" ")
    total_items = SelectField('Numero de items',[validators.Required()],choices=[(i,i) for i in range(1,21)]) 
    tipo_doc_ref = StringField('Tipo de documento referencia(Opcional)',default=" ")
    ruta_ref = StringField('Ruta referencia(Opcional)',default=" ")
    no_docu_ref = StringField('No de documento referencia(Opcional)',default=" ")
    moneda = SelectField('Seleccione una moneda',[validators.Required()],choices=[('P','Bolivianos'),('D','Dolares')])

    no_arti = SelectField('Selecciona un articulo', [validators.Required()],choices=articulos())
    precio = IntegerField('Ingrese un monto',[validators.Required()])
    no_item_ref = html5.IntegerField('Referencia del item (opcional)',default=" ")
    nivel = StringField('Ingrese el nivel',[validators.Required()])
    spot = StringField('Ingrese el spot',[validators.Required()])
    segundo = StringField('Ingrese el segundo',[validators.Required()])
    fech_ini = html5.DateField('Ingrese la fecha inicial',[validators.Required()])
    fech_fin = html5.DateField('Ingrese la fecha final',[validators.Required()])
    pases = html5.IntegerField('Ingrese el numero de pases',[validators.Required()])
    programa = StringField('Ingrese el programa',[validators.Required()])
    detalle = StringField('Detalle del articulo (opciona)',default=" ")
    Submit = SubmitField('Guardar')






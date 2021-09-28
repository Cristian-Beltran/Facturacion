from flask_wtf import FlaskForm
from wtforms.fields import html5,StringField,DateField,SubmitField,SelectField,IntegerField,DecimalField
from wtforms import validators
from db import grupos,clientes
class FilterForm(FlaskForm):
    fecha = StringField('Ingrese una fecha',[validators.Required()])
    submit = SubmitField('Enviar')


class RegisterFactu(FlaskForm):
    grupo = SelectField('Seleccione un grupo',[validators.Required()],choices=grupos())
    cliente = SelectField('Seleccione un cliente',[validators.Required()])
    no_ruc = StringField('Ingrese el ci ',[validators.Required()])
    nbr_cliente = StringField('Nombre de cliente',[validators.Required()])
    direccion = StringField('Ingrese la dirección',[validators.Required()])
    observ1 = StringField('Observacion',[validators.Required()])
    total_items = html5.IntegerField('Numero de items',[validators.Required()]) 
    tipo_doc_ref = StringField('Tipo de documento referencia(Opcional)',[validators.Required()])
    ruta_ref = StringField('Ruta referencia(Opcional)',[validators.Required()])
    no_docu_ref = StringField('No de documento referencia(Opcional)',[validators.Required()])
    moneda = SelectField('Seleccione una moneda',[validators.Required()],choices=[('P','Bolivianos'),('D','Dolares')])
    submit = SubmitField('Guardar')


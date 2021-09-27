from flask_wtf import FlaskForm
from wtforms.fields import StringField,DateField,SubmitField,SelectField,IntegerField,DecimalField
from wtforms.validators import DataRequired

class FilterForm(FlaskForm):
    fecha = StringField('Ingrese una fecha',validators=[DataRequired()])
    submit = SubmitField('Enviar')


class RegisterFactu(FlaskForm):
    grupo = SelectField('Seleccione un grupo',choices=[('grupo 1','1'),('grupo','2')],validators=[DataRequired()])
    cliente = SelectField('Seleccione un cliente',choices=[('grupo 1','1'),('grupo','2')],validators=[DataRequired()])
    no_ruc = StringField('Ingrese el ci ',validators=[DataRequired()])
    nbr_cliente = StringField('Nombre de cliente',validators=[DataRequired()])
    dirrecion = StringField('Ingrese la direcion',validators=[DataRequired()])
    observ1 = StringField('Observacion',validators=[DataRequired()])
    total_items = IntegerField('Numero de items',validators=[DataRequired()]) 
    total = DecimalField('Ingrese el total',validators=[DataRequired()])
    tipo_doc_ref = StringField('Tipo de documento referencia(Opcional)',validators=[DataRequired()])
    ruta_ref = StringField('Ruta referencia(Opcional)',validators=[DataRequired()])
    no_docu_ref = StringField('No de documento referencia(Opcional)',validators=[DataRequired()])
    moneda = SelectField('Seleccione un cliente',choices=[('grupo 1','1'),('grupo','2')],validators=[DataRequired()])
    submit = SubmitField('Guardar')


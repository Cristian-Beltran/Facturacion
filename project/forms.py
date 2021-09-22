from flask_wtf import FlaskForm
from wtforms.fields import DateField,SubmitField
from wtforms.validators import DataRequired

class FilterForm(FlaskForm):
    fecha = DateField('Ingrese una fecha',validators=[DataRequired()])
    submit = SubmitField('Enviar')


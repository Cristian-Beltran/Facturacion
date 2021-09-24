from flask_wtf import FlaskForm
from wtforms.fields import StringField,DateField,SubmitField
from wtforms.validators import DataRequired

class FilterForm(FlaskForm):
    fecha = StringField('Ingrese una fecha',validators=[DataRequired()])
    submit = SubmitField('Enviar')


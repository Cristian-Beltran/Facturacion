from flask import Flask,render_template
from db import table,header,details,money
from app import create_app
from .forms import FilterForm

app = create_app()

@app.route('/',methods=['GET', 'POST'])
def index(): 
    filter_form = FilterForm()
    fecha = '2019'
    if filter_form.validate_on_submit():
        fecha = filter_form.fecha.data
    data = table(fecha) 
    contex = {
        'DATA':data,
        'filter':filter_form
    }
    return render_template('index.html',contex=contex) 
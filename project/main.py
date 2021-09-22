from flask import Flask,render_template
from db import table,header,details,money

app = Flask(__name__)

@app.route('/')
def index(): 
    data = table('2019') 
    contex = {
        'DATA':data
    }
    return render_template('index.html',contex=contex) 
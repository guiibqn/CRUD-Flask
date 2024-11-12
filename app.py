from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'

db = SQLAlchemy(app)

class Estudante(db.Model):
    id = db.column('id', db.integer, primary_key=True, autoincrement=True)
    nome = db.column(db.string(150))
    idade = db.column(db.integer) 

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade







@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
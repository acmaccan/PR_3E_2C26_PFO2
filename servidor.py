import sqlite3
from flask import Flask, render_template, request, jsonify, redirect
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates')
DATABASE = 'tareas.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contraseña TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/registro', methods=['GET'])
def registro_page():
    return render_template('registro.html')

@app.route('/tareas', methods=['GET'])
def tareas_page():
    return render_template('tareas.html')

@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    hash_contraseña = generate_password_hash(contraseña)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)', (usuario, hash_contraseña))
    conn.commit()
    conn.close()

    return jsonify({ "message": "Usuario registrado correctamente" }), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE usuario = ?', (usuario,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[2], contraseña):
        return jsonify({ "message": "Login exitoso" }), 200
    else:
        return jsonify({ "message": "Usuario o contraseña incorrectos" }), 401

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

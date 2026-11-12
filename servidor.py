import os
import psycopg2
from flask import Flask, render_template, request, jsonify, redirect
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates', static_folder='static')

def get_conn():
    return psycopg2.connect(os.environ['DATABASE_URL'])

def init_db():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            usuario TEXT UNIQUE NOT NULL,
            contraseña TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_user_by_username(usuario):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE usuario = %s', (usuario,))
    user = cursor.fetchone()
    conn.close()
    return user

def create_user(usuario, contraseña):
    hash_contraseña = generate_password_hash(contraseña)
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (%s, %s)', (usuario, hash_contraseña))
        conn.commit()
        conn.close()
        return True, "Usuario registrado correctamente"
    except psycopg2.errors.UniqueViolation:
        conn.close()
        return False, "El usuario ya existe"

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
    usuario = data.get('usuario', '').strip()
    contraseña = data.get('contraseña', '')

    if not usuario:
        return jsonify({ "message": "El usuario no puede estar vacío" }), 400

    if len(contraseña) < 6:
        return jsonify({ "message": "La contraseña debe tener al menos 6 caracteres" }), 400

    success, message = create_user(usuario, contraseña)
    if success:
        return jsonify({ "message": message }), 201
    else:
        return jsonify({ "message": message }), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    user = get_user_by_username(usuario)

    if user and check_password_hash(user[2], contraseña):
        return jsonify({ "message": "Login exitoso" }), 200
    else:
        return jsonify({ "message": "Usuario o contraseña incorrectos" }), 401

init_db()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)

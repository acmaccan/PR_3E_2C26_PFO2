from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__, template_folder='templates')

usuarios = []

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
    usuarios.append(data)
    return jsonify({ "message": "Usuario registrado correctamente" }), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    if usuario == 'nombre' and contraseña == '1234':
        return jsonify({ "message": "Login exitoso" }), 200
    else:
        return jsonify({ "message": "Usuario o contraseña incorrectos" }), 401

if __name__ == '__main__':
    app.run(debug=True)

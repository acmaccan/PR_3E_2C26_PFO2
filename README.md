# PFO2: Sistema de Gestión de Tareas con API y Base de Datos

## Descripción

Sistema web para gestionar tareas (TODO) con autenticación de usuarios, almacenamiento persistente en SQLite y contraseñas hasheadas. Incluye una API REST desarrollada con Flask y una interfaz web responsive.

## Funcionalidades

- Registro e inicio de sesión de usuarios
- Almacenamiento seguro de contraseñas (hashing con Werkzeug)
- Base de datos SQLite
- API REST con endpoints funcionales
- Interfaz web responsive
- Validaciones en frontend y backend

## Requisitos

- Python 3.8+
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar o descargar el repositorio

```bash
cd /PR_3E_2C26_PFO2
```

### 2. Instalar dependencias

```bash
python -m pip install flask
```

**Nota:** Werkzeug se instala automáticamente como dependencia de Flask.

## Ejecución

### Iniciar el servidor

```bash
python servidor.py
```

En consola se verá un mensaje similar a:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Acceder a la aplicación

Abrir navegador:
```
http://localhost:5000
```

## Cómo usar

### 1. Crear una cuenta

- Hacer clic en "crear una cuenta" desde el login
- Ingresar un usuario y contraseña (mínimo 6 caracteres)
- Confirmar la contraseña
- Hacer clic en "crear cuenta"

**Validaciones:**
- Usuario no puede estar vacío
- Contraseña mínimo 6 caracteres
- Las contraseñas deben coincidir
- El usuario debe ser único

### 2. Iniciar sesión

- Ingresar tu usuario y contraseña
- Hacer clic en "iniciar sesión"
- Redirección a espacio de tareas

### 3. Cerrar sesión

- Haz clic en "cerrar sesión" en la esquina superior derecha
- Confirma la acción

## Casos de Prueba

### Registro y validaciones

![Validaciones de registro](/static/img/validaciones.gif)

### Login y navegación a tareas

![Login y tareas](/static/img/navegacion.gif)

### Base de datos (contraseñas hasheadas)

![Hashing en BD](/static/img/hashing.png)

## Estructura del Proyecto

```
.
├── servidor.py                 # API Flask + SQLite
├── templates/                  # Templates HTML
│   ├── login.html
│   ├── registro.html
│   └── tareas.html
├── static/
│   ├── css/
│   │   ├── style.css          # Estilos compartidos
│   │   ├── auth.css           # Estilos para login/registro
│   │   └── tareas.css         # Estilos para tareas
│   └── js/
│       ├── common.js          # Funciones reutilizables
│       ├── auth.js            # Lógica de autenticación
│       └── tareas.js          # Lógica de tareas
├── .gitignore
└── README.md
```

## API Endpoints

### POST `/registro`

Registrar un nuevo usuario.

**Request:**
```json
{
  "usuario": "nombre",
  "contraseña": "password123"
}
```

**Response (201):**
```json
{
  "message": "Usuario registrado correctamente"
}
```

**Errores (400):**
- Usuario vacío
- Contraseña menor a 6 caracteres
- Usuario ya existe

### POST `/login`

Autenticar un usuario.

**Request:**
```json
{
  "usuario": "nombre",
  "contraseña": "password123"
}
```

**Response (200):**
```json
{
  "message": "Login exitoso"
}
```

**Errores (401):**
- Usuario o contraseña incorrectos

### GET `/tareas`

Devuelve la página de tareas (protegida por frontend).

## Base de Datos

### Tabla: usuarios

```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    contraseña TEXT NOT NULL
);
```

**Archivo:** `tareas.db` (se genera automáticamente)

## Troubleshooting

### "No module named 'flask'"

```bash
python -m pip install flask
```

### "Address already in use"

El puerto 5000 está ocupado. Cambiar puerto en `servidor.py`:

```python
app.run(debug=True, port=5001)
```

### Base de datos corrupta

Borrar `tareas.db` - se recrea automáticamente en el próximo inicio:

```bash
rm tareas.db
python servidor.py
```

## Respuestas Conceptuales

### ¿Por qué hashear contraseñas?

Nunca se debe almacenar contraseñas en texto plano. Si la base de datos se filtra, las contraseñas están protegidas. No se pueden recuperar las contraseñas originales, sólo verificar. Eso quiere decir que ningún tercero puede ver la contraseña de un usuario, ni siquiera el administrador del sistema.

### Ventajas de usar SQLite en este proyecto

No requiere servidor externo. Genera un archivo único y fácil de compartir. Es de implementación sencilla para prototipos, mvp o proyectos pequeños.
Para aplicaciones reales es recomendable migrar a un motor de base de datos más robusto como PostgreSQL o MySQL, en el caso de SQL. Si se prefiere un motor NoSQL, puede ser MongoDB. 

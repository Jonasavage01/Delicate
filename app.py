import os
from flask import jsonify
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from flask import abort, jsonify
from flask import flash, redirect, url_for
from flask import Flask, request, jsonify


app = Flask(__name__)

# Configuración de la sesión para utilizar Flask-Session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configuración de la base de datos
db = SQL("sqlite:///final-project.db")
print("Conexión a la base de datos establecida con éxito")


# Funciones de utilidad
def validate_password(password, confirm_password):
    """Valida que las contraseñas coincidan."""
    return password == confirm_password

def hash_password(password):
    """Devuelve la contraseña hasheada."""
    if password is not None:
        return generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
    else:
        return None

def insert_user(email, hashed_password):
    """Inserta el usuario en la base de datos."""
    try:
        query = "INSERT INTO users (email, hash) VALUES (:email, :hash)"
        db.execute(query, email=email, hash=hashed_password)
        print(f"Usuario {email} insertado con éxito")
    except Exception as e:
        print(f"Error al insertar usuario: {str(e)}")

# Rutas

# Contacto
@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        subject = data.get('subject')
        greeting = data.get('greeting')
        email = data.get('email')
        name = data.get('name')

        # Insertar el mensaje de contacto en la tabla
        db.execute("INSERT INTO contact_messages (subject, greeting, email, name) VALUES (:subject, :greeting, :email, :name)",
                   subject=subject, greeting=greeting, email=email, name=name)

        return jsonify({'success': True, 'message': '¡Mensaje enviado correctamente!'})

    except Exception as e:
        app.logger.error(f"Error al procesar el mensaje de contacto: {str(e)}")
        return jsonify({'success': False, 'message': 'Hubo un error al procesar el mensaje de contacto.'}), 500

# Suscripción
@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        data = request.get_json()
        email = data.get('email')

        if not email or not isValidEmail(email):
            return jsonify({'success': False, 'message': 'Correo electrónico no válido'}), 400

        # Insertar el correo electrónico en la tabla de suscriptores
        db.execute("INSERT INTO subscribers (email) VALUES (:email)", email=email)

        return jsonify({'success': True, 'message': '¡Suscripción exitosa! Gracias por suscribirte.'})

    except Exception as e:
        app.logger.error(f"Error en la suscripción: {str(e)}")
        return jsonify({'success': False, 'message': 'Hubo un error al procesar la suscripción.'}), 500

# Páginas estáticas
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/Aboutus')
def Aboutus():
    return render_template('Error-page.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')



# Páginas dinámicas
@app.route('/read_more')
def read_more():
    return render_template('firts-blog.html')

@app.route('/read_more2')
def read_more2():
    return render_template('Blog-second.html')

@app.route('/read_more3')
def read_more3():
    return render_template('Tercer-blog-blog.html')

@app.route('/read_more4')
def read_more4():
    return render_template('Cuarto-blog.html')

# Tienda
@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/shop/product-1')
def product_1():
    return render_template('Product-1.html')

@app.route('/shop/product-2')
def product_2():
    return render_template('Product-2.html')

@app.route('/shop/product-3')
def product_3():
    return render_template('Product-3.html')


@app.route('/shop/product-4')
def product_4():
    return render_template('Product-4.html')


@app.route('/shop/product-5')
def product_5():
    return render_template('Product-5.html')

@app.route('/shop/product-6')
def product_6():
    return render_template('Product-6.html')

@app.route('/shop/product-7')
def product_7():
    return render_template('Product-7.html')

@app.route('/shop/product-8')
def product_8():
    return render_template('Product-8.html')


""" # Lógica de la página de perfil """

@app.route('/')
def index():
    user_id = session.get('user_id')

    # Determinar el enlace de inicio de sesión
    if user_id:
        login_link = url_for('profile')
    else:
        login_link = url_for('login2')

         # Imprimir el User ID en la consola
    print("Session contents:", session)

    return render_template('index.html', login_link=login_link)


@app.route('/login2')
def login2():
    return render_template('log-in.html', error_message=request.args.get('error_message'))



@app.route('/profile')
def profile():
    # Lógica de la página de perfil
    user_id = session.get('user_id')

    # Imprimir el User ID en la consola
    print("User ID in profile:", user_id)

    return render_template('Perfil.html')


@app.route('/success')
def registration_success():
    return render_template('exitoso.html', nombre_usuario='UsuarioEjemplo')


# Rutas de registro e inicio de sesión
@app.route('/register', methods=['GET'])
def show_register_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    try:
        # Obtener los datos del formulario
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        # Imprimir el valor del correo electrónico
        print(f"Email: {email}, Password: {password}, Confirm Password: {confirm_password}")

        # Validar que las contraseñas coincidan
        if not validate_password(password, confirm_password):
            flash("Las contraseñas no coinciden", "error")
            return redirect(url_for('register'))

        # Hash de la contraseña antes de almacenarla
        hashed_password = hash_password(password)

        # Insertar el usuario en la base de datos
        insert_user(email, hashed_password)

        # Redireccionar a la página de éxito después del registro
        return redirect(url_for('registration_success'))
    except Exception as e:
        app.logger.error(f"Error en el registro: {str(e)}")
        flash("Error al registrar el usuario", "error")
        return redirect(url_for('register'))

@app.route('/login', methods=['POST'])
def login():
    try:
        # Obtener los datos del formulario
        email = request.form.get('email')
        password = request.form.get('password')

        # Validar el usuario y la contraseña
        success, error_message = validate_login(email, password)

        if success:
            # Establecer la sesión del usuario
            session['user_id'] = get_user_id_by_email(email)
            # Redirigir a la página de éxito después del inicio de sesión
            return redirect(url_for('index'))
        else:
            # Renderizar la plantilla de inicio de sesión con un mensaje de error
            return render_template('log-in.html', error_message=error_message)
    except Exception as e:
        app.logger.error(f"Error en el inicio de sesión: {str(e)}")
        # Renderizar la plantilla de inicio de sesión con un mensaje de error genérico
        return render_template('log-in.html', error_message="Error al iniciar sesión")


# Funciones para obtener el ID del usuario y validar el inicio de sesión
def get_user_id_by_email(email):
    query = "SELECT id FROM users WHERE email = :email"
    result = db.execute(query, email=email)

    # Verificar si result es None o una lista vacía
    if result is None or len(result) == 0:
        return None
    else:
        # Devolver el primer elemento de la lista (primera fila del resultado)
        return result[0]['id']

def validate_login(email, password):
    query = "SELECT hash FROM users WHERE email = :email"
    result = db.execute(query, email=email)

    if result:
        hashed_password = result[0]['hash']
        if check_password_hash(hashed_password, password):
            return True, None  # Éxito
        else:
            return False, "Contraseña incorrecta"
    else:
        return False, "Usuario no encontrado"

def get_user_info_by_id(user_id):
    query = "SELECT * FROM users WHERE id = :user_id"
    result = db.execute(query, user_id=user_id)

    # Verificar si result es None o una lista vacía
    if result is None or len(result) == 0:
        return None
    else:
        # Devolver el primer elemento de la lista (primera fila del resultado)
        return result[0]


@app.route('/check_email_registration', methods=['POST'])
def check_email_registration():
    try:
        data = request.get_json()
        email = data.get('email')

        # Verificar si el correo está registrado utilizando la función get_user_id_by_email
        is_registered = get_user_id_by_email(email) is not None

        return jsonify({'is_registered': is_registered})

    except Exception as e:
        app.logger.error(f"Error al verificar el correo electrónico registrado: {str(e)}")
        return jsonify({'is_registered': False, 'error': 'Error al verificar el correo electrónico registrado'}), 500


@app.route('/validate_password', methods=['POST'])
def validate_password_route():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # Validar la contraseña utilizando la función validate_login
        success, error_message = validate_login(email, password)

        return jsonify({'success': success, 'error_message': error_message})

    except Exception as e:
        app.logger.error(f"Error al validar la contraseña: {str(e)}")
        return jsonify({'success': False, 'error_message': 'Error al validar la contraseña'}), 500


# Manejo de errores
@app.errorhandler(Exception)
def handle_exception(e):
    return f"An error occurred: {str(e)}", 500

# Ruta para la página de éxito después del registro
@app.route('/login_after_success')
def login_after_success():
    return render_template('log-in.html')

# Comienzo de la aplicación Flask si se ejecuta como script principal
if __name__ == '__main__':
    app.run(debug=True)

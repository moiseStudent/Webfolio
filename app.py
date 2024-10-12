from flask import Flask,render_template, send_file, request, redirect,jsonify
from routes import admin_panel
from markupsafe import escape
import requests


### Send email
from flask_mail import Mail
from flask_mail import Message


### COnfiguraciones de EMail



app = Flask(__name__)



app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'moises.p.student@gmail.com'
app.config['MAIL_PASSWORD'] = 'qyfw evcq fxwg eqpw' 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

app.register_blueprint(admin_panel.AdminPanel)


@app.errorhandler(404)
def error(error):
    return render_template('404.html')

### Ruta principal ( Index )
@app.route('/')
def root():
    return redirect('homepage')
    
@app.route('/homepage')
def index():
    return render_template('index.html')



### Ruta para Informacion legal ###
@app.route('/legal')
def legal():
    return render_template('legal.html')


### Descargar CV ###
@app.route('/download')
def download():
    path_file = 'documents/CV.pdf'
    return send_file(path_file, as_attachment=True)


### Formulario de contacto
@app.route('/contact', methods=['POST'])
def contact():

    if request.method == 'POST':

        name = escape(request.form['name'])
        email_adress = escape(request.form['email'])
        email = escape(request.form['message'])

        send_email(name_client=name, message=email, adress=email_adress)
        
        return redirect('homepage')



def send_email(name_client, message, adress):

    msg = Message(
        subject='Nuevo mensaje enviado desde el portafolio web.',
        sender='moises.p.student@gmail.com',
        recipients=['moises.p.student@gmail.com'] ### Destino
    )
    
    msg.body = 'Este es un mensaje enviado desde el webfolio.'
    msg.html = f"<h3>Nombre: {name_client}<h3><br><h3>Direccion Email: {adress}</h3><br> <h3>Mensaje: {message}</h3>."

    
    try:
        mail.send(msg)
        return 'Correo enviado!'
    except Exception as e:
        return str(e)


mail = Mail(app)











GITHUB_USERNAME = 'moiseStudent'  # Constante

@app.route('/api/portfolio')
def api():
    # URL de la API de GitHub para obtener los repositorios
    url = f'https://api.github.com/users/{GITHUB_USERNAME}/repos'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la respuesta no es 200

    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Error de conexión"}), 500
    except requests.exceptions.HTTPError as http_err:
        return jsonify({"error": f"Error al obtener datos de GitHub: {http_err}"}), response.status_code
    
    # Procesar la respuesta JSON
    repos = response.json()

    # Filtración y organización de la información
    projects = []


    for repo in repos:
        
        category_url = f"{repo['html_url']}/raw/main/category.txt"
        try:
            category_response = requests.get(category_url)
            category_response.raise_for_status()  # Lanza un error si la respuesta no es 200
            category = category_response.text.strip()  # Obtiene el contenido del archivo
        
        except requests.exceptions.RequestException:
            category = "web"
            
        project = {
            'name': repo['name'],
            'description': repo['description'] or 'Sin descripción',  # Maneja casos sin descripción
            'url': repo['html_url'],
            'stars': repo['stargazers_count'],
            'language': repo['language'] or 'No especificado',  # Maneja casos sin lenguaje
            'category':category
        }











        projects.append(project)

    return jsonify(projects)  # Devuelve la lista de proyectos como JSON















### Inicialización general ###
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




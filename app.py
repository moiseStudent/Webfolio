from flask import Flask,render_template, send_file, request, redirect,jsonify
from routes import admin_panel
from markupsafe import escape
import requests

app = Flask(__name__)

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
    name = escape(request.form['name'])
    phone_number = escape(request.form['phone_number'])
    client_email = escape(request.form['client_email'])
    sms = escape(request.form['sms'])
    return f'Hola: {name}, {phone_number}, {client_email}, {sms}'















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




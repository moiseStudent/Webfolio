### Github portfolio API 
from flask import Blueprint, render_template, jsonify
import requests
API = Blueprint('API', __name__)
GITHUB_USERNAME = 'moiseStudent' ### Constant

### Route
@API.route('/api/portfolio')
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

    return jsonify(projects)  #* Devuelve la lista de proyectos como JSON




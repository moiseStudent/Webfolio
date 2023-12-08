from flask import Flask,render_template
# import auth,login

app = Flask(__name__)


### Ruta principal ( Index )
@app.route('/')
def index():
    return render_template('index.html')

### Ruta para blog ( Articles ) ###
@app.route('/blog')
def articles():
    return render_template('blog.html')
##########################################
### Ruta para blog - que es html ( Example ) ###
@app.route('/blog/html_article')
def html_article():
    return render_template('articles/article.html')
##########################################

### Ruta para blog - Acerca del sitio web ###
@app.route('/blog/about_website')
def about_website():
    return render_template('blog.html')


### Ruta para portafolio ###
@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

### Ruta para portafolio - Desarrollo web ###
@app.route('/portafolio/desarrollo_web')
def desarrollo_web():
    return render_template('portafolio.html')

### Ruta para portafolio - Proyectos  ###
@app.route('/portafolio/proyectos')
def proyectos():
    return render_template('portafolio.html')

### Ruta para Contacto ###
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

### Ruta para Informacion legal ###
@app.route('/legal')
def legal():
    return render_template('legal.html')


### Ruta para Informacion sobre el autor del sitio. ###
@app.route('/autor')
def autor():
    return render_template('autor.html')

### Ruta autor - Habilidades tecnicas ###
@app.route('/autor/habilidades_tecnicas')
def habilidades_tecnicas():
    return render_template('autor.html')




### Inicialización general ###
if __name__ == '__main__':
    app.run(debug=True)




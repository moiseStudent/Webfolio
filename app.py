from flask import Flask,render_template, send_file, request, redirect,jsonify, flash
from routes import api
from markupsafe import escape
from flask_mail import Mail, Message
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Your Secret key'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'moises.p.student@gmail.com'
app.config['MAIL_PASSWORD'] = 'qyfw evcq fxwg eqpw' 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

app.register_blueprint(api.API)

@app.errorhandler(404)
def error(error):
    return render_template('404.html')

@app.route('/')
def root():
    return redirect('homepage')
    
@app.route('/homepage')
def index():
    return render_template('index.html')

### Download CV
@app.route('/download')
def download():
    path_file = 'documents/CV.pdf'
    return send_file(path_file, as_attachment=True)

@app.route('/contact', methods=['POST'])
def contact():

    if request.method == 'POST':

        name = escape(request.form['name'])
        email_adress = escape(request.form['email'])
        email = escape(request.form['message'])

        send_email(name_client=name, message=email, adress=email_adress)
        flash('Correo enviado de forma exitosa.')
        return redirect('homepage')

def send_email(name_client, message, adress):

    msg = Message(
        subject='Nuevo mensaje enviado desde el portafolio web.',
        sender='moises.p.student@gmail.com',
        recipients=['moises.p.student@gmail.com'] 
    )
    
    msg.body = 'Este es un mensaje enviado desde el webfolio.'
    msg.html = f"<h3>Nombre: {name_client}<h3><br><h3>Direccion Email: {adress}</h3><br> <h3>Mensaje: {message}</h3>."

    
    try:
        mail.send(msg)
        return 'Correo enviado!'
    except Exception as e:
        return str(e)

mail = Mail(app)

### Init App
if __name__ == '__main__':
    app.run(debug=True)




from flask import Blueprint
from flask import render_template

AdminPanel= Blueprint('AdminPanel', __name__)

### Route
@AdminPanel.route('/adminpanel')
def admin_panel():
    return "Esto es un panel de administracion del sitio web"
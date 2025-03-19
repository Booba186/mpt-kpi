from os import environ

from backend.core.config import Config
from backend.core.extensions import db, migrate, login_manager, mail
from resources.basic_resource import BasicResource
from resources.pdf_resource import PDFResource
from resources.employees_resource import EmployeesResource
from resources.criteries_resource import CriteriesResource
from resources.certificates_resource import CertificatesResource
from backend.auth.auth import auth_bp
from backend.auth.routes import bp as main_bp
from flask import render_template
from core.app_factory import create_app

PORT = environ.get('BACKEND_PORT', 8000)
DEBUG = environ.get('DEBUG', True)

app = create_app()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

app.run(extra_files=[], debug=DEBUG, host='0.0.0.0', port=PORT)

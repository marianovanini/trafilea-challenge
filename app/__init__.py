from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

from app import routes

#swagger documentation
SWAGGER_URL = '/api/docs'
API_URL = 'http://localhost:5000/static/swagger.json'

# Llamada a la función para obtener una instancia de blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Trafilea Challenge API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
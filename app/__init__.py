
from flask import Flask

# Initialize Flask app here
app = Flask(__name__)

# Import and register routes (blueprints)
from app.routes.user_routes import user_routes
app.register_blueprint(user_routes)

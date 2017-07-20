# global imports
from flask import Flask
# Add more here ...


# local imports
from config import app_config
# Add more here ...


def create_app(config_var):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_var])
    app.config.from_pyfile("config.py")

    # Add blueprints here
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint, url_prefix="/dashboard")

    return app

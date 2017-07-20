import os
import configparser

from app import create_app

config = configparser.ConfigParser()
config.read("env.ini")
# config['DEFAULT']['FLASK_CONFIG']

config_var = ""

if "FLASK_CONFIG" in os.environ:
    config_var = os.getenv("FLASK_CONFIG")
else:
    config_var = config['DEFAULT']['FLASK_CONFIG']

app = create_app(config_var)

if __name__ == "__main__":
    app.run()

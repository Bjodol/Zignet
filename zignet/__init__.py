from flask import Flask
import config
controller = Flask(__name__)
controller.config.from_object(config)

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(controller)

if __name__ == "__main__":
	controller.run()
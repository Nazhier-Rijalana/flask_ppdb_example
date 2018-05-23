import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor@localhost/ua_imk'
	# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/book'
	app.config['SECRET_KEY'] = 'p9Bv<3Eid9%$i01'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['DEBUG'] = True
	app.config['SQLALCHEMY_ECHO'] = True
	Bootstrap(app)
	db.init_app(app)
	login_manager.init_app(app)
	login_manager.login_message = "You must be logged in to access this page."
	login_manager.login_view = "authentication.login"

	migrate = Migrate(app,db)
	from app import models

	from .authentication import authentication as authentication_blueprint
	app.register_blueprint(authentication_blueprint)

	from .administrator import administrator as administrator_blueprint
	app.register_blueprint(administrator_blueprint)

	return app

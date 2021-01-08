from flask import Flask, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from database import db
import model
import yaml
from app_route import rout_api

app = Flask(__name__)
app.register_blueprint(rout_api)
with open("config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{0}:{1}@{2}/{3}'.format(cfg["mysql"]["user"], cfg["mysql"]["passwd"], 
                                                                         cfg["mysql"]["host"], cfg["mysql"]["db"] )    # connecting MySql Database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

def main():
   db.init_app(app)
   with app.app_context():
      db.drop_all()
      db.create_all()

if __name__ == "__main__":
   main()
   app.run(debug=True, use_reloader=True)




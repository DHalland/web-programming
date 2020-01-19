import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLalchemy

class Flight(db.Model):
   __tablename__ = "flights"
   id = db.Column(db.integer, primary_key=True)
   source = db.Column(db.String, nullable=False)
   destination = db.Column(db.String, nullable=False)
   duration = db.Column(db.String, nullable=False)

class Passenger(db.Model):
   __tablename__ = "passengers"
   id = db.Column(db.integer, primary_key=True)
   name = db.Column(db.String, nullable=False)
   flight_id = db.Column(db.Integer, db.foreignKey("flights.id"))

app = Flask(__name__)
app.config["SQL_DATABASE_URI"] = os.getenv("DATABASE_URL") 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

db = SQLalchemy()
db.init_app(app)

def main():
   db.create_all()

if __name__ == "__main__":
   with app.app_context():
      main()
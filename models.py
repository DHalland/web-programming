import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
   __tablename__ = "flights"
   id = db.Column(db.Integer, primary_key=True)
   source = db.Column(db.String, nullable=False)
   destination = db.Column(db.String, nullable=False)
   duration = db.Column(db.String, nullable=False)

   def add_passenger(self, name):
      p = Passenger(name=name, flight_id=self.id)
      db.session.add(p)
      db.session.commit()

class Passenger(db.Model):
   __tablename__ = "passengers"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String, nullable=False)
   flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"))
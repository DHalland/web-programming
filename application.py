from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL") 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

db.init_app(app)

#engine = create_engine(os.getenv("DATABASE_URL"))
#db url --> C:\Program Files\PostgreSQL\12\bin
#db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
   flights = Flight.query.all()
   return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    # Get form information.
    firstandlast = request.form.get("firstandlast")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    # Make sure the flight exists.
    flight = Flight.query.get(flight_id)
    if not flight:
        return render_template("error.html", message="No such flight with that id.")
    
    flight.add_passenger(firstandlast)
    return render_template("success.html")

#imports 
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask, jsonify
# setup data base
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()

#reflect database
Base.prepare(engine, reflect=True)
#create a variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station
#create link from Python to Database
session = Session(engine)

#Create a New Flask App Instance
app = Flask(__name__)

#create routes

@app.route('/') #home page
def welcome():
    return(
    '''
    <h1>Welcome to the Climate Analysis API!</h1>

    <h2>Available Routes:</h2>

    <a href="/api/v1.0/precipitation"> Precipitation</a></br>
    <a href="/api/v1.0/stations"> Stations</a></br>
    <a href="/api/v1.0/tobs"> Tobs</a></br>
    <a href="/api/v1.0/temp/start/end"> Start/End</a>
    ''')

#precipitation 
@app.route("/api/v1.0/precipitation")

def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
                    filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
    

#stations
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#tobs
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#start/end
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)



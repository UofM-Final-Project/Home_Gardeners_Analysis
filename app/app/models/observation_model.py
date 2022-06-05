from app import db
from datetime import datetime as dt, timedelta

class observation(db.Model):
    station_uid = db.Column(db.Integer, db.ForeignKey("station.station_uid"))
    date = db.Column(db.DateTime, primary_key=True)
    maxt = db.Column(db.Float)
    mint = db.Column(db.Float)
    pcpn = db.Column(db.Float)
    snow = db.Column(db.Float)
    snwd = db.Column(db.Float)
    avgt = db.Column(db.Float)
    freeze_day = db.Column(db.Integer)
    above_freezing = db.Column(db.Integer)
    obs_year = db.Column(db.Integer)
    obs_month = db.Column(db.Integer)
    obs_day = db.Column(db.Integer)
    obs_dayofyear = db.Column(db.Integer)
    maxt_7_day = db.Column(db.Float)
    mint_7_day = db.Column(db.Float)
    avgt_7_day = db.Column(db.Float)
    precip_7_day = db.Column(db.Float)
    obs_count_7_day = db.Column(db.Float)
    maxt_30_day = db.Column(db.Float)
    mint_30_day = db.Column(db.Float)
    avgt_30_day = db.Column(db.Float)
    precip_30_day = db.Column(db.Float)
    obs_count_30_day = db.Column(db.Float)



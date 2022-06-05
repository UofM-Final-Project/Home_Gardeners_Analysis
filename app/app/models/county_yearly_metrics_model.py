

from app import db


class county_yearly_metrics(db.Model):
    county = db.Column(db.Integer,primary_key=True)
    obs_year = db.Column(db.Integer,unique=True)
    county_name = db.Column(db.String)
    station_count = db.Column(db.Integer)
    coldest_day = db.Column(db.Float)
    coldest_dayofyear = db.Column(db.Integer) 
    hottest_day = db.Column(db.Float)
    hottest_dayofyear = db.Column(db.Integer)
    last_freeze_date = db.Column(db.DateTime)
    last_freeze_dayofyear = db.Column(db.Integer)
    first_freeze_date = db.Column(db.DateTime)
    first_freeze_dayofyear = db.Column(db.Float)
    observations_recorded_april_to_may = db.Column(db.Integer)



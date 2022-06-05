

from app import db


class county_metrics(db.Model):
    county = db.Column(db.Integer,primary_key=True)
    county_name = db.Column(db.String)
    station_count = db.Column(db.Integer)
    avg_last_freeze_dayofyear = db.Column(db.Float)
    avg_last_freeze_mm_dd = db.Column(db.String)
    median_last_freeze_dayofyear = db.Column(db.Float)
    median_last_freeze_mm_dd = db.Column(db.String)
    years_included = db.Column(db.Integer)
    count_at_or_before_avg_last_freeze = db.Column(db.Integer) 
    count_later_than_avg_last_freeze = db.Column(db.Integer)

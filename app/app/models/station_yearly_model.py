from app import db


class station_yearly(db.Model):
    station_uid = db.Column(db.Integer, db.ForeignKey("station.station_uid"))
    obs_year = db.Column(db.Integer,primary_key=True)
    coldest_day = db.Column(db.Float)
    coldest_dayofyear = db.Column(db.Float)
    hottest_day = db.Column(db.Float)
    hottest_dayofyear = db.Column(db.Float)
    last_freeze_date = db.Column(db.DateTime)
    last_freeze_dayofyear = db.Column(db.Float)
    first_freeze_date = db.Column(db.DateTime)
    first_freeze_dayofyear = db.Column(db.Float)
    observations_recorded_april_to_may = db.Column(db.Float)


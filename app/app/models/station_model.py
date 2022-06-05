from app import db


class station(db.Model):
    station_uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    county = db.Column(db.Integer)
    state = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    climdiv = db.Column(db.String)
    avg_last_freeze_dayofyear = db.Column(db.Float)
    avg_last_freeze_mm_dd = db.Column(db.String)
    median_last_freeze_dayofyear = db.Column(db.Float)
    median_last_freeze_mm_dd = db.Column(db.String)
    years_included = db.Column(db.Integer)
    count_at_or_before_avg_last_freeze = db.Column(db.Integer)
    count_later_than_avg_last_freeze = db.Column(db.Integer)
    stations_yearly = db.relationship('station_yearly', backref='station', lazy="dynamic")
    observations = db.relationship('observation', backref='station', lazy="dynamic")
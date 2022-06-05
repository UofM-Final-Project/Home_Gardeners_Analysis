from app import db


class county_lookup(db.Model):
    state = db.Column(db.String,primary_key=True)
    county_code = db.Column(db.Integer) 
    county_name = db.Column(db.String) 

from app.main import db

class VehicleListing(db.Model):
    __tablename__ = 'vehicle_listings'

    id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.String(17), unique=True, nullable=False)
    year = db.Column(db.Integer)
    make = db.Column(db.String(200))
    model = db.Column(db.String(200))
    trim = db.Column(db.String(200))
    dealer_name = db.Column(db.String(200))
    dealer_street = db.Column(db.String(200))
    dealer_city = db.Column(db.String(200))
    dealer_state = db.Column(db.String(100))
    dealer_zip = db.Column(db.String(100))
    listing_price = db.Column(db.Numeric(10, 2))
    listing_mileage = db.Column(db.Integer)
    used = db.Column(db.Boolean)
    certified = db.Column(db.Boolean)
    style = db.Column(db.String(200))
    driven_wheels = db.Column(db.String(200))
    engine = db.Column(db.String(200))
    fuel_type = db.Column(db.String(200))
    exterior_color = db.Column(db.String(200))
    interior_color = db.Column(db.String(200))
    seller_website = db.Column(db.String(255))
    first_seen_date = db.Column(db.Date)
    last_seen_date = db.Column(db.Date)
    dealer_vdp_last_seen_date = db.Column(db.Date)
    listing_status = db.Column(db.String(200))

    __table_args__ = (
        db.Index('idx_vin', 'vin'),
        db.Index('idx_year_make_model', 'year', 'make', 'model')
    )

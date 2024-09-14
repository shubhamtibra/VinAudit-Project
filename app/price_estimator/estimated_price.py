from app.models.models import VehicleListing
from sqlalchemy import func
from sklearn.linear_model import LinearRegression
import numpy as np

class EstimatePrice:
    def __init__(self, year, make, model, mileage=None):
        self.year = year
        self.make = make
        self.model = model
        self.mileage = mileage
        self.query = VehicleListing.query.filter(VehicleListing.listing_price != None, VehicleListing.listing_mileage != None, VehicleListing.year==year, VehicleListing.make==make, VehicleListing.model==model)
    
    def get_price(self):
        estimated_price = None
        if self.mileage:
            result = self.query.with_entities(VehicleListing.listing_price, VehicleListing.listing_mileage).all()
            x = np.array([r.listing_mileage for r in result]).reshape(-1, 1)
            y = np.array([r.listing_price for r in result])
            model = LinearRegression().fit(x, y)
            estimated_price = model.predict(np.array([int(self.mileage)]).reshape(-1, 1))[0]
        else:
            estimated_price = self.query.with_entities(func.avg(VehicleListing.listing_price)).scalar()
        return estimated_price
    def get_sample_listings(self):
        sample_listings = self.query.limit(100).all()
        return sample_listings

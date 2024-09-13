from flask import Blueprint, request, jsonify
from sqlalchemy import func
from .models import db, VehicleListing
from flask_cors import cross_origin
main = Blueprint('main', __name__)

@main.route('/api/search', methods=['POST'])
@cross_origin()
def search():
    data = request.json
    year = data.get('year')
    make = data.get('make')
    model = data.get('model')
    mileage = data.get('mileage')

    if not all([year, make, model]):
        return jsonify({"error": "Year, make, and model are required"}), 400

    query = VehicleListing.query.filter(VehicleListing.listing_price != None, VehicleListing.listing_mileage != None, VehicleListing.year==year, VehicleListing.make==make, VehicleListing.model==model)


    estimated_price = db.session.query(func.avg(VehicleListing.listing_price)).filter_by(year=year, make=make, model=model).scalar()

    sample_listings = query.limit(100).all()

    result = {
        "estimated_price": estimated_price,
        "sample_listings": [
            {
                "year": v.year,
                "make": v.make,
                "model": v.model,
                "trim": v.trim,
                "price": v.listing_price,
                "mileage": v.listing_mileage,
            } for v in sample_listings
        ]
    }

    response = jsonify(result)
    return response
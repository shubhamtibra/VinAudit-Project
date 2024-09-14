from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.price_estimator.estimated_price import EstimatePrice

main = Blueprint('main', __name__)

@main.route('/')
@cross_origin()
def home():
    pass

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
    
    estimate = EstimatePrice(year, make, model, mileage)
    estimated_price = estimate.get_price()
    sample_listings = estimate.get_sample_listings()

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
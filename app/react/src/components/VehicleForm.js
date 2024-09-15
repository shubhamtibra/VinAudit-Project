import React, { useState } from 'react';
import './VehicleForm.css';

function VehicleForm() {
    const [make, setMake] = useState('');
    const [year, setYear] = useState('');
    const [model, setModel] = useState('');
    const [mileage, setMileage] = useState('');
    const [estimatedPrice, setEstimatedPrice] = useState(null)
    const [sampleListing, setSampleListing] = useState(null)

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('/api/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    make, year, model, mileage
                }),
            });
            const data = await response.json();
            setEstimatedPrice(Number(data.estimated_price).toFixed(2));
            setSampleListing(data.sample_listings);
            console.log('API response:', data);
        } catch (error) {
            console.error('Error calling API:', error);
        }
    };

    return (
        <div>
            <form className="vehicle-form" onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="make">Make:</label>
                    <input
                        type="text"
                        id="make"
                        value={make}
                        onChange={(e) => setMake(e.target.value)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="year">Year:</label>
                    <input
                        type="number"
                        id="year"
                        value={year}
                        onChange={(e) => e.target.value >= 0 ? setYear(e.target.value) : null}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="model">Model:</label>
                    <input
                        type="text"
                        id="model"
                        value={model}
                        onChange={(e) => setModel(e.target.value)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="mileage">Mileage (Optional):</label>
                    <input
                        type="number"
                        id="mileage"
                        value={mileage}
                        onChange={(e) => e.target.value >= 0 ? setMileage(e.target.value): null}
                    />
                </div>
                <button type="submit" className='submit-btn'>Submit</button>
            </form>
            {estimatedPrice && (
                <div className="estimated-price">
                    <h2>Estimated Price: ${estimatedPrice}</h2>
                </div>
            )}
            {sampleListing && sampleListing.length > 0 && (
                <div className="sample-listing">
                    <h2>Sample Listings</h2>
                    <div className="table-container">
                    <table class="styled-table">
                        <thead>
                            <tr>
                                {Object.keys(sampleListing[0]).map((header) => (
                                    <th key={header}>{header}</th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {sampleListing.map((listing, index) => (
                                <tr key={index}>
                                    {Object.values(listing).map((value, valueIndex) => (
                                        <td key={valueIndex}>{value}</td>
                                    ))}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                    </div>
                </div>
            )}
        </div>
    );
}

export default VehicleForm;
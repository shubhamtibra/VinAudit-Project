import sys
print(sys.path)
from app.main import create_app, db
from app.models.models import VehicleListing
from datetime import datetime

class FileReader:
    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            headers = file.readline().strip().split('|')
            for line in file:
                yield dict(zip(headers, line.strip().split('|')))

class DataProcessor:
    @staticmethod
    def process_row(row):
        # Convert empty strings to None
        for key, value in row.items():
            if value == '':
                row[key] = None

        # Convert date strings to datetime objects
        for date_field in ['first_seen_date', 'last_seen_date', 'dealer_vdp_last_seen_date']:
            if row[date_field]:
                row[date_field] = datetime.strptime(row[date_field], '%Y-%m-%d').date()

        # Convert boolean strings to actual booleans
        for bool_field in ['used', 'certified']:
            if row[bool_field]:
                row[bool_field] = row[bool_field].lower() == 'true'

        # Convert numeric fields
        if row['year']:
            row['year'] = int(row['year'])
        if row['listing_price']:
            row['listing_price'] = float(row['listing_price'])
        if row['listing_mileage']:
            row['listing_mileage'] = int(row['listing_mileage'])

        return row

class DataImporter:
    @staticmethod
    def import_data(file_path):
        file_reader = FileReader()
        for row in file_reader.read_file(file_path):
            processed_row = DataProcessor.process_row(row)
            with app.app_context():
                try:
                    listing = VehicleListing(**processed_row)
                    db.session.add(listing)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    print(f"Error inserting listing: {e}")

if __name__ == "__main__":
    file_path = r"C:\Users\shubh\Downloads\NEWTEST-inventory-listing-2022-08-17.txt"
    app = create_app(load_data=True)
    with app.app_context():
        db.create_all()
    DataImporter.import_data(file_path)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()

def create_app(load_data=False):
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://shubham:123456789@localhost/vehicle_listings'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    if load_data == False:
        from app.routes import main
        app.register_blueprint(main)
    return app

# File: wsgi.py
# from app import create_app

# application = create_app()

if __name__ == "__main__":
    application = create_app()
    application.run(debug=True)

# # File: gunicorn.conf.py
# workers = 3
# bind = "unix:/tmp/gunicorn.sock"
# module = "wsgi:application"

# # Nginx configuration (to be placed in /etc/nginx/sites-available/vinaudit)
# server {
#     listen 80;
#     server_name your_domain.com;

#     location / {
#         proxy_pass http://unix:/tmp/gunicorn.sock;
#         proxy_set_header Host $host;
#         proxy_set_header X-Real-IP $remote_addr;
#     }
# }
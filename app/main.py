from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app(load_data=False):
    app = Flask(__name__, static_url_path='', static_folder='react/build', template_folder='react/build')
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URL'] if "DB_URL" in os.environ else 'postgresql://shubham:123456789@localhost/vehicle_listings'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    if load_data == False:
        from app.routes.routes import main
        app.register_blueprint(main)
    return app

application = create_app()
if __name__ == "__main__":
    application.run()
    # Serve static react files


# # File: gunicorn.conf.py
# workers = 3
# bind = "unix:/tmp/gunicorn.sock"
# module = "wsgi:application"

# # Nginx configuration
# server {
#     listen 80;
#     server_name your_domain.com;

#     location / {
#         proxy_pass http://unix:/tmp/gunicorn.sock;
#         proxy_set_header Host $host;
#         proxy_set_header X-Real-IP $remote_addr;
#     }
# }
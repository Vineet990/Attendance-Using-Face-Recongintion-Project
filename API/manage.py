import os
from flask_cors import CORS
from flask_restful import Api

from app.main import (
        db, # SQLAlchemy Connector dB Object
        create_app
    )

# setting the environment
from dotenv import load_dotenv # Python 3.6+
load_dotenv(verbose = True) # configure .env File or set Environment Variables

app = create_app(os.getenv("PROJECT_ENV_NAME") or "dev") # check config.py
CORS(app) # enable CORS for cross-application data sharing

api = Api(app)

from app.main.application import * # import all controllers

api.add_resource(AttendanceController, "/api/att/name",endpoint="name")
api.add_resource(AttendanceController, "/api/att/date",endpoint="date")

if __name__ == "__main__":
    app.run(
        port = os.getenv("port", 5000),
        host = os.getenv("host", "0.0.0.0")
    )
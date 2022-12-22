import os
from flask_cors import CORS
from flask import Flask
from config.db import get_db


if __name__ == "__main__":
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/version', methods=['GET'])
    def version():
        return { 'name': 'Flask server', 'version': '1.0.0'}

    @app.route('/check-mongo-connection', methods=['GET'])
    def checkMongoConnection():
        try:
            get_db()
            return {'status': True}
        except:
            return {'status': False}

    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = os.getenv('DB_URI')
    app.run()
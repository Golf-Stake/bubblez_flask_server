import os
from flask import Flask
from config.db import get_db

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['MONGO_URI'] = os.getenv('DB_URI')

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

if __name__ == '__main__':
  app.run(port=os.getenv('PORT', 5000),host=os.getenv('HOST', '0.0.0.0'),debug=True)
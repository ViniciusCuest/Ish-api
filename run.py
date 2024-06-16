from flask import Flask
from api.models.database import mongo, User
from api.controller import routes 
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/ish-api'
mongo.init_app(app)
routes.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        if 'user' not in mongo.db.list_collection_names():
            mongo.db.user.insert_one({
                'full_name': '',
                'birth': '',
                'identifier': '',
                'work_authorization_code': '',
                'phone': '',
                'email': '',
                'password': ''
            })
    
    app.run(host='localhost', port=5000, debug=True)
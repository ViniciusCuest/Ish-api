from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo, MongoClient
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] = 'mongodb+srv://express-database-training:88kQHm4DYqeslhex@cluster0.ae1nqqm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
mongo = PyMongo(app=app)
print(mongo.db)
ma = Marshmallow(app)

from .controller import user_controller
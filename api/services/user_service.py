from api import mongo
from ..models import user_model
from bson import ObjectId

@staticmethod
def getUser():
    return list(mongo.db.games.find())

def addUser(user):
    return mongo.db.users.insert_one({
        "full_name": user.full_name, 
        "birth": user.birth, 
        "identifier": user.identifier,
        "work_authorization_code": user.work_authorization_code, 
        "phone": user.phone,
        "email": user.email, 
        "password": user.password
    })
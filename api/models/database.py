from flask_pymongo import PyMongo
mongo = PyMongo()

class User():
   def __init__(self, full_name, birth, identifier, work_authorization_code, phone, email, password):
      self.full_name = full_name
      self.birth = birth
      self.identifier = identifier
      self.work_authorization_code = work_authorization_code
      self.phone = phone
      self.email = email
      self.password = password
   
   def create_user(self):
      mongo.db.user.insert_one({
         'full_name': self.full_name,
         'birth': self.birth,
         'identifier': self.identifier,
         'work_authorization_code': self.work_authorization_code,
         'phone': self.phone,
         'email': self.email,
         'password': self.password
      })
   
def login(email, password):
   user = mongo.db.user.find_one({
      'email': email,
      'password':password
   })
   return user
   
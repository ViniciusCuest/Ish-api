from api import mongo
class User():
   def __init__(self, full_name, birth, identifier, work_authorization_code, phone, email, password):
      self.full_name = full_name
      self.birth = birth
      self.identifier = identifier
      self.work_authorization_code = work_authorization_code
      self.phone = phone
      self.email = email
      self.password = password
   
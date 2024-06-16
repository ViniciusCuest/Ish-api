from flask import jsonify, request
from api.models.database import User, mongo, login

def init_app(app):
    @app.route('/register', methods=['POST'])
    def register():
          data = request.get_json()
          full_name = data.get('full_name')
          birth = data.get('birth')
          identifier = data.get('identifier')
          work_authorization_code = data.get('work_authorization_code')
          phone = data.get('phone')
          email = data.get('email')
          password=data.get('password')
          if not full_name or birth or identifier or phone | email | password:
              return jsonify({'message': 'Fields missing'}), 401
 
          user = User(
              email=email, 
              full_name=full_name, 
              birth=birth, 
              identifier=identifier, 
              work_authorization_code=work_authorization_code,
              phone=phone, 
              password=password
            )
          user.create_user()
          return jsonify({data}), 201
    
    @app.route('/login', methods=['POST'])
    def login_post():
      data = request.get_json()
      email = data.get('email')
      password = data.get('password')

      user_data = []
      user = login(email=email, password=password)

      user_data.append({
        'full_name': user['full_name'],
        'work_authorization_code':user['full_name'],
        'phone': user['full_name'],
        'email': user['full_name']
      })
      return jsonify(user_data), 200
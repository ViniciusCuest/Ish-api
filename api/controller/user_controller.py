from flask_restful import Resource
from api import api
from ..schemas import user_schema
from ..models import user_model
from ..services import user_service
from flask import make_response, jsonify, request

class UserController():
   class WithoutBody(Resource):
      def get(self):
         user = user_service.getUser()
         data = user_schema.UserSchema(many=False)
         return make_response(data.jsonify(user), 200)
      def post(self):
         user = user_schema.UserSchema()
         not_valid = user.validate(request.json)
         if not_valid:
            return make_response(jsonify(not_valid), 400)
         else: 
            full_name = request.json["full_name"]
            birth = request.json["birth"]
            email = request.json["email"]
            identifier = request.json["identifier"]
            phone = request.json["phone"]
            password = request.json["password"]
            work_authorization_code = request.json["work_authorization_code"]

            new_user = user_model.User(full_name=full_name,phone=phone, birth=birth,email=email,identifier=identifier,password=password,work_authorization_code=work_authorization_code)
            created_user = user_service.addUser(new_user)
            return make_response(user.jsonify(created_user), 201)

# class GameList(Resource):
#     def get(self):
#         games = game_service.get_games()
#         g = game_schema.GameSchema(many=True)
#         return make_response(g.jsonify(games), 200)
#         # Código 200 (OK) : Requisição bem sucedida.
        
#     def post(self):
#         g = game_schema.GameSchema()
#         validate = g.validate(request.json)
#         if validate:
#             return make_response(jsonify(validate), 400) #Código 400: (BAD REQUEST) : Solicitação inválida ou malformada.
#         else:
#             titulo = request.json["titulo"]
#             descricao = request.json["descricao"]
#             ano = request.json["ano"]
            
#             new_game = game_model.Game(titulo=titulo, descricao=descricao, ano=ano)
#             result = game_service.add_game(new_game)
#             res = g.jsonify(result)
#             return make_response(res, 201) #Código 201 (CREATED): Criação bem-sucedida de um novo recurso.
        
# class GameDetail(Resource):
#     def get(self, id):
#         game = game_service.get_game_by_id(id)
#         if game is None:
#             return make_response(jsonify("Game não foi encontrado."), 404) #Código 404 (NOT FOUND): Indica que o recurso requisitado não foi encontrado no servidor.
#         g = game_schema.GameSchema()
#         return make_response(g.jsonify(game), 200) #Código 200 (OK)       
        
#     def put(self, id):
#         game_bd = game_service.get_game_by_id(id)
#         if game_bd is None:
#             return make_response(jsonify("Game não foi encontrado"), 404) #Código 404 - NOT FOUND
#         g = game_schema.GameSchema()
#         validate = g.validate(request.json)
#         if validate:
#             return make_response(jsonify(validate), 404)
#         else:
#             titulo = request.json["titulo"]
#             descricao = request.json["descricao"]
#             ano = request.json["ano"]
#             new_game = game_model.Game(titulo=titulo, descricao=descricao, ano=ano)
#             game_service.update_game(new_game, id)
#             updated_game = game_service.get_game_by_id(id)
#             return make_response(g.jsonify(updated_game), 200)

# api.add_resource(GameList, '/games')
# api.add_resource(GameDetail, '/games/<id>')

api.add_resource(UserController.WithoutBody, '/')
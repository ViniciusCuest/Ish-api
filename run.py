from api import app, mongo
from api.models.user_model import User
from api.services import user_service

if __name__ == "__main__":
    with app.app_context():
        if 'user' not in mongo.db.list_collection_names():
             game = User(full_name='', birth='', identifier='', work_authorization_code='', phone='', email='', password='')
             user_service.addUser(game)
    app.run(host='localhost', port=5000, debug=True)
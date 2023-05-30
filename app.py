import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actors, Movies
# from auth import AuthError, requires_auth


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  @app.route('/', methods=["GET"])
  def get_init():
     return jsonify({
        'test_url':os.environ['EXCITED']
     })
  
  #added for CRUD requests
  @app.after_request
  def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response
  #For each requests we must check auth for the user by @requires_auth

  @app.route('/actors', methods=['GET'])
#   @requires_auth(permission='get:actors')
  def get_actors(payload):
        try:
            actors = Actors.query.order_by(Actors.id).all()
            total_actors = len(actors)
            return jsonify({
                'success': True,
                'actors': actors,
                'total-actors': total_actors
            })
        except Exception:
            abort(422)
  

  

  return app

   

app = create_app()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
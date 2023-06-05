import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actors, Movies
from auth import AuthError, requires_auth


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
  def format_records(data):
   data2 = [elm.format() for elm in data]
   return data2
   
  
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
  @requires_auth(permission='get:actors')
  def get_actors(payload):
        try:
            actors = Actors.query.order_by(Actors.id).all()
            total_actors = len(actors)
            actors = format_records(actors)
            return jsonify({
                'success': True,
                'actors': actors,
                'total-actors': total_actors
            })
        except Exception:
            abort(422)

#   @app.route('/actors/<int:id>',methods=['GET'])
#   @requires_auth(permission='get:actors')
#   def get_actor_by_id(payload,id):
#       try:
#           actor = Actors.query.get(id)
#           return jsonify({
#                 'success': True,
#                 'name': actor.name

           
              
#           })
#       except:
#           abort(422)

# To patch an actor u must resend all the data via an json object
# Ex. if u want to only update the name u also have to resedn the age and gender

  @app.route('/actors/<int:id>',methods=['PATCH'])
  @requires_auth(permission='patch:actors')
  def update_actor(payload,id):
      
      try:

         movie = Actors.query.get(id)
         updatedActor = request.get_json()

         if updatedActor in None:
              abort(404)
         movie.title = updatedActor['name']
         movie.age = updatedActor['age']
         movie.gender = updatedActor['gender']
         movie.update()
         return jsonify({
                'success': True,
                'actor_id': id
          })
      except:
          abort(422)
  @app.route('/actors/<int:id>',methods=['DELETE'])
  @requires_auth(permission='delete:actors')
  def delete_actor(payload,id):
          
      try:

         actor = Actors.query.get(id)
         if not actor:
             abort(404)
         actor.delete()
         return jsonify({
                'success': True,
                'actor_id': id
          })
      except:
          abort(422)

  @app.route('/movies', methods=['GET'])
  @requires_auth(permission='get:movies')
  def get_movies(payload):
        try:
            movies = Movies.query.order_by(Movies.id).all()
            total_movies = len(movies)
            movies = format_records(movies)
            return jsonify({
                'success': True,
                'movies': movies,
                'total-movies': total_movies
            })
        except Exception:
            abort(422)
#   @app.route('/movies/<int:id>', methods=['GET'])
#   @requires_auth(permission='get:movies')
#   def get_movie_by_id(payload,id):
#         try:
#             movie = Movies.query.get(id)
#             if movie is None:
#                 abort(422)

#             movie = format_records(movie)
#             return jsonify({
#                 'success': True,
#                 'movie': movie,
#             })
#         except Exception:
#             abort(422)

  @app.route('/movies', methods=['POST'])
  @requires_auth(permission='post:movies')
  def add_movies(payload):
        
        new_movie = request.get_json()
        title = new_movie.get('title')
        date = new_movie.get('release_date')

        if title is None or date is None:
            abort(422)
         
        try:
            movie = Movies(title=title,release_date=date)
            
            movie.insert()
            return jsonify({
                "success":True,
                "movie": movie.id
            })
        except:
            abort(422)
  @app.route('/movies/<int:id>',methods=['PATCH'])
  @requires_auth(permission='patch:actors')
  def update_movie(payload,id):
      
      try:

         movie = Actors.query.get(id)
         updatedMovie = request.get_json()

         if updatedMovie in None:
              abort(404)
         movie.title = updatedMovie['name']
         movie.release_date = updatedMovie['age']
         movie.update()
         return jsonify({
                'success': True,
                'movie_id': id
          })
      except:
          abort(422)

  @app.route('/movies/<int:id>',methods=['DELETE'])
  @requires_auth(permission='delete:actors')
  def delete_movie(payload,id):
      
      try:

         movie = Actors.query.get(id)


         if movie in None:
              abort(404)
         

         movie.delete()
         return jsonify({
                'success': True,
                'movie_id': id
          })
      except:
          abort(422)
  

  return app

   

app = create_app()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actors, Movies
from sqlalchemy import Column, Integer, String, create_engine, Date


class CastingAgencyTestCase(unittest.TestCase):
    def setUp(self):


        DATABASE_URL="postgresql://postgres@localhost:5432/postgres "
        admin_jwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhjVURhSHYyTTFIcHlXYjlyYjhKaiJ9.eyJpc3MiOiJodHRwczovL3VkMjMudXMuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEzMzMxODkyNTgyNDI2MzU4MDE0IiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTY4NjExOTgwMiwiZXhwIjoxNjg2MTI3MDAyLCJhenAiOiJBS1JDOUFhUUczbUYwMTNxQXhEY1ZhMDdHWjVDTldodSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.J0E6GB2hdI_uJzkoWcb01OvNUz-h9-hX7kz9rG3i6pB9RtVriVH3di0BQFaoPOOZNdWHJOJDYV3Ny-BUM_ZvUNn1yk5tDY1l1kEEQcV85eIW2ZhIxXgjYe3wjLVc5BpxCcQHJGtsK2oenB7W-RJ9elbeQXyRTxF9m8zXujEqiQt6g4jwWLBMv1DyTLG5l1gUfybDRtDgp6XwKqEAiqU43iAG0N6UvEDX9_fu9XlkrCTh69-GdtHg0jzkKqjTqoMNBK4UxPNJXbth6CUWkwMyzGDM8mX_exymgv9TuXgAojyE3KIhjA7aupMzOv-MxWplXSxQYooST-4fXlkWRilFzA" 
        user_jwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhjVURhSHYyTTFIcHlXYjlyYjhKaiJ9.eyJpc3MiOiJodHRwczovL3VkMjMudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDY0ODA1ZDA3NzQ2ZDg4OTdmMWM3OTlkMCIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2ODYxMzQwOTgsImV4cCI6MTY4NjE0MTI5OCwiYXpwIjoiQUtSQzlBYVFHM21GMDEzcUF4RGNWYTA3R1o1Q05XaHUiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.Wt0_ByME4tVLA-gmVKihhOMn4KzRSz9Hgx4wNDOLcNKJvKXO4By3YW6W5QOotGoL2awze_y0_BinH-N4Vu1w2LZKHewXe4x8mIBzlcTyrZ2dBiIRZBATsPjbUWfGY1nCfHlqMIkEcwUtDBZhBoJxu0jHNPIAYmwOJYCtL1NmI0nv6R0-LQqU9lQZh9wL92neMd5PEwgFypYdtorOfhz9ApJ3kcggo8hytt7D8ghC7GDIW3u_lKFh76QT9Rxrx-FBWKYeNOUJK6vRxb8HCO4I7jEW2CCzSLvQ_ditvr2DZNsMjLcLEtS3Vc-53RiVUW4lZKoFAKU2oa-mSnVgzDPh5w"
        self.user_header = {'Authorization': 'Bearer' + user_jwt}
        self.admin_header = {'Authorization': 'Bearer' + admin_jwt}

        self.db_path = DATABASE_URL

        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, self.db_path)
        # class Actors(db.Model):
        #     __tablename__ = 'actors'

        #     id = Column(Integer, primary_key=True)
        #     name = Column(String)
        #     gender = Column(String)
        #     age = Column(Integer)
        # class Movies(self.db.Model):
        #     __tablename__ = 'movies'

        #     id = Column(Integer, primary_key=True)
        #     title = Column(String)
        #     release_date = Column(Date)

        self.post_actor1 = {
            'name': "actorq",
            'age': 23,
            'gender': 'MALE'
        }

        self.post_actor1 = {
            'name': "actor2",
            'age': 25,
            'gender': 'MALE'
        }

        self.post_actor2 = {
            'name': "actor3",
            'age': 33,
            'gender': 'FEMALE'
        }
        self.post_movie1 = {
            'title': "MOVIE1",
            'release_date': "12/11/2020"
        }

        self.post_movie2 = {
            'title': "movie2",
            'release_date': "12/11/2020"
        }

        self.post_movie3 = {
            'title': "movie3",
            'release_date': "12/11/2020"
        }
        print(self.post_movie3)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        def test_get_actors():
            res = self.client.get('/actors',headers=self.admin_header)

            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(len(data['actors']))

        def test_get_movies(self):
            res = self.client().get('/movies',
                                    headers=self.admin_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(len(data['movies']))

        def test_422_create_actor(self):
            new_actor = {}
            res = self.client().post('/actors', json=new_actor,
                                    headers=self.admin_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)
            self.assertEqual(
                data['message'],
                    "error")
        def test_create_movie(self):
            new_movie = {'title': 'movie',
                        'release_date': '6/8/2021'}
            res = self.client().post('/movies', json=new_movie,
                                    headers=self.admin_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)

        def test_422_create_movie(self):
            new_movie = {}
            res = self.client().post('/movies', json=new_movie,
                                    headers=self.admin_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)
            self.assertEqual(
                data['message'],
                "error")
        def test_delete_actor(self):
            res = self.client().delete('/actors/1', headers=self.admin_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['delete'], 1)
        def test_422_delete_actor(self):
            res = self.client().delete('/actors/400', headers=self.admin_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)
            self.assertEqual(
                data['message'],
                "error")
            
        def test_delete_movie(self):
            res = self.client().delete('/movies/1', headers=self.admin_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['delete'], 1)
        def test_422_delete_movie(self):
            res = self.client().delete('/movies/400', headers=self.admin_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)
            self.assertEqual(
                data['message'],
                "error")

        def test_update_actor(self):
            update_actor = {'name': 'rr','age':34,'gender':"MALE"}
            res = self.client().patch('/actors/2', json=update_actor,
                                    headers=self.admin_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)

        def test_422_update_actor(self):
            update_actor = {}
            res = self.client().patch('/actors/2', json=update_actor,
                                    headers=self.admin_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)
            self.assertEqual(
                data['message'],
                """Unprocessable Entity.""")
            
        def test_update_movie(self):
            update_movie = {'title': 'rr','release_date':"12/12/2020"}
            res = self.client().patch('/movies/2', json=update_movie,
                                    headers=self.admin_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)

        def test_422_update_movie(self):
            update_movie = {}
            res = self.client().patch('/actors/2', json=update_movie,
                                    headers=self.admin_header)
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)
            self.assertEqual(
                data['message'],
                """Unprocessable Entity.""")


        # user test

    def test_get_actors_user(self):
        res = self.client().get('/actors',
                                headers=self.user_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))


    def test_get_422_actors_user(self):
        res = self.client().get('/actors/233',
                                headers=self.user_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(
                data['message'],
                """Unprocessable Entity.""")
        
    def test_get_movies_user(self):
        res = self.client().get('/movies',
                                headers=self.user_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))


    def test_get_422_movies_user(self):
        res = self.client().get('/movies/233',
                                headers=self.user_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(
                data['message'],
                """Unprocessable Entity.""")
        

if __name__ == "__main__":
    unittest.main()






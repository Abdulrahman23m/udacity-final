# Casting Agency App
This app is a Udacity project.it is the final project of the full stack Nanodegree course. This app is a casting agency that connects actors to movies. it is hosted in Heroku and uses auth0.


## Getting started 


### Dependencies 
This app runs in python 3.10 and the list of dependancies are listed in requirements.txt .

```bash
pip install -r requirements.txt
```

### Environment 
Make sure that the you set the env values in setup.sh before running. 


```bash
export DATABASE_URL= url
# export DATABASE_URL='postgresql://postgres@localhost:5432/postgres'
export EXCITED="true"

#Auth0
export AUTH0_DOMAIN="ud23.us.auth0.com"
export ALGORITHMS=['RS256']
export API_AUDIENCE="casting"

echo "setup.sh script executed successfully!"
```


## Run
To run first set the env variables in bash

```bash
chmod +x setup.sh
source setup.sh
echo $DATABASE_URL
```

### local run
to local run the app.
```bash
python app.py
```
### Heroku 
https://udacity-casting.herokuapp.com

## Roles 
There are two roles on this app 
1- admin
2- basic user 
#### admin 
has all permissions 
- get/actors 
- patch/actors
- delete/actors
- get/movies
- delete/movies
- patch/movies
#### user
- get/actors
- get/movies
## API
Casting agency API has multiple endpoints
- ENDPOINTS 
     - GET /actors return all actors in database. 
     - GET /actors/<id> return actor with specific id. 
     - PATCH /actors update actors data. must send a valid JSON object with all data.
     - DELETE /actors deletes actor by id.

     - GET /movies return all movies in database. 
     - GET /movies/<id> return movie with specific id. 
     - PATCH /movies update movie data. must send a valid JSON object with all data.
     - DELETE /movies deletes actor by id.


### To test app 
```bash
python test_app.py
```
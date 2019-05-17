# BBMDB - Django API example

Simple Django API example, which downloads movie data from OMDB and stores it in local database. It allows also comment movies, and display list of most commented movies.

## Installation and configuration

Bassicaly it requires only to set DJANGO_OMDB_API_KEY environment variable with your personal OMDB API key.

After that just run:

    python manage.py migrate

## Testing

All endpoints and I think all function are covered with automatic test, so running this command will ensure You that everythings works fine:

    python manage.py test
    

## Used and required libraries

Bassicaly it requires only those three packeges to be installed with **python-pip**:

    Django==2.2.1
    djangorestframework==3.9.4
    omdb==0.10.1

**Django** doesn't require any explanation. I used **djangorestframework** to simplify handling requests and responses and **omdb** to avoid writing communication with *OMDB* from scratch - which is easy but why preach to the converted?

## Enpoints

### /movies

##### GET
##### POST

### /comments

##### GET
##### POST

### /comments/{movie_id}

##### GET

### /top

##### GET

### /top/{from date}/{to date}

##### GET
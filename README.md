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

## Endpoints

### /movies

##### GET
* __params:__ -
* __response:__ List of all movies in database.


    [
        {
            "movie_id": [integer],
            "title": [string],
        },
        ...
    ]

##### POST
* __params:__ {"title":"_[movie title here]_"}
* __response:__


    {
        "movie_id": [integer],
        "title": [string],
        "year": [integer],
        "imdb_rating": [float],
        "director": [string],
        "comments_count": [integer]
    }

### /comments

##### GET
* __params:__ -
* __response:__ List of all comments for all movies, that exists in database.


    [
        {
            "comment_id": [integer],
            "movie_id": [integer],
            "content": [string],
            "created": [datetime],
        },
        ...
    ]
    
##### POST
* __params:__ {"movie_id": _[movie_id here]_,"content": "_[comment text here]_"}
* __response:__ 


    {
        "comment_id": [integer],
        "movie_id": [integer],
        "content": [string],
        "created": [datetime],
    }

### /comments/{movie_id}

##### GET
* __params:__ Just _movie_id_ in url.
* __response:__ List of all comments for selected movie, that exists in database.


    [
        {
            "comment_id": [integer],
            "movie_id": [integer],
            "content": [string],
            "created": [datetime],
        },
        ...
    ]
    
### /top

##### GET
* __params:__ -
* __response:__ List of movies sorted descending by number of comments.


    [
        {
            "movie_id": [integer],
            "ranking": [integer],
            "comments_count": [integer],
        },
        ...
    ]

### /top/{from date}/{to date}

##### GET
* __params:__ Two dates ex.: _/top/1939-09-01/1945-05-08_
* __response:__ List of movies sorted descending by number of comments posted in selected date range.


    [
        {
            "movie_id": [integer],
            "ranking": [integer],
            "comments_count": [integer],
        },
        ...
    ]


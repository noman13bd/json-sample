# ToDos
ToDos APIs - 
------------------
* clone the repo
* cd into repo
* create virtual env
`python3 -m venv env`
* activate virtual env
`source env/bin/activate`
* install modules
`pip install -r requirements.txt`
* start docker (PostgreSQL will run on docker)
` docker-compose up -d`
* run DB migrations
`python3 manager.py db init`
`python3 manager.py db migrate`
`python3 manager.py db upgrade`
* start the server
`python3 server.py`
* access endpoints on `127.0.0.1:5000`
-----
END Points are:
1. `/api/v1/register` - POST
```json
{
    "name":"XYZ",
    "email":"xyz@abc.com",
    "password": "123456"
}
```
2. `/api/v1/login` - POST
```json
{
    "email":"xyz@abc.com",
    "password": "123456"
}
```
3. `/api/v1/todo` - POST
```json
{
    "title":"to do one",
    "isCompleted": 0
}
```
need to POST this with `Access-Token` in header. Login POST will return the needed token.

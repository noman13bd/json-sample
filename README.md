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
```{
    "name":"XYZ",
    "email":"xyz@abc.com",
    "password": "123456"
}```
2. `/api/v1/login` - POST
```{
    "email":"xyz@abc.com",
    "password": "123456"
}```

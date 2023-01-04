:fire:<mark>FAST API</mark>:fire:<br>

<h1> FastAPI Social Media </h1>

<h2> Description</h2>
This is an API in Python to CRUD a simple base social media with Users, Posts and Likes. The project is a learning class from [Sanjeev Corse](https://github.com/Sanjeev-Thiyagarajan/fastapi-course)
For this implementation I am using Fast Framerok with Postgres database, SQLAlchemy ORM, and Dockerization

<h2>Project Details</h2>

FastAPI is web framework for building APIs with Python 3.7+ based on standard Python type hints. [Documentation](https://fastapi.tiangolo.com/)
</br>
</br>


### Project Layout
```
root/
|
├── App/
|   ├── routers/
|   |  	 ├── auth.py
|   |  	 ├── post.py
|   |  	 ├── user.py
|   |  	 └── vote.py
|   ├── main.py
|   ├── database.py
|   ├── config.py
|   ├── models.py
|   ├── auth2.py
|   ├── schemas.py
|   └── utils.py
|
├── tests/
├── .env
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

### packages:
> python3 -> It is the Python Language Interpreter <br>
> sqlite3 -> A module to integrate the SQLite with Python <br>
> FastAPI -> Web Framework in Python
> SQLAlchemy -> ORM for Python <br>
> uvicorn -> An ASGI web server implementation for Python <br>
> alembic -> A lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python <br>
> passlib -> A password hashing library for Python <br>
> psycopg2 -> Driver - A mature driver for interacting with PostgreSQL from the Python scripting language <br>
> pydantic -> A Python library for data modeling/parsing that has efficient error handling and a custom validation mechanism <br>
> python-jose -> The JavaScript Object Signing and Encryption for JWT in python <br>

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Building

### DOckerization

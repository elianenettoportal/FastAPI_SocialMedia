:fire:<mark>FAST API</mark>:fire:<br>

<h1> FastAPI Social Media </h1>

<h2> Description</h2>
This is an API in Python to CRUD a simple base social media with Users, Posts and Likes. For this implementation I am using Fast Framerok with Postgres database, SQLAlchemy ORM, and Dockerization. <br>

> The project is a learning exercise from: [Sanjeev-Thiyagarajan](https://github.com/Sanjeev-Thiyagarajan/fastapi-course)

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
### Building localhost
To run this project in a local environment follow the steps below
1. Clone the repository
2. Install a Postgre database
3. Update the .env file with DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOSTNAME, DATABASE_PORT and DATABASE_NAME
4. Execute the comand to install all libraries:`pip install -r requirements.txt`
5. Execute the command to start the api: `uvicorn App.main:app`

### Building in Docker Container
To run this project, please follow steps below
1. Clone the repository
2. Go to the root package and run the command: <br>
```
  docker-compose up -d --build
```
> The command builds the containers: <br>
> a) API container -> The Social Media API <br>
> b) The Postegre Database <br>
> c) The UI Adminer to manage the Postgres Data Base. <br>

4. Go to the link http://localhost:8008/docs to play with the endpoints. This is a Swagger UI documentation.
> 1) Create a user  <br>
> POST - {{URL}}users/<br>
> 2) Execute Login with the credentials of the user logged<br>
> POST - {{URL}}login/<br>
> 3) Create Posts<br>
> POST {{URL}}posts/<br>
Swagger will also provide the endpoints in case you want to use Postman

5. To see the tables created go to http://localhost:8080/ and fill up the credentials like the image below:
![postgres](https://user-images.githubusercontent.com/6922622/210644671-3cebeeeb-6ff8-4e2a-8d0d-5e066f3eba26.jpg)
```
System = postgresSQL
servername = database
username = admin
password = password123
database = socialmedia_db
```
You should see the 3 main tables
![postgres2](https://user-images.githubusercontent.com/6922622/210645017-9c08b5f4-d2b6-42c8-a018-089765709f65.jpg)


### Docker
In docker-compose Note that the API uses the command to run the application and since it is dependent of the database, if sleeps while the database is created/started.
The `.env` file will have the credentials. <br>
We should never push to github an env file, however, since this is a learning project, I decided for pushing it to have it documented.<br>
<br>

You may want to visit the link below to understand better the Docker Compose file
https://testdriven.io/blog/fastapi-docker-traefik/

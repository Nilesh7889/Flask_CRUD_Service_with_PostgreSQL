## Flask CRUD service with PostgreSQL


### Introduction

Simple Flask CRUD service with PostgreSQL.


### Setup

1. Install Python version 3.8+ : https://www.python.org/downloads/
2. Clone or download this repository
3. Import project in IDE (PyCharm, VS Code)
4. Install Flask and required pkgs: open terminal enter-
  
   pip install flask

   pip install flask-sqlalchemy

   pip install Flask-Migrate

   
### Database setup
1. Install PostgreSQL
2. Open pgAdmin4- create new database authorization_service
3. Configure database connection
   Open config.py change username & password
    SQLALCHEMY_DATABASE_URI = 'postgresql://**username**:**password**@localhost/authorization_service'
4. Initialize the Database: Open terminal and enter below commands

   flask db init
   
   flask db migrate -m "initial migration"

   flask db upgrade

**Now, open run.py and Run.**

Service should start Running on http://127.0.0.1:5000.

![image](https://github.com/Nilesh7889/Flask_CRUD_Service_with_PostgreSQL/assets/43874699/f81f3544-eff4-4434-b8a0-1e5e2731394a)

Next, Download and Install Postman : https://www.postman.com/downloads/

### API Endpoints

1. **POST endpoint - Add User**

Open Postman and enter details for new user: 

![image](https://github.com/Nilesh7889/Flask_CRUD_Service_with_PostgreSQL/assets/43874699/67e3c53a-1a7b-4b02-a9ca-49e4acf8af59)
 
Click Send.

![image](https://github.com/Nilesh7889/Flask_CRUD_Service_with_PostgreSQL/assets/43874699/113b9fa1-bd0c-4486-9a22-c41a35cbe4bd)

Open database user table, new record should be added.

![image](https://github.com/Nilesh7889/Flask_CRUD_Service_with_PostgreSQL/assets/43874699/d4a7e723-101b-4870-a74c-0c9eca917449)


2. **GET endpoint - Get user details** 

Open Postman and enter details: 

![image](https://github.com/Nilesh7889/Flask_CRUD_Service_with_PostgreSQL/assets/43874699/7ff25eae-31e4-466e-a7f7-3acaad67751e)

Click Send.

![image](https://github.com/Nilesh7889/Flask_CRUD_Service_with_PostgreSQL/assets/43874699/2f54b240-b9c1-44b1-952b-03f0f8f0a734)


3. **PUT endpoint - Update user details**

Open Postman and enter updated details: 

![image](https://github.com/Nilesh7889/Flask_CRUD_Service_with_PostgreSQL/assets/43874699/d1795608-55ac-4738-80bc-675641db9239)

Click Send.

![image](https://github.com/Nilesh7889/Flask_CRUD_Service_with_PostgreSQL/assets/43874699/de0f396d-8e8c-40e7-95ea-202485d11959)

Open database user table, record with ID as 1 should be updated.

![image](https://github.com/Nilesh7889/Flask_CRUD_Service_with_PostgreSQL/assets/43874699/fdf54336-c8d6-4d23-9c7a-2cb7ec143d0f)


4. DELETE endpoint - delete user details

Open Postman and enter updated details: 

![image](https://github.com/Nilesh7889/Flask_CRUD_Service_with_PostgreSQL/assets/43874699/f16aa159-04da-4b09-8fe6-5732c8e3c957)

Click send.

204, No content

![image](https://github.com/Nilesh7889/Flask_CRUD_Service_with_PostgreSQL/assets/43874699/9ef8c3b8-fc83-4e12-aa40-55fcec3f98c1)

Open database user table, record with ID as 1 should be deleted.

![image](https://github.com/Nilesh7889/Flask_CRUD_Service_with_PostgreSQL/assets/43874699/dbc55fb2-1cf1-4649-9c88-4346eff34811)


### Running Unit Test

Go to tests folder, open tests_routes.py.

Click Run test.

Or right click on file and click run python tests..











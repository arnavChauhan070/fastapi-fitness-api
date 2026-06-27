#  Fitness Backend API

A RESTful Fitness Backend built using **FastAPI**, **SQLAlchemy**, and **SQLite**. This project allows users to manage fitness records, perform CRUD operations, and view a leaderboard based on workout speed.

##  Features

### User Management

* Create a user
* Get all users
* Get user by ID
* Update user (PUT)
* Partially update user (PATCH)
* Delete user

### Fitness Management

* Add a fitness record for a user
* Get all fitness records of a user
* Get fitness records by workout type
* Update fitness record
* Partially update fitness record
* Delete fitness record

### Leaderboard

* View the Top 10 users for a selected workout type.
* Leaderboard is ranked using:

```
Speed = Distance / Time
```

---

##  Tech Stack

* Python 3.9
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

---

## 📁 Project Structure

```
Fitness_Backend/
│
├── main.py          # API Routes
├── database.py      # Database models & configuration
├── model.py         # Pydantic request/response models
├── helper.py        # Utility functions
├── Fitness.db       # SQLite database
└── README.md
```

---

##  API Endpoints

### User

| Method | Endpoint   | Description           |
| ------ | ---------- | --------------------- |
| POST   | /user      | Create a user         |
| GET    | /user      | Get all users         |
| GET    | /user/{id} | Get user by ID        |
| PUT    | /user/{id} | Update user           |
| PATCH  | /user/{id} | Partially update user |
| DELETE | /user      | Delete user           |

### Fitness

| Method | Endpoint      | Description                     |
| ------ | ------------- | ------------------------------- |
| POST   | /fitness      | Add fitness record              |
| GET    | /fitness/{id} | Get all workouts of a user      |
| GET    | /fitness      | Filter workouts by type         |
| PUT    | /fitness      | Update fitness record           |
| PATCH  | /fitness      | Partially update fitness record |
| DELETE | /fitness      | Delete fitness record           |

### Leaderboard

| Method | Endpoint     | Description                  |
| ------ | ------------ | ---------------------------- |
| GET    | /leaderboard | Top 10 users ranked by speed |

---

## ▶ Running the Project

Clone the repository:

```bash
git clone <https://github.com/arnavChauhan070/fastapi-fitness-api.git>
```

Move into the project directory:

```bash
cd Fitness_Backend
```

Install dependencies:

```bash
pip install fastapi sqlalchemy uvicorn pydantic
```

Run the server:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

##  What I Learned

This project helped me learn:

* FastAPI
* SQLAlchemy ORM
* CRUD APIs
* Pydantic Models
* Dependency Injection
* Database Relationships
* Foreign Keys
* Enums
* Error Handling
* REST API Design
* Leaderboard Implementation

---

##  Future Improvements

* JWT Authentication
* Password Hashing
* User Authentication & Authorization



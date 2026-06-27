from fastapi import FastAPI,Depends,HTTPException
from model import User_Create,User_Response,User_Update,User_Patch,Create_Fitness,Fitness_Type,Patch_Fitness,Update_Fitness,LeaderBoard
from database import get_db,User,Fitness
from sqlalchemy.orm import Session
from helper import get_user_by_email
from sqlalchemy.exc import IntegrityError



app = FastAPI()

#Home Route
@app.get("/")
def welcome():
    return {"message" : "Welcome to Home!!"}

#Create User
@app.post("/user")
def create_user(user_data : User_Create, session : Session = Depends(get_db)) -> User_Response:
    existing_user = get_user_by_email(session=session,email=user_data.email)

    if existing_user:
        print("User already Exists...")
        return
    
    db_user = User(name = user_data.name,email = user_data.email)
    try:
        session.add(db_user)
        session.commit()
    except IntegrityError as e:
        print(f"Error Caught!! as {e}")
        session.rollback()
    return db_user

#Get all User
@app.get("/user")
def get_all_user(session : Session = Depends(get_db)):
    users = session.query(User).all()
    return users

#Get a user by specific id
@app.get("/user/{id}")
def get_user_by_id(id : int,session : Session = Depends(get_db)):
    user = session.get(User,id)
    if not user:
        raise HTTPException(status_code=404,detail="No Account Found!!")
    return user

#Update a user whole
@app.put("/user/{id}")
def update_user_by_id(id : int,user_data: User_Update,session : Session = Depends(get_db)):
    user = session.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User not found!!!")
    
    user.name = user_data.name
    user.email = user_data.email

    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        print("Session RollBacked to Previous commit....")
    except Exception as e:
        print(f"Exception caught as {e}")

#Update a user but only 1 or may data 
@app.patch("/user/{id}")
def patch_user_by_id(id : int,user_data : User_Patch,session : Session = Depends(get_db)):
    user = session.get(User,id)

    if not user:
        raise HTTPException(status_code=404,detail="User not found!!!")
    
    user.name = user_data.name or user.name
    user.email = user_data.email or user.email

    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        print("Session RollBacked to Previous commit....")
    except Exception as e:
        print(f"Exception caught as {e}")


#Delete User
@app.delete("/user")
def delete_user_by_id(id : int , session : Session = Depends(get_db)):
    user = session.get(User,id)

    if not user:
        raise HTTPException(status_code=404,detail="User not found!!!")
    
    try:
        session.delete(user)
        session.commit()
    except IntegrityError:
        session.rollback()
        print("Session RollBacked to Previous commit....")
    except Exception as e:
        print(f"Exception caught as {e}")

    
#Fitness Routes

@app.post("/fitness")
def add_fitness(id : int,fitness : Create_Fitness,session : Session = Depends(get_db)):
    user = session.get(User,id)

    if not user:
         raise HTTPException(status_code=404,detail="User not found!!!")
    
    new_fitness = Fitness(
        type = fitness.type,
        distance = fitness.dist,
        time = fitness.time,
        user = user)
    
    try:
        user.fitness.append(new_fitness)
        #This .fintess comes from database - > User Class - > fintess valraible that defies relationship
        session.commit()
    except IntegrityError:
        session.rollback()
        print("Session RollBacked to Previous commit....")
    except Exception as e:
        print(f"Exception caught as {e}")

@app.get("/fitness/{id}")
def get_fitness_record(id : int,session : Session = Depends(get_db)):
    user = session.get(User,id)

    if not user:
        raise HTTPException(status_code=404,detail="User not Found!!")
    
    return user.fitness

@app.get("/fitness")
def get_fitness_record_by_type(id : int,type : Fitness_Type,session : Session = Depends(get_db)):
    user = session.get(User,id)

    if not user : 
        raise HTTPException(status_code=404,detail="User not Found!!")
    
    fitness_List = session.query(Fitness).filter(Fitness.user_id == id,Fitness.type == type).all()
    return fitness_List

@app.put("/fitness")
def update_fitness_record(id : int,fitness_id : int ,update_fitness : Update_Fitness,session : Session = Depends(get_db)):
    user = session.get(User,id)

    if not user:
        raise HTTPException(status_code=404,detail="User not Found!!")
    
    if fitness_id != user.id :
        raise HTTPException(status_code=404,detail=f"The Workout is not registered with this USER : {user}")
    
    fitness_record = session.get(Fitness,fitness_id)

    fitness_record.type = update_fitness.type
    fitness_record.distance = update_fitness.dist
    fitness_record.time = fitness_record.time

    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        print("Session RollBacked to Previous commit....")
    except Exception as e:
        print(f"Exception caught as {e}")

@app.patch("/fitness")
def patch_fitness_record(id : int , fitness_id : int , fitness : Patch_Fitness , session : Session = Depends(get_db)):
    user = session.get(User,id)

    if not user:
        raise HTTPException(status_code=404,detail= "User Not Found!!")
    
    if fitness_id != user.id :
        raise HTTPException(status_code=404,detail=f"The Workout is not registered with this USER : {user}")
    
    fitness_record = session.get(Fitness,fitness_id)

    fitness_record.type = fitness.type or fitness_record.type
    fitness_record.distance = fitness.dist or fitness_record.distance
    fitness_record.time = fitness.time or fitness_record.time

    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        print("Session RollBacked to Previous commit....")
    except Exception as e:
        print(f"Exception caught as {e}")


@app.delete("/fitness")
def delete_fitness_by_id(fitness_id : int,session : Session = Depends(get_db)):
    fitness = session.get(Fitness,fitness_id)

    if not fitness:
        raise HTTPException(status_code=404,detail="Workout Doesnt Exist")
    
    try:
        session.delete(fitness)
        session.commit()
    except IntegrityError:
        session.rollback()
        print("Session RollBacked to Previous commit....")
    except Exception as e:
        print(f"Exception caught as {e}")

#Top 10
@app.get("/leaderboard")
def get_leaderboard(type : Fitness_Type,session : Session = Depends(get_db)):
    fitness_record = session.query(Fitness).filter(Fitness.type == type).all()

    leaderboard = []
    
    for fitness in fitness_record:
        user_name = fitness.user.name
        try:
            speed = fitness.distance / fitness.time
        except ZeroDivisionError:
            print("Can't Divide by Zero!!")
        
        new_record = LeaderBoard(
            name=user_name,
            type=type,
            dist = fitness.distance,
            time = fitness.time,
            speed = speed
        )

        leaderboard.append(new_record)

    return list(sorted(leaderboard,key= lambda record : record.speed,reverse=True))[:10]







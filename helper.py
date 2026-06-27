from sqlalchemy.orm import Session
from database import User,Fitness
#Utilty Functions

def get_user_by_email(session : Session,email : str):
    return session.query(User).filter_by(email = email).first()
from sqlalchemy import create_engine,Column,ForeignKey,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.exc import IntegrityError

#Databse creation

engine = create_engine("sqlite:///Fitness.db",echo=False)
Base = declarative_base()
Session = sessionmaker(bind = engine)


def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True)
    name = Column(String(50),nullable=False)
    email = Column(String(50),nullable=False)
    fitness = relationship('Fitness',back_populates='user',cascade='all,delete-orphan')
    
class Fitness(Base):
    __tablename__ = "fitness"
    id = Column(Integer,primary_key=True)
    type = Column(String(50),nullable=False)
    distance = Column(Float,nullable=False)
    time = Column(Float,nullable=False)
    user_id = Column(Integer,ForeignKey("user.id"))
    user = relationship('User',back_populates='fitness')

Base.metadata.create_all(bind=engine)
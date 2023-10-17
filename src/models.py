import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
   
    favorite_characters = relationship('FavoriteCharacter', back_populates='user')
    favorite_planets = relationship('FavoritePlanet', back_populates='user')



class FavoriteCharacter(Base):
    __tablename__ = 'favorite_characters'
    
    character_id = Column(Integer, ForeignKey('character.character_id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planets'
    
    planet_id = Column(Integer, ForeignKey('planet.planet_id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))        

class Character(Base):
    __tablename__ = 'character'
    character_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

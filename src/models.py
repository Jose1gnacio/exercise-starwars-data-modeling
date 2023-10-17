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
   
    favorites = relationship('Favorite', back_populates='user')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)

    user = relationship('User', back_populates='favorites')
    characters = relationship('Character', secondary='favorite_characters')
    planets = relationship('Planet', secondary='favorite_planets')

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_characters'
    favorite_id = Column(Integer, ForeignKey('favorite.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey('character.character_id'))

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planets'
    favorite_id = Column(Integer, ForeignKey('favorite.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.planet_id'))

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

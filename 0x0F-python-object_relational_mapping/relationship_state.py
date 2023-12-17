#!/usr/bin/python3
"""
Contains the class definition of a State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")


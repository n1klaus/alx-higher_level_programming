#!/usr/bin/python3
""" Module containing the class definition of a City
    and an instance of a declarative base.
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from model_state import Base


class City(Base):
    """ Class definition for table 'cities'. """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey("states.id"))
    __table_args__ = (UniqueConstraint("id"), )

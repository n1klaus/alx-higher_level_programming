#!/usr/bin/python3
""" Module containing the class definition of a State
    and an instance of a declarative base.
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint


Base = declarative_base()


class State(Base):
    """ Class definition for table 'states'. """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    __table_args__ = (UniqueConstraint("id"), )

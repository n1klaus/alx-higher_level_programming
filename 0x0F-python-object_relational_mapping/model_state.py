#!/usr/bin/python3
""" Module containing the class definition of a State
    and an instance of a declarative base.
"""


from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Metadata, Column, Integer, String, UniqueConstraint

meta = Metadata()
Base = declarative_base(metadata=meta)


class State(Base):
    """ Class definition for table 'states'. """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    city = relationship("City")
    __table_args__ = (UniqueConstraint("id"), )

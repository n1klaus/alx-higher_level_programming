#!/usr/bin/python3
""" Module containing the class definition of a City
"""


from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from relationship_state import Base


class City(Base):
    """ Class definition for table 'cities'. """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    __table_args__ = (UniqueConstraint("id"), )

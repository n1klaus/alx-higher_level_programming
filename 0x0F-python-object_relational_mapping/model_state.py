#!/usr/bin/python3
""" Module containing the class definition of a State
    and an instance of a declarative base.
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sys import argv
import urllib.parse


host = "localhost"
port = 3309

Base = declarative_base()

if __name__ == "__main___":
    if len(argv) == 4:
        username = str(argv[1])
        passwd = urllib.parse.quote_plus(str(argv[2]))
        db = str(argv[3])
        url = f"mysql://{username}:{passwd}@{host}:{port}/{db}"
        engine = create_engine(url, echo=True)
        Base.metadata.create_all(engine)


class State(Base):
    """ Class definition for table 'states'. """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    __table_args__ = (UniqueConstraint("id"), )

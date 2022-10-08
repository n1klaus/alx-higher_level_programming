#!/usr/bin/python3
""" Module to list all State objects from the database hbtn_0e_6_usa
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
import urllib.parse
from model_state import Base, State


host = "localhost"
port = 3309

Base = declarative_base()

if __name__ == "__main___":
    if len(argv) == 4:
        username = str(argv[1])
        passwd = urllib.parse.quote_plus(str(argv[2]))
        db = str(argv[3])
        url = f"mysql+mysqldb://{username}:{passwd}@{host}:{port}/{db}"
        engine = create_engine(url, pool_pre_ping=True)
        Session = sessionmaker()
        Session.configure(bind=engine)
        Base.metadata.create_all(engine)
        session = Session()
        for instance in session.query(State).order_by(State.id).all():
            print(f"{instance.id}: {instance.name}")


#!/usr/bin/python3
""" Module to list all State objects from the database hbtn_0e_6_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv, stdout, exit
import urllib.parse
from model_state import Base, State


host = "localhost"
port = 3306

if __name__ == "__main__":
    if len(argv) == 4:
        username = str(argv[1])
        passwd = urllib.parse.quote_plus(str(argv[2]))
        db = str(argv[3])
        url = f"mysql+mysqldb://{username}:{passwd}@{host}:{port}/{db}"
        engine = create_engine(url)
        Base.metadata.create_all(engine)
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        for instance in session.query(State).order_by(State.id).all():
            stdout.write(f"{instance.id}: {instance.name}\n")
        session.close()
    exit()

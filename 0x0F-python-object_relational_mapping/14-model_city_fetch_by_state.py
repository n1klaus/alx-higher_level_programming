#!/usr/bin/python3
""" Module to print all City objects from the database hbtn_0e_14_usa
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
        try:
            username = str(argv[1])
            passwd = urllib.parse.quote_plus(str(argv[2]))
            db = str(argv[3])
            url = f"mysql+mysqldb://{username}:{passwd}@{host}:{port}/{db}"
            engine = create_engine(url, pool_pre_ping=True)
            Base.metadata.create_all(engine)
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            for instance in (session.query(
                                 State.name, City.id, City.name).filter(
                                 City.state_id == State.id).order_by(
                                 City.id).all()):
                stdout.write(f"{instance[0]}: ({instance[1]}) {instance[2]}\n")
        except Exception as e:
            raise
        finally:
            exit()

#!/usr/bin/python3
""" Module to list all the State objectand corresponding city objects
    to the database hbtn_0e_101_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv, stdout, exit
import urllib.parse
from relationship_state import Base, State
from relationship_city import City


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
            for state_instance in session.query(State).order_by(State.id):
                stdout.write(f"{state_instance.id}: {state_instance.name}\n")
                for city_instance in state_instance.cities:
                    stdout.write(
                              f"\t{city_instance.id}: {city_instance.name}\n")
        except Exception as e:
            raise
        finally:
            exit()

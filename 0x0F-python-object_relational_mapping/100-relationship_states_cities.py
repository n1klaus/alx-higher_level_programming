#!/usr/bin/python3
""" Module to adds the State object 'California', with city 'San Francisco'
    to the database hbtn_0e_100_usa
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
            my_state = State(name="California")
            my_city = City(name="San Francisco")
            my_state.cities.append(my_city)
            session.add(my_state)
            session.add(my_city)
            session.commit()
        except Exception as e:
            raise
        finally:
            exit()

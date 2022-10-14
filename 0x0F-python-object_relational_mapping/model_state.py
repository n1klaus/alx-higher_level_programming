#!/usr/bin/python3
""" Module containing the class definition of a State
    and an instance of a declarative base.
"""


from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sys import argv, exit


Base = declarative_base()


class State(Base):
    """ Class definition for table 'states'. """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    city = relationship("City")
    __table_args__ = (UniqueConstraint("id"), )


if __name__ == '__main__':
    if len(argv) == 4:
        host = 'localhost'
        port = 3306
        try:
            user = str(argv[1])
            passwd = str(argv[2])
            db = str(argv[3])
            db_url = f"mysql+mysqldb//{user}:{passwd}@{host}:{port}/{db}"
            engine = create_engine(db_url, pool_pre_ping=True)
            Base.metadata.create_all(engine)
        except Exception:
            raise
        finally:
            exit()

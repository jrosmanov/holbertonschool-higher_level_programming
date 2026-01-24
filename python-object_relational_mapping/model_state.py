#!/usr/bin/python3
"""State class definition linked to the MySQL states table"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """creaded class for state"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./model_state.py <username> <password> <database>")
        exit(1)

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{password}@localhost/{db_name}',
    pool_pre_ping=True)
    Base.metadata.create_all(engine)
    print("Table 'states' created (if it did not exist).")

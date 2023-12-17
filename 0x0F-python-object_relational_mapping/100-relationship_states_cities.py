#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


def create_data(engine):
    """Create California state with San Francisco city"""
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California", cities=[City(name="San Francisco")])
    session.add(new_state)
    session.commit()
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
        create_data(engine)
    else:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))


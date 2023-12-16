#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    try:
        # Set up the connection to the database
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)

        # Create a session
        session = Session(engine)

        # Query to get all states with a name containing the letter a
        states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

        # Delete the selected states
        for state in states_to_delete:
            session.delete(state)

        # Commit the changes
        session.commit()

        # Close the session
        session.close()

    except Exception as e:
        try:
            print("Error: {}".format(str(e)))
        except IndexError:
            print("Error: {}".format(str(e)))


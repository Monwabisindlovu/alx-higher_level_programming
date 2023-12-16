#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa.
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

        # Query to get the state with ID 2
        state_to_update = session.query(State).filter_by(id=2).first()

        # Check if the state exists before updating
        if state_to_update:
            state_to_update.name = "New Mexico"
            session.commit()

        # Close the session
        session.close()

    except Exception as e:
        try:
            print("Error: {}".format(str(e)))
        except IndexError:
            print("Error: {}".format(str(e)))


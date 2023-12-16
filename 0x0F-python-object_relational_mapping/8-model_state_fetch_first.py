#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
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

        # Query the first State object and print it
        first_state = session.query(State).order_by(State.id).first()
        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")

        # Close the session
        session.close()

    except Exception as e:
        try:
            print("Error: {}".format(str(e)))
        except IndexError:
            print("Error: {}".format(str(e)))


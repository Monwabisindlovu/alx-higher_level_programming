#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa.
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

        # Create a new State object
        new_state = State(name="Louisiana")

        # Add the new State object to the session
        session.add(new_state)

        # Commit the changes to the database
        session.commit()

        # Print the new state's ID
        print(new_state.id)

        # Close the session
        session.close()

    except Exception as e:
        try:
            print("Error: {}".format(str(e)))
        except IndexError:
            print("Error: {}".format(str(e)))


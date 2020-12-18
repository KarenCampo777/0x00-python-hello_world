#!/usr/bin/python3
"""
   Script that changes the name of a State object from the database
"""
if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    # Creates the engine we need
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = State(name="Louisiana")
    session.add(state_name)
    session.commit()
    print(state_name.id)
    session.close()

#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database
"""

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    for value in Session().query(State).order_by(State.id).all():
        if 'a' in value.name:
            print("{}: {}".format(value.id, value.name))

        Session().close()

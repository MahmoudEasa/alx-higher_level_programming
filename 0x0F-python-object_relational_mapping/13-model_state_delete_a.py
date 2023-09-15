#!/usr/bin/python3

"""Script that deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa
"""


def main():
    """Fuction to delete all State objects with a name
        containing the letter a from the database hbtn_0e_6_usa
    """
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker, Session
    from sqlalchemy import (create_engine)

    argv = sys.argv

    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
@localhost/{argv[3]}")

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.name.like("%a%"))\
        .delete(synchronize_session='fetch')
    session.commit()


if __name__ == "__main__":
    main()

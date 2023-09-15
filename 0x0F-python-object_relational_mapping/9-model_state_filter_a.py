#!/usr/bin/python3

"""Script that lists all State objects that contain the letter a
    from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker, Session
    from sqlalchemy import (create_engine)
    from model_state import Base, State

    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}\
:{sys.argv[2]}@localhost/{sys.argv[3]}")

    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State).filter(State.name.like("%a%")).all()

    for c in q:
        print(f"{c.id}: {c.name}")

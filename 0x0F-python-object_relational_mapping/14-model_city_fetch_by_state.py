#!/usr/bin/python3

"""Script that prints all City objects from the database hbtn_0e_14_usa
"""


def main():
    """Function to print all City objects from the database hbtn_0e_14_usa
    """
    import sys
    from sqlalchemy.orm import sessionmaker, Session
    from sqlalchemy import (create_engine)
    from model_state import Base, State
    from model_city import City

    argv = sys.argv

    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
@localhost/{argv[3]}")

    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State.name, City.id, City.name).outerjoin(State)\
        .filter(State.id == City.state_id).order_by(City.id).all()

    for c in q:
        print(f"{c[0]}: ({c[1]}) {c[2]}")


if __name__ == "__main__":
    main()

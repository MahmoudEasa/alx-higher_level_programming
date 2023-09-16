#!/usr/bin/python3

"""Script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""


def main():
    """Function to lists all State objects, and corresponding City objects
    """
    import sys
    from sqlalchemy.orm import sessionmaker, Session
    from sqlalchemy import create_engine
    from relationship_state import Base, State
    from relationship_city import City

    argv = sys.argv
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
@localhost/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State).all()

    for state in q:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    main()

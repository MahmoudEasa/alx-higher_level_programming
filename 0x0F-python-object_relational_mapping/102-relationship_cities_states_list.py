#!/usr/bin/python3

"""Script that lists all City objects from the database hbtn_0e_101_usa
"""


def main():
    """Function to lists all City
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

    q = session.query(City).order_by(City.id)

    for city in q:
        print(f"{city.id}: {city.name} -> {city.state.name}")


if __name__ == "__main__":
    main()

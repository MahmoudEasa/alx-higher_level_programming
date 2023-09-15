#!/usr/bin/python3

"""Script that creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa
"""


def main():
    """Function to creates the State “California”
        with the City “San Francisco”
    """
    import sys
    from sqlalchemy.orm import sessionmaker, Session
    from sqlalchemy import (create_engine)
    from relationship_state import Base, State
    from relationship_city import City

    argv = sys.argv

    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
@localhost/{argv[3]}")

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    st = State(name="California")
    session.add(st)
    session.commit()

    c = City(name="San Francisco", state_id=st.id)
    session.add(c)
    session.commit()


if __name__ == "__main__":
    main()

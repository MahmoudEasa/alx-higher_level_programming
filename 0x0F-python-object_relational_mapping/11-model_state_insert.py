#!/usr/bin/python3

"""Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker, Session
    from sqlalchemy import (create_engine)

    argv = sys.argv

    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
@localhost/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    s = State(name="Louisiana")
    session.add(s)
    session.commit()
    print(s.id)

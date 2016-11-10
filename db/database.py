## INFO ##
## INFO ##

# Import sqlalchemy modules
from sqlalchemy                 import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm             import scoped_session, sessionmaker

# Import pop modules
from config import SQLALCHEMY_DATABASE_URI

engine  = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
Base = declarative_base()
Base.query = session.query_property()

#------------------------------------------------------------------------------#
def initialise():
    import db.models
    Base.metadata.create_all(bind=engine)

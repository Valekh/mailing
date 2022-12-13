from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()

SessionLocal = sessionmaker(autoflush=False, bind=engine)
Session = SessionLocal()


class Mailing(Base):
    __tablename__ = 'mailing'

    id = Column(Integer, primary_key=True, index=True)
    start = Column(DateTime)
    text = Column(String)
    filters = Column(JSON)
    end = Column(DateTime)


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(Integer)
    operator_cod = Column(Integer)
    tag = Column(String)
    timezone = Column(String)


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    sending_date = Column(DateTime)
    status = Column(String)
    mailing_id = Column(Integer)
    client_id = Column(Integer)


Base.metadata.create_all(bind=engine)

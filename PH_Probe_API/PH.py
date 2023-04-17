from sqlalchemy import create_engine, Column, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta

engine = create_engine('sqlite:///data.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class PH(Base):
    __tablename__ = 'ph'
    id = Column(Float, primary_key=True)
    value = Column(Float, nullable=False)
    datetime = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"PH(id={self.id}, value={self.value}, datetime={self.datetime})"


Base.metadata.create_all(engine)

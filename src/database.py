from typing import AsyncGenerator
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from src.config import settings

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
)

async_session_factory = async_sessionmaker(async_engine)

class Base(DeclarativeBase):
    pass

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session


# class Car(Base):
#     __tablename__ = 'cars'
#     id = Column(Integer, primary_key=True)
#     car_brand = Column(String)
#     car_model = Column(String)
#     car_color = Column(String)
#     car_plate = Column(String)
#     car_type = Column(String)
#     num_seats = Column(Integer)
#
# class Driver(Base):
#     __tablename__ = 'drivers'
#     id = Column(Integer, primary_key=True)
#     license_num = Column(Integer)
#     car_id = Column(Integer, ForeignKey('cars.id'))
#     car = relationship('Car')
#     car_owner = Column(String)
#     car_owner_contact = Column(String)
#     trips = Column(Integer, default=0)
#     rating = Column(Float, default=0.0)
#
# class Passenger(Base):
#     __tablename__ = 'passengers'
#     id = Column(Integer, primary_key=True)
#     trips = Column(Integer, default=0)
#     rating = Column(Float, default=0.0)
#
# class UserInfo(Base):
#     __tablename__ = 'user_info'
#     id = Column(Integer, primary_key=True)
#     is_driver = Column(Boolean, default=False)
#     driver_id = Column(Integer, ForeignKey('drivers.id'), nullable=True)
#     ws = relationship('Driver', backref='user_info', uselist=False)
#     passenger_id = Column(Integer, ForeignKey('passengers.id'), nullable=True)
#     passenger = relationship('Passenger', backref='user_info', uselist=False )
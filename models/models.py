from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, TIMESTAMP, create_engine, BigInteger, text
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase

from typing import Annotated
import datetime

metadata = MetaData()

Driver = Table(
    'driver',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('created_at', TIMESTAMP, nullable=False, server_default=text("TIMEZONE('utc', now())")),
    Column('title', String, nullable=False),
    Column('active', Integer, nullable=False, default=False),
    Column('car_info', String, nullable=False),
    Column('stars', Integer, nullable=False),
    Column('num_trips', Integer, nullable=False),
)

Passenger = Table(
    'passenger',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('created_at', TIMESTAMP, nullable=False, server_default=text("TIMEZONE('utc', now())")),
    Column('title', String, nullable=False),
    Column('stars', Integer, nullable=False),
    Column('num_trips', Integer, nullable=False),
)

City = Table(
    'city',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('created_at', TIMESTAMP, nullable=False, server_default=text("TIMEZONE('utc', now())")),
    Column('title', String, nullable=False),
    Column('active', Integer, nullable=False, default=False),
)
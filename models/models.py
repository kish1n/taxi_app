from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text, func, BigInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Annotated
import datetime

from database import Base

intpk = Annotated[int, mapped_column(BigInteger, primary_key=True)]
name = Annotated[str, mapped_column(nullable=False)]
active = Annotated[bool, mapped_column(nullable=False, default=False)]
data_now = Annotated[datetime.datetime, mapped_column(nullable=False, server_default=text("TIMEZONE('utc', now())"))]

class Passenger(Base):
    __tablename__ = "passenger"
    id: Mapped[intpk]
    name: Mapped[name]
    city: Mapped[name]

class Driver(Base):
    __tablename__ = "driver"
    id: Mapped[intpk]
    name: Mapped[name]
    city: Mapped[name]
    car: Mapped[name]

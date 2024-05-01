from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text, func, BigInteger, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Annotated
import datetime

from models.database import Base

intpk = Annotated[int, mapped_column(BigInteger, primary_key=True)]
name = Annotated[str, mapped_column(nullable=False)]
active = Annotated[bool, mapped_column(nullable=False, default=False)]
data_now = Annotated[datetime.datetime, mapped_column(nullable=False, server_default=text("TIMEZONE('utc', now())"))]
email = Annotated[str, mapped_column(String(length=320), unique=True, index=True, nullable=False)]
username = Annotated[str, mapped_column(String(length=320), unique=True, index=True, nullable=False)]

class User(Base):
    __tablename__ = "user"

    id: intpk = Column(BigInteger, primary_key=True)
    username: name = Column(String, unique=True, nullable=True)
    email: email = Column(String, unique=True, nullable=False)
    hashed_password: name = Column(String, nullable=False)
    is_active: active = Column(Boolean, default=False)
    is_superuser: active = Column(Boolean, default=False)
    is_verified: active = Column(Boolean, default=False)
    is_driver: active = Column(Boolean, default=False)


class Driver(Base):
    __tablename__ = "driver"

    id: Mapped[intpk]
    username: Mapped[username]
    email: Mapped[email]
    hashed_password: Mapped[name]
    is_active: Mapped[active]
    is_superuser: Mapped[active]
    is_verified: Mapped[active]
    city: Mapped[name]
    car_model: Mapped[name]

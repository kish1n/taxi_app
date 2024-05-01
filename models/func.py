from sqlalchemy import text, insert, select, update
from datetime import datetime

from models.models import User, Driver
from models.database import async_sessionmaker, async_engine, Base


class Core:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            await conn.commit()

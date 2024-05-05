from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.database import Driver, Car, async_session_factory, async_engine, Base
from sqlalchemy.dialects.postgresql import insert
from src.auth.models import User

class Core:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            await conn.commit()

    @staticmethod
    async def toggle_user_attribute(user: User, attribute: str):
        async with async_session_factory() as session:
            try:
                stmt = select(User).where(User.id == user.id)
                result = await session.execute(stmt)
                user_from_db = result.scalars().first()
                current_value = getattr(user_from_db, attribute)
                print(f"Current {attribute} status before change: {current_value}")
                setattr(user_from_db, attribute, not current_value)
                new_value = getattr(user_from_db, attribute)
                print(f"New {attribute} status after change: {new_value}")
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e

    @staticmethod
    async def change_value(model, attribute, new_value):
        async with async_session_factory() as session:
            try:
                stmt = select(model).where(model.id == model.id)
                result = await session.execute(stmt)
                model_from_db = result.scalars().first()
                current_value = getattr(model_from_db, attribute)
                print(f"Current {attribute} status before change: {current_value}")
                setattr(model_from_db, attribute, new_value)
                new_value = getattr(model_from_db, attribute)
                print(f"New {attribute} status after change: {new_value}")
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e

    @staticmethod
    async def create_driver(id, license_num, car_id, car_owner, car_owner_contact, city):
        async with async_session_factory() as session:
            try:
                # Создание нового объекта Driver
                stmt = insert(Driver).values(
                    id=int(id),
                    license_num=int(license_num),
                    car_id=int(car_id),
                    car_owner=car_owner,
                    car_owner_contact=car_owner_contact,
                    trips=0,
                    rating=0.0,
                    city=city
                )
                on_conflict_stmt = stmt.on_conflict_do_update(
                    constraint='drivers_pkey',  # Указание на constraint первичного ключа
                    set_={
                        'license_num': stmt.excluded.license_num,
                        'car_id': stmt.excluded.car_id,
                        'car_owner': stmt.excluded.car_owner,
                        'car_owner_contact': stmt.excluded.car_owner_contact,
                        'city': stmt.excluded.city
                    }
                )
                await session.execute(on_conflict_stmt)
                await session.commit()
                print(f"Driver created with ID: {on_conflict_stmt}")
                return on_conflict_stmt

            except Exception as e:
                await session.rollback()
                print(f"Failed to create driver: {e}")
                raise

    @staticmethod
    async def reg_car(id, car_brand, car_model, car_color, car_plate, car_type, num_seats):
        async with async_session_factory() as session:
            try:
                # Создание нового объекта Car
                stmt = insert(Car).values(
                    id=int(id),
                    car_brand=car_brand,
                    car_model=car_model,
                    car_color=car_color,
                    car_plate=car_plate,
                    car_type=car_type,
                    num_seats=int(num_seats)
                )
                on_conflict_stmt = stmt.on_conflict_do_update(
                    constraint='cars_pkey',  # Указание на constraint первичного ключа
                    set_={
                        'car_brand': stmt.excluded.car_brand,
                        'car_model': stmt.excluded.car_model,
                        'car_color': stmt.excluded.car_color,
                        'car_plate': stmt.excluded.car_plate,
                        'car_type': stmt.excluded.car_type,
                        'num_seats': stmt.excluded.num_seats
                    }
                )
                await session.execute(on_conflict_stmt)
                await session.commit()
                print(f"Car with ID {id} has been registered or updated.")
                return {"message": "Car registered or updated successfully"}

            except Exception as e:
                await session.rollback()
                print(f"Failed to create car: {e}")
                raise
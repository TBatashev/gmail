import asyncpg
from tgbot.gmail_user import password
from sqlalchemy import BigInteger
from sqlalchemy.orm import relationship, Mapped , mapped_column , DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs , async_sessionmaker, create_async_engine

from tgbot import configs


engine = create_async_engine(configs.Config.SQLALCHEMY_URL, echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base) :

    __tablename__ = 'users'

    id_user : Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)

    

class StatesUSA(Base):
    __tablename__ = 'StatesUSA'

    id_st : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column()
    index : Mapped[int] = mapped_column()
    text : Mapped[str] = mapped_column()




async def async_main() :
    async with engine.begin() as conn :
        await conn.run_sync(Base.metadata.create_all)
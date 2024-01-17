from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table, Text
from sqlalchemy.orm import declarative_base
from database import engine
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


Base = declarative_base()
metadata = Base.metadata


user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", ForeignKey("my_users.id")),
    Column("role_id", ForeignKey("roles.id")),
)


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)

class User(Base):
    __tablename__ = "my_users"
    id = Column(Integer(), primary_key=True)
    username = Column(String(100), nullable=True)
    email = Column(String(100), nullable=False)
    password = Column(String(526), nullable=False)
    address = Column(String(100), nullable=True)
    roles: Mapped[List[Role]] = relationship(secondary=user_roles, lazy="joined")

class Post(Base):
    __tablename__ = "my_posts"
    id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(100), nullable=False)
    likes = Column(Integer(), nullable=True)


Base.metadata.create_all(engine)

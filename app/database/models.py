from sqlalchemy import Column, Integer, String, Date
from app.database.base import Base
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from app.database.base import Base
from sqlalchemy import Column, Integer, String, Date



class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, index=True)
    birthday = Column(Date)
    additional_info = Column(String, nullable=True)

ContactPydantic = sqlalchemy_to_pydantic(Contact)
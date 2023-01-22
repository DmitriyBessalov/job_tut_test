from typing import Optional
from pydantic import BaseModel, EmailStr


class Adress(BaseModel):
    region: str
    city: str
    street_type: Optional[str]
    street: Optional[str]
    house_type: Optional[str]
    house: Optional[str]
    value: str
    lat: float
    lng: float


class Salary(BaseModel):
    from_: int
    to: int
    currency: str
    gross: bool


class Contacts(BaseModel):
    fullName: str
    phone: str
    email: EmailStr


class Data(BaseModel):
    description: str
    employment: str
    address: Adress
    name: str
    salary: Salary
    contacts: Contacts

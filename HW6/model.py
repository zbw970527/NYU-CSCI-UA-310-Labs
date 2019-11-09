# columns and their types, including fk relationships
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# declarative base
from sqlalchemy.ext.declarative import declarative_base

# create the base class (declarative base)
# call it Base!
Base = declarative_base()


# implement the following three classes...

class Scooter(Base):
    __tablename__ = 'scooter'
    scooter_id = Column('scooter_id', Integer, primary_key=True)
    acquire_date = Column('acquire_date', Date)
    retired = Column('retired', Boolean, default=False)
    scooter_type_id = Column('scooter_type_id', Integer, ForeignKey('scooter_type.scooter_type_id'))

    scooter_type = relationship('ScooterType', back_populates='scooter')

    def __str__(self):
        return f'{self.scooter_id} {self.retired} {self.scooter_type_id.__str__} acquired at {self.acquire_date}'
    def __repr__(self):
        return f'{self.scooter_id} {self.retired} {self.scooter_type_id.__str__} acquired at {self.acquire_date}'
    def to_dict(self):
        dict = {
            'acquire_date': self.acquire_date.strftime('%Y-%m-%d'),
            'retired': self.retired,
            'scooter_type': self.scooter_type.model,
            'max_speed': self.scooter_type.max_speed,
            'weight': self.scooter_type.weight,
            'manufacturer': self.scooter_type.manufacturer.name,
            'website': self.scooter_type.manufacturer.website
        }
        return dict;


class ScooterType(Base):
    __tablename__ = 'scooter_type'
    scooter_type_id = Column('scooter_type_id', Integer, primary_key=True)
    model = Column('model', String)
    max_speed = Column('max_speed', Integer)
    max_range = Column('max_range', Integer)
    weight = Column('weight', Integer)
    company_id = Column('company_id', Integer, ForeignKey('company.company_id'))

    manufacturer = relationship('Company', back_populates='scooter_types')
    scooter = relationship('Scooter', back_populates='scooter_type')

    def __str__(self):
        return f'{self.manufacturer}{self.model}: max speed is {self.max_speed}, weight is {self.weight}'
    def __repr__(self):
        return f'{self.manufacturer}{self.model}: max speed is {self.max_speed}, weight is {self.weight}'

class Company(Base):
    __tablename__ = 'company'
    company_id = Column('company_id', Integer, primary_key=True)
    name = Column('name', String)
    website = Column('website', String)
    founded = Column('founded', Integer)

    scooter_types = relationship('ScooterType', back_populates='manufacturer')

    def __str__(self):
        return f'{self.name} {self.website} {self.founded}'
    def __repr__(self):
        return f'{self.name} {self.website} {self.founded}'

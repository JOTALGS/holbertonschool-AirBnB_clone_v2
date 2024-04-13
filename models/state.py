#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City",
            backref="state",
            cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            from models import storage
            c_instances = storage.all(City).values()
            m_cities = []
            for city in c_instances:
                if city.state_id == self.id:
                    m_cities.append(city)
            return m_cities
#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import MetaData, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
import models
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete, delete-orphan",
        )

    @property
    def cities(self):
        """
         A getter attribute 'cities' that returns the list of City
         instances with state_id equals to the current State.id
        """
        if getenv("HBNB_TYPE_STORAGE") == 'db':
            return self.cities
        else:
            list_of_cities = []
            for city in models.storage.all(City):
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities
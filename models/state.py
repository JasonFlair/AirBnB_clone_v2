#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import MetaData, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete, delete-orphan",
        passive_deletes=True,
    )

    @property
    def cities(self):
        """
         A getter attribute 'cities' that returns the list of City
         instances with state_id equals to the current State.id
        """
        list_of_cities = []

        for city in models.storage.all(City):
            if city.state_id == self.id:
                list_of_cities.append(city)
        return list_of_cities

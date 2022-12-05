#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import MetaData, Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False),
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship("Review", backref="place", cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", backref='place', secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """getter attribute to get the reviews of a place"""
            reviews_for_this_city = []
            for review_obj in models.storage.all(Review).values():  # returns all review objects
                if review_obj.place_id == self.id:
                    reviews_for_this_city.append(review_obj)

            return reviews_for_this_city

        @property
        def amenities(self):
            """returns amenities for this place"""
            amenity_ids_for_this_place = []
            for amenity in models.storage.all(Amenity):
                if amenity.id in self.amenity_ids:
                    amenity_ids_for_this_place.append(amenity)
            return amenity_ids_for_this_place

        @amenities.setter
        def amenities(self, obj):
            """adds id of object to the amenity_ids array"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)

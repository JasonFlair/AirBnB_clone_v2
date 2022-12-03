#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import MetaData, Column, Integer, String, DateTime, ForeignKey


class State(BaseModel):
    """ State class """
    name = Column(String(128), nullable=False)

    @property
    cities

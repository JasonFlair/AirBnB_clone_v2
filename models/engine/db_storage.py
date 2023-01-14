#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
import json
import models
from models.base_model import Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models in database"""

    arg_classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

    __engine = None
    __session = None

    def __init__(self):
        """ initialiser """
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}'
                                      ':3306/{}'.format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ returns all instances requested"""
        this_dict = {}
        if cls:
            query = self.__session.query(cls)
            for instance in query:
                key_name = cls.__name__ + "." + instance.id
                this_dict[key_name] = instance
                return this_dict
        else:
            for class_name in self.arg_classes:
                query = self.__session.query(class_name)
                for instance in query:
                    key_name = class_name.__name__ + "." + instance.id
                    this_dict[key_name] = instance
                    return this_dict

    def new(self, obj):
        """ adds a new object """
        self.__session.add(obj)

    def save(self):
        """save changes made"""
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes object"""
        self.__session.delete()

    def reload(self):
        """reload the instances from memory"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        
    def close(self):
        """calls close on the private session attribute (self.__session)"""
        self.__session.close()
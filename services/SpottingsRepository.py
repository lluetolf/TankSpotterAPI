import os
from pymongo import MongoClient


class SpottingsRepository(object):
    """ Repository implementing CRUD operations on Spottings collection in MongoDB """

    def __init__(self, srv):
        self.srv = srv
        self.client = MongoClient(srv)
        self.spottings = self.client['TankSpotterMDB'].spottings

    def read_all(self):
        return list(self.spottings.find({}, {"_id": 0}))
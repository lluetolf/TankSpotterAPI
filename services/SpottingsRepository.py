import os
import dateutil.parser
from pymongo import MongoClient


class SpottingsRepository(object):
    """ Repository implementing CRUD operations on Spottings collection in MongoDB """

    def __init__(self, srv):
        self.srv = srv
        self.client = MongoClient(srv)
        self.spottings = self.client['TankSpotterMDB'].spottings

    def read_all(self):
        return list(self.spottings.find({}, {"_id": 0}))

    def create(self, spotting):
        if spotting is not None:
            new_id = self._get_next_id()
            spotting['id'] = new_id
            spotting['created'] = dateutil.parser.isoparse(spotting['created'])
            spotting['spotTime'] = dateutil.parser.isoparse(spotting['spotTime'])
            self.spottings.insert(spotting)
            del(spotting['_id'])
            print("Created new field with id: {}".format(new_id))
            return spotting
        else:
            raise Exception("Nothing to save, because spottings parameter is None")

    def _get_next_id(self):
        tmp = self.spottings.find_one(sort=[("id", -1)])["id"]
        return tmp + 1
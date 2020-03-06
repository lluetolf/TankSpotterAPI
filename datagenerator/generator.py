import datetime
from json import JSONEncoder
from faker import Faker
import random
import json

Faker.seed(4321)
fake = Faker()

class Spotting():
    _statuses = ['Open', 'Verified', 'Rejected', 'Unknown']
    _own_troops = ['Company 1',
                   'Platoon 1.1', 'Squad 1.1.1', 'Squad 1.1.2', 'Squad 1.1.3', 'Squad 1.1.4',
                   'Platoon 1.2', 'Squad 1.2.1', 'Squad 1.2.2', 'Squad 1.2.3', 'Squad 1.2.4']
    _tanks = ['Centurion', 'T-54', 'M47 Patton', 'M48 Patton', 'T-55', 'Type 59', 'Type 61']

    def __init__(self, fake):
        self.id = fake.random.randint(1, 10000000000)
        self.created = fake.date_time_between(start_date='-30d', end_date='now')
        self.sensor = random.choice(self._own_troops)
        self.sender = random.choice(self._own_troops)
        self.status = random.choice(self._statuses)
        self.recipient = "All"
        self.observerLocation = ObserverLocation(fake)
        self.spotTime = fake.date_time_between(start_date='-30d', end_date='now')
        self.tankType = random.choice(self._tanks)
        self.spotLocation = ObserverLocation(fake)


class ObserverLocation():

    def __init__(self, fake):
        self.accuracy = random.random()
        lat, long = fake.local_latlng(country_code='US', coords_only=True)
        self.longitude, self.latitude = float(long), float(lat)


class MyEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return { "$date":  o.isoformat() }
        else:
            return o.__dict__


spottings = []
for _ in range(100):
    spottings.append(Spotting(fake))

with open('spottings.json', 'w') as f:
    json.dump(spottings, f, cls=MyEncoder)
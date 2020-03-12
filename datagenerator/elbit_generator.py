import datetime
from json import JSONEncoder
from faker import Faker
import random
import json

Faker.seed(4321)
fake = Faker()


class Unit():
    def __init__(self, name, long, lat, unittype):
        self.unittype = unittype
        self.lat = lat
        self.long = long
        self.name = name


class Spotting():
    _statuses = ['Open', 'Verified', 'Rejected', 'Unknown']
    _tanks = ['Centurion', 'T-54', 'M47 Patton', 'M48 Patton', 'T-55', 'Type 59', 'Type 61']
    _own_units = list(
        Unit('1/0/1/1/4', 47.6085736, 9.256542, 'Recc'),
        Unit('2/0/1/1/4', 47.6085736, 9.256542, 'Recc'),
        Unit('3/0/1/1/4', 47.6085736, 9.256542, 'Recc'),
        Unit('4/0/1/1/4', 47.6085736, 9.256542, 'Recc'),
        Unit('5/0/1/1/4', 47.6085736, 9.256542, 'Recc'),
        Unit('0/1/1/4', 47.6085736, 9.256542, 'Recc'),
        Unit('1/4', 47.6085736, 9.256542, 'Recc'),
    )
    enemy_activities = [
        { "etype": 'Tank', "long": 47.5956442, "lat": 9.285237 },
        { "etype": 'Inf', "long": 47.620181, "lat": 9.266059 }
    ]

    def __init__(self, fake, id):
        self.id = id
        self.created = fake.date_time_between(start_date='-1d', end_date='now')
        self.sensor = random.choice(self._own_troops)
        self.sender = random.choice(self._own_troops)
        self.status = random.choice(self._statuses)
        self.recipient = "All"
        self.observerLocation = None
        self.spotTime = fake.date_time_between(start_date='-30d', end_date='now')
        self.tankType = random.choice(self._tanks)
        self.spotLocation = None

class MyEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return {"$date": o.isoformat()}
        else:
            return o.__dict__


spottings = []
for i in range(100):
    spottings.append(Spotting(fake, i))

with open('spottings.json', 'w') as f:
    json.dump(spottings, f, cls=MyEncoder)

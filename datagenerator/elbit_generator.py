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
    _own_units = [
        Unit('1/0/1/1/4', 47.6085736, 9.256542, 'Recc'),
        Unit('2/0/1/1/4', 47.6085736, 9.256542, 'Recc'),
        Unit('3/0/1/1/4', 47.6085736, 9.256542, 'Recc'),
        Unit('4/0/1/1/4', 47.6085736, 9.256542, 'Recc'),
        Unit('5/0/1/1/4', 47.6085736, 9.256542, 'Recc'),
        Unit('0/1/1/4', 47.6085736, 9.256542, 'Recc'),
        Unit('1/4', 47.6085736, 9.256542, 'Recc')
    ]

    enemy_activities = [
        { "etype": 'Tank', "long": 47.5956442, "lat": 9.285237 },
        { "etype": 'Inf', "long": 47.620181, "lat": 9.266059 }
    ]

    _types = {
        'military unit': {
            'infantry': ['abraham', 'leo'],
            'special forces': ['panzerlis', 'bomberlis']
        },
        'civil event': {
            'natural': ['earthquake', 'storm'],
            'anthropic': ['demo', 'lütolfs furz']
        },
        'unknown': {
            '': ['']
        }
    }

    def __init__(self, fake, id):
        self.id = id
        self.created = fake.date_time_between(start_date='-1d', end_date='now')
        self.status = random.choice(self._statuses)
        self.category, catvalue = random.choice(list(self._types.items()))
        self.subtype, subvalue = random.choice(list(catvalue.items()))
        self.specific = random.choice(subvalue)
        self.spotTime = fake.date_time_between(start_date='-30d', end_date='now')

class MyEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return {"$date": o.isoformat()}
        else:
            return o.__dict__


spottings = []
for i in range(1):
    spottings.append(Spotting(fake, i))

with open('spottings.json', 'w') as f:
    json.dump(spottings, f, cls=MyEncoder)

from sqlalchemy.orm import sessionmaker
import db
from model import Company, ScooterType, Scooter, Base
from datetime import datetime
import random

Session = sessionmaker(db.engine)
session = Session()

# use the session object and imported classes (Company, Scooter, etc.)
# ... to create companies, types and scooters in teh database

c1 = Company()
c1.name = 'Super Fast Co'
c1.website = 'superfast.lol'
c1.founded = 2016

c2 = Company()
c2.name = 'Not Slow Co'
c2.website = 'notslow.lol'
c2.founded = 2014

c3 = Company()
c3.name = 'Seems Good Co'
c3.website = 'seemsgood.lol'
c3.founded = 2016

m_model = ["Scoot V1", "Scoot V2", "Scoot V3", "SuperStar v1", "SuperStar v2", "SuperStar v3", "CatchMe v1", "CatchMe v2", "CatchMe v3"]
m_range = [100, 110, 120, 130, 140]
m_weight = [15, 20, 25, 30]
m_speed = [15, 20, 25, 30, 35, 40, 45]
m_manufact = [c1, c2, c3]

type_res = []
for i in range(8):
    type = ScooterType(
        model = random.choice(m_model),
        max_speed = random.choice(m_speed),
        max_range = random.choice(m_range),
        weight = random.choice(m_weight),
        manufacturer = random.choice(m_manufact)
    )
    type_res.append(type);

scooter_res = []
for i in range(70):
    scoot = Scooter(
        acquire_date = f'{random.randint(2014,2018)}-{random.randint(1, 12):02}-{random.randint(1,28):02}',
        retired = True if random.randint(0,2)%2 != 0 else False,
        scooter_type = random.choice(type_res)
    )
    scooter_res.append(scoot);

#session.add_all(m_manufact)
#session.add_all(type_res)
session.add_all(scooter_res)
session.commit()

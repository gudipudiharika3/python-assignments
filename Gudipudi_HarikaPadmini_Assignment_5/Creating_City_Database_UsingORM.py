"""
HW: 5
Problem: 1
Author: Harika Padmini
"""
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, select

# declare base class
Base = declarative_base()


# defining class and schema
class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    population = Column(Integer)


engine = sqlalchemy.create_engine('sqlite:///city.db')
session = sessionmaker(bind=engine, future=True)()
# Creating the table 'City' in the database if it does not exist
Base.metadata.create_all(engine)
# Adding city data
new_york = City(name="New York", population=18593220)
cairo = City(name="Cairo", population=18771769)
osaka = City(name="Osaka", population=20237645)
beijing = City(name="Beijing", population=20383994)
mexico_city = City(name="Mexico City", population=20998543)
mumbai = City(name="Mumbai", population=21042538)
seo_paulo = City(name="Seo Paulo", population=21066245)
shanghai = City(name="Shanghai", population=23740778)
delhi = City(name="Delhi", population=25703168)
tokyo = City(name="Tokyo", population=38001000)
# Adding cities to the session
session.add(new_york)
session.add_all([cairo, osaka, beijing, mexico_city, mumbai, seo_paulo, shanghai, delhi, tokyo])

session.commit()
# Querying all the cities from the database
cities = session.execute(select(City)).scalars().all()
# Printing the city data with appropriate alignment and formatting
for city in cities:
    print(f"{city.id:<3} {city.name:<13} {city.population:>13,}")

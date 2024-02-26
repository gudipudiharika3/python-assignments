"""
HW: 5
Problem: 2
Author: Harika Padmini
"""
import sqlalchemy
from sqlalchemy import Integer, Column, String, select, desc, delete
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func

# declaring base class
Base = declarative_base()


# declaring City base class
class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    population = Column(Integer)


# Sorting the city population in ascending order
def sort_cities_by_population_asc_order():
    results = session.execute(select(City).order_by(City.population)).scalars().all()
    print("Cities Sorted By Population in Ascending Order\n"
          "-----------------------------------------------")
    for city in results:
        print(f"{city.id} {city.name} {city.population}")


# Sorting the city population in descending order
def sort_cities_by_population_desc_order():
    print("Cities Sorted By Population in Descending Order\n"
          "-----------------------------------------------")
    results = session.execute(select(City).order_by(desc(City.population))).scalars().all()
    for city in results:
        print(f"{city.id} {city.name} {city.population}")


# Soring cities by names
def sort_cities_by_name():
    print("Cities Sorted By Name\n"
          "-----------------------------------------------")
    results = session.execute(select(City).order_by(City.name)).scalars().all()
    for city in results:
        print(f"{city.id} {city.name} {city.population}")


# Displaying total population
def display_total_population():
    total = session.query(func.sum(City.population)).scalar()
    print(f"Total Population: {total}")


# Displaying average salary
def display_avg_population():
    avg = session.query(func.avg(City.population)).scalar()
    print(f"Average Population: {avg}")


# Displaying the highest populated city
def display_city_with_highest_population():
    max_population = session.query(func.max(City.population)).scalar()
    results = session.query(City).filter(City.population == max_population).all()
    for city in results:
        print(f"{city.name} has the highest population {city.population}")


# Displaying the lowest populated city
def display_city_with_lowest_population():
    min_population = session.query(func.min(City.population)).scalar()
    results = session.query(City).filter(City.population == min_population).all()
    for city in results:
        print(f"{city.name} has the lowest population {city.population}")


# Updating the database
def add_new_city(city_name, city_population):
    session.add(City(name=city_name, population=city_population))
    session.commit()


# Deleting the record from the database
def delete_city(city_name):
    obj = delete(City).where(City.name == city_name)
    session.execute(obj)
    session.commit()


engine = sqlalchemy.create_engine('sqlite:///city.db')
session = sessionmaker(bind=engine, future=True)()
# Printing the menu
with open(r'C:\Users\harik\Downloads\menu.txt', "r", encoding="utf-8") as file:
    menu = file.read()
    print(menu)

while True:
    text = input("Please select (1 - 10):")
    if text == "1":
        sort_cities_by_population_asc_order()
    if text == "2":
        sort_cities_by_population_desc_order()
    if text == "3":
        sort_cities_by_name()
    if text == "4":
        display_total_population()
    if text == "5":
        display_avg_population()
    if text == "6":
        display_city_with_highest_population()
    if text == "7":
        display_city_with_lowest_population()
    if text == "8":
        city_name = input("Please enter the city: ")
        city_population = input("Please enter the population: ")
        add_new_city(city_name, city_population)
    if text == "9":
        city_name = input("Please enter city to delete: ")
        delete_city(city_name)
    if text == "10":
        ex = input("Do you want to exit the system? Enter y to confirm: ")
        if ex == "y":
            print("Exit the system...")
            break

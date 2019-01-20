import pymongo
from src.database import Database
from src.menu import Menu

Database.initialize()

menu = Menu()
menu.run_menu()


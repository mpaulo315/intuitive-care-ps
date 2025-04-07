from dotenv import load_dotenv
from os import getenv, path
import caribou

load_dotenv()

def run_migrations():
    db = getenv("DATABASE")
    if path.exists(db):
        return 
    
    print("Running migrations...")
    migration_dir = "api/migrations/"
    try:
        caribou.upgrade(db, migration_dir)
    except Exception as e:
        print(e)
        print("Migrations failed")
        exit(1)
    print("Migrations finished")
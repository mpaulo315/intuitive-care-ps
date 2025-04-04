import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from routers.operadoras import router as operadoras_router

from dotenv import load_dotenv
from os import getenv, path
import caribou

from db.insert_data import insert_csv_data

load_dotenv()

app = FastAPI(
    title="API de Operadoras",
    description="API para consultar operadoras de telefonia celular",
    version="1.0.0",
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)

app.include_router(router=operadoras_router, prefix="/api")

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


if __name__ == "__main__":
    run_migrations()

    file_path_list = ["api", "data", "cadop.csv"]
    insert_csv_data(file_path_list, "OPERADORAS", delimiter=";")
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, app_dir=".")
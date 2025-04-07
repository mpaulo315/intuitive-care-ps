import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from routers.operadoras import router as operadoras_router

from db import insert_csv_data, run_migrations

app = FastAPI(
    title="API de Operadoras",
    description="API para consultar operadoras de planos de saúde",
    version="1.0.0",
    docs_url="/docs",
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)

api_router = APIRouter(prefix="/api")

api_router.include_router(router=operadoras_router)
app.include_router(router=api_router)

@app.exception_handler(404)
async def handle_404(request, exc):
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    run_migrations()

    file_path_list = ["api", "data", "cadop.csv"]
    insert_csv_data(file_path_list, "OPERADORAS", delimiter=";")
    
    uvicorn.run("main:app", host="localhost", port=8000, reload=True, app_dir=".")
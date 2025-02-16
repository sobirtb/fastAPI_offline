from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles



app = FastAPI(
    docs_url = None,          
    redoc_url = None,         
    openapi_url = "/openapi.json", 
    title = "Project API",
    description = "This is a very fancy project, with auto docs for the API and everything.",
    version = "0.1.0",)


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui():
    return RedirectResponse(url="/static/swagger/index.html")


@app.get("/redoc", include_in_schema=False)
async def custom_redoc():
    return RedirectResponse(url="/static/redoc/index.html")


@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!",
            "Documentation": "/docs",
            "Redoc": f"/redoc"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
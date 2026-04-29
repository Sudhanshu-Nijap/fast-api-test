from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Setup Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"status": "Online", "platform": "Shipit"})

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "database": "connected", "server": "AWS Ubuntu"}

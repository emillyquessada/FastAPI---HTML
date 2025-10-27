#pip install fastapi uvicorn jinja2 python-multipart
from fastapi import FastAPI, request, Formfrom 
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title= "Lista de Alunos")

#Definir a pasta onde está os hyml
templates = Jinja2Templates(directory="templates")

#Definir a pasta onde está os arquivos estáticos (CSS, Imagens e JS)
app.mount("/static", StaticFiles(directory= "static"))


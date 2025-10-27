#pip install fastapi uvicorn jinja2 python-multipart
from fastapi import FastAPI, Request, Formfrom 
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title= "Lista de Alunos")

#Definir a pasta onde está os hyml
templates = Jinja2Templates(directory="templates")

#Definir a pasta onde está os arquivos estáticos (CSS, Imagens e JS)
app.mount("/static", StaticFiles(directory= "static"))

alunos = [
    {"nome": "Iago", "nota":8.5},
    {"nome": "Murilo", "nota":6.5},
    {"nome": "Francisco", "nota":8.0},
    {"nome": "Joana", "nota":9.5}
]

#Rota Principal

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "lista_alunos": alunos}
    )
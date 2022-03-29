from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from deta import Deta


# Key Name
# 5mpt6a

# Key Description
# Project Key: 5mpt6a

# Project Key
# b0wantux_NBtEAwKr6yWbqXqSFL2MN8S7wSu7DaYS

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
deta = Deta("b0wantux_NBtEAwKr6yWbqXqSFL2MN8S7wSu7DaYS")
g_sales_db = deta.Base("garage_sales")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/create", response_class=HTMLResponse)
async def create(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def search(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.post("/submit")
def submit_gsale(title: str = Form(...), description: str = Form(...), street: str = Form(...), city: str = Form(...),
                 zip: str = Form(...), state: str = Form(...),start_date: str = Form(...), end_date: str = Form(...)):

    g_sales_db.insert({"title": title, "description": description, "street": street, "city": city, "zip": zip,
                       "state": state, "start_date": start_date, "end_date": end_date})

    return {"message": "success"}



@app.get("/item/{id}/{name}", response_class=HTMLResponse)
async def read_item(request: Request, id: str, name: str):
    print(id)
    return templates.TemplateResponse("item.html", {"request": request, "id": id, "name": name})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="localhost", reload=True)
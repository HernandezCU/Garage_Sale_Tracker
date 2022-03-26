from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from deta import Deta
import uvicorn

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
async def read_root():
    return """
    <html>
        <title>Garage Sale Locator</title>
        <center>
            <h1 style="font-family: Bahnschrift, sans-serif; font-size:50px">Future home of Garage Sale Locator</h1>
            <p  style="font-family: Bahnschrift, sans-serif; font-size:25px" class="w3-large w3-center">add <a href="/docs" target="_blank">/docs</a> to your url to view endpoints</p>
        </center>
        
        <center>
            <form action="/submit" enctype="multipart/form-data" method="post">
                <label for="title">Title:</label>
                <input name="title" type="text"><br>
                
                <label for="description">Description:</label>
                <input name="description" type="text"><br>
                
                <label for="address">Address:</label>
                <input name="address" type="text"><br>
                
                <label for="start_date">Start Date:</label>
                <input name="start_date" type="date"><br>
                
                <label for="end_date">End Date:</label>
                <input name="end_date" type="date">><br>
                
                <input type="submit">
            </form>
        </center>
    </html>
    """


@app.post("/submit")
def submit_gsale(title: str = Form(...), description: str = Form(...),
                 address: str = Form(...), start_date: str = Form(...), end_date: str = Form(...)):
    print(title)
    print(description)
    print(address)
    print(start_date)
    print(end_date)
    g_sales_db.insert({"title": title, "description": description, "address": address,
                       "start_date": start_date, "end_date": end_date})

    return {"message": "success"}



@app.get("/item/{id}/{name}", response_class=HTMLResponse)
async def read_item(request: Request, id: str, name: str):
    print(id)
    return templates.TemplateResponse("item.html", {"request": request, "id": id, "name": name})



if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", reload=True)
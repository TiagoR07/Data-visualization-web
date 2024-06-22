from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Sample data - replace with your own dynamic data source
posts = [
    {'author': 'John Doe', 'title': 'Blog Post 1', 'content': 'First post content', 'date_posted': 'June 1, 2023'},
    {'author': 'Jane Smith', 'title': 'Blog Post 2', 'content': 'Second post content', 'date_posted': 'June 2, 2023'}
]

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "posts": posts})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

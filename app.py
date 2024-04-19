from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai import ai
from pydantic import BaseModel
import uvicorn

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    message: str


@app.get("/api/test")
async def test():
    return "Hello World"


@app.post("/api/chat")
async def ai_2(data: str):
    return ai(data)


@app.post("/api/name")
async def name(ticker:str,exchange:str):
    return name(ticker,exchange)

@app.post("/api/price")
async def price(ticker:str,exchange:str):
    price(ticker,exchange)
    
    
if __name__=='__main__':
    uvicorn.run('app:app',host='localhost',port=8000,reload=True)
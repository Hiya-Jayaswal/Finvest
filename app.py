from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai import ai
from ai import name
from ai import price
from ai_hiiiiiiiyaaaaaaaa import info
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
async def name_1(ticker:str,exchange:str):
    return name(ticker,exchange)

@app.post("/api/price")
async def price_2(ticker:str):
    return price(ticker)
    

@app.post("/api/information")
async def information(question:str):
    return info(question)
    
if __name__=='__main__':
    uvicorn.run('app:app',host='localhost',port=8000,reload=True)
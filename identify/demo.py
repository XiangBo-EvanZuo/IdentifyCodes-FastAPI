from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


@app.post("/items/")
async def create_item(price: float):
    return price

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=9001)


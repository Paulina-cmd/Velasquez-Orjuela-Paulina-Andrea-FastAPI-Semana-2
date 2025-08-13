from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

products = []

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None

@app.get("/")
def home() -> dict:
    return {"message": "¡Bienvenido a mi API mejorada con FastAPI!"}

@app.get("/products")
def get_products() -> List[Product]:
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int) -> dict:
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Producto no encontrado"}

@app.post("/products")
def create_product(product: Product) -> dict:
    products.append(product.dict())
    return {"message": "Producto creado exitosamente", "product": product}

@app.get("/search")
def search_product(name: str) -> List[dict]:
    return [p for p in products if name.lower() in p["name"].lower()]


from typing import List
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field


app = FastAPI(
    title="API Semana 2",
    description="API con mejoras: Type hints + Pydantic + Endpoint POST",
    version="2.0.0"
)


class Item(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Nombre del item")
    price: float = Field(..., gt=0, description="Precio positivo del item")
    tags: List[str] = Field(default=[], description="Lista opcional de etiquetas")



@app.get("/", tags=["Base"])
def read_root() -> dict:
    """
    Endpoint raíz de bienvenida.
    """
    return {"message": "Bienvenido a la API mejorada de Semana 2 🚀"}

@app.get("/items/{item_id}", tags=["Items"])
def read_item(
    item_id: int = Path(..., gt=0, description="ID del item, entero positivo"),
    q: str | None = Query(default=None, max_length=50, description="Filtro opcional")
) -> dict:
    """
    Devuelve un item por su ID con un filtro opcional.
    """
    return {"item_id": item_id, "query": q}


@app.post("/items/", tags=["Items"])
def create_item(item: Item) -> dict:
    """
    Crea un nuevo item con validación automática gracias a Pydantic.
    """
    return {
        "message": "Item creado exitosamente",
        "item": item.dict()
    }
